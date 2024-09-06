"""
These hooks are stored in a separate module. If they were included in plugin.py, then
the pod-autoscaling hooks would be created in the context of some other plugin that imports
them.
"""

from __future__ import annotations

from typing import TypedDict, NotRequired

from tutor.core.hooks import Filter


class CELERY_WORKERS_ATTRS_TYPE(TypedDict):
    min_replicas: NotRequired[int]
    max_replicas: NotRequired[int]
    list_length: NotRequired[int]


CELERY_WORKERS_CONFIG: Filter[dict[str, dict[str, CELERY_WORKERS_ATTRS_TYPE]], []] = (
    Filter()
)
