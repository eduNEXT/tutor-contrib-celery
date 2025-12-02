from __future__ import annotations

import os
from glob import glob

import importlib_resources
from tutor import hooks

from tutorcelery.__about__ import __version__
from tutorcelery.hooks import CELERY_WORKERS_ATTRS_TYPE, CELERY_WORKERS_CONFIG

CORE_CELERY_WORKER_CONFIG: dict[str, dict[str, CELERY_WORKERS_ATTRS_TYPE]] = {
    "lms": {
        "default": {
            "min_replicas": 0,
            "max_replicas": 10,
            "list_length": 40,
            "enable_keda": False,
        },
    },
    "cms": {
        "default": {
            "min_replicas": 0,
            "max_replicas": 10,
            "list_length": 40,
            "enable_keda": False,
        },
    },
}


# The core autoscaling configs are added with a high priority, such that other users can override or
# remove them.
@CELERY_WORKERS_CONFIG.add(priority=hooks.priorities.HIGH)
def _add_core_autoscaling_config(
    scaling_config: dict[str, dict[str, CELERY_WORKERS_ATTRS_TYPE]],
) -> dict[str, dict[str, CELERY_WORKERS_ATTRS_TYPE]]:
    scaling_config.update(CORE_CELERY_WORKER_CONFIG)
    return scaling_config


@hooks.lru_cache
def get_celery_workers_config() -> dict[str, dict[str, CELERY_WORKERS_ATTRS_TYPE]]:
    """
    This function is cached for performance.
    """
    return CELERY_WORKERS_CONFIG.apply({})


def iter_celery_workers_config() -> dict[str, dict[str, CELERY_WORKERS_ATTRS_TYPE]]:
    """
    Yield:

        (name, dict)
    """
    return {name: config for name, config in get_celery_workers_config().items()}


def is_celery_multiqueue(service: str) -> bool:
    """
    This function validates whether celery is configured in multiqueue mode for a given service
    """
    service_celery_config = iter_celery_workers_config().get(service, {})
    service_queue_len = len(service_celery_config.keys())

    # If no queue variants are configured, multiqueue is disabled
    if not service_queue_len:
        return False

    # Multiqueue is not enabled if only the default variant is available
    if service_queue_len == 1 and "default" in service_celery_config:
        return False

    return True


@hooks.Actions.PROJECT_ROOT_READY.add()
def configure_default_workers(root: str) -> None:
    if is_celery_multiqueue("lms"):
        hooks.Filters.LMS_WORKER_COMMAND.add_items(["--queues=edx.lms.core.default"])
    if is_celery_multiqueue("cms"):
        hooks.Filters.CMS_WORKER_COMMAND.add_items(["--queues=edx.cms.core.default"])


hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        # Add your new settings that have default values here.
        # Each new setting is a pair: (setting_name, default_value).
        # Prefix your setting names with 'CELERY_'.
        ("CELERY_VERSION", __version__),
        ("CELERY_LMS_EXPLICIT_QUEUES", {}),
        ("CELERY_CMS_EXPLICIT_QUEUES", {}),
        ("CELERY_FLOWER", False),
        ("CELERY_FLOWER_EXPOSE_SERVICE", False),
        ("CELERY_FLOWER_HOST", "flower.{{LMS_HOST}}"),
        ("CELERY_FLOWER_DOCKER_IMAGE", "docker.io/mher/flower:2.0.1"),
        ("CELERY_FLOWER_SERVICE_MONITOR", False),
    ]
)

hooks.Filters.CONFIG_UNIQUE.add_items(
    [
        # Add settings that don't have a reasonable default for all users here.
        # For instance: passwords, secret keys, etc.
        # Each new setting is a pair: (setting_name, unique_generated_value).
        # Prefix your setting names with 'CELERY_'.
        # For example:
        ### ("CELERY_SECRET_KEY", "{{ 24|random_string }}"),
        ("CELERY_FLOWER_BASIC_AUTH", "flower:{{ 24 |random_string }}")
    ]
)

hooks.Filters.CONFIG_OVERRIDES.add_items(
    [
        # Danger zone!
        # Add values to override settings from Tutor core or other plugins here.
        # Each override is a pair: (setting_name, new_value). For example:
        ### ("PLATFORM_NAME", "My platform"),
    ]
)


hooks.Filters.ENV_TEMPLATE_ROOTS.add_items(
    # Root paths for template files, relative to the project root.
    [
        str(importlib_resources.files("tutorcelery") / "templates"),
    ]
)

hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    # For each pair (source_path, destination_path):
    # templates at ``source_path`` (relative to your ENV_TEMPLATE_ROOTS) will be
    # rendered to ``source_path/destination_path`` (relative to your Tutor environment).
    # For example, ``tutorcelery/templates/celery/build``
    # will be rendered to ``$(tutor config printroot)/env/plugins/celery/build``.
    [
        ("celery/k8s", "plugins"),
    ],
)


# Make the pod-autoscaling hook functions available within templates
hooks.Filters.ENV_TEMPLATE_VARIABLES.add_items(
    [
        ("iter_celery_workers_config", iter_celery_workers_config),
        ("is_celery_multiqueue", is_celery_multiqueue),
    ]
)

# For each file in tutorcelery/patches,
# apply a patch based on the file's name and contents.
for path in glob(str(importlib_resources.files("tutorcelery") / "patches" / "*")):
    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item((os.path.basename(path), patch_file.read()))
