# Celery plugin for [Tutor](https://docs.tutor.edly.io)

A tutor plugin to extend the default LMS and CMS celery workers included in Tutor.
It adds and configures extra deployments running LMS and CMS celery workers where
every deployment will process async tasks routed to a specific queue. Having this
workers separation per queue can help to define the scaling requirements for the Celery
deployments, since having a single queue (the default one) with a single deployment can
lead to unexpected behaviors when running large-scale sites.

## Installation

```shell
pip install git+https://github.com/eduNEXT/tutor-contrib-celery
```

## Usage

```shell
tutor plugins enable celery
```

## Configuration

### Celery queues

By default, tutor-contrib-celery enables the following queues with independent deployments
for each:

- **CMS**: default, high, low (taken from CMS settings [here](https://github.com/openedx/edx-platform/blob/open-release/redwood.master/cms/envs/common.py#L1578-L1582))
- **LMS**: default, high, high_mem (taken from LMS settings [here](https://github.com/openedx/edx-platform/blob/open-release/redwood.master/lms/envs/common.py#L2913-L2917))

> [!NOTE]
> We recommend using [tutor-contrib-pod-autoscaling](https://github.com/eduNEXT/tutor-contrib-pod-autoscaling)
> to setup requested resources and limits.

In case you are using different celery queues than the defaults from Open edX, you can
extend the list by using the filter `CELERY_WORKERS_CONFIG` on a patch, e.g:

```python

from tutorcelery.hooks import CELERY_WORKERS_CONFIG

@CELERY_WORKERS_CONFIG.add()
def _add_celery_workers_config(workers_config):
    # Setup params for the lms high queue
    workers_config["lms"]["high"] = {
        "min_replicas": 0,
        "max_replicas": 30,
        "list_length": 40,
        "enable_keda": True,
    }
    # Add another queue to the lms with empty params
    workers_config["lms"]["very_low"] = {}
    return workers_config
```

This plugin also provides a setting to directly route LMS/CMS tasks to an specific queue. It can extends/overrides
the default `EXPLICIT_QUEUES` setting:

```yaml
CELERY_LMS_EXPLICIT_QUEUES:
  lms.djangoapps.grades.tasks.compute_all_grades_for_course:
    queue: edx.lms.core.high_mem
CELERY_CMS_EXPLICIT_QUEUES:
  cms.djangoapps.contentstore.tasks.import_olx:
    queue: edx.cms.core.high
```

### Autoscaling

This plugins supports Celery workers autoscaling based on the size of the celery queue of a given worker variant. We are using
Keda autoscaling for this purposes, check the [Keda documentation](https://keda.sh/docs) to find out more.

To enable autoscaling you need to enable the `enable_keda` key for every queue variant. The defaults parameters are the following:

```python
{
  "min_replicas": 0,
  "max_replicas": 30,
  "list_length": 40,
  "enable_keda": False,
}
```

> [!NOTE]
> You can use the filter `CELERY_WORKERS_CONFIG` as shown above to modify the scaling parameters.

If you are using [tutor-contrib-pod-autoscaling](https://github.com/eduNEXT/tutor-contrib-pod-autoscaling) and want to setup Keda autoscaling make sure to disable HPA for the `lms-worker` and the `cms-worker` as you shouldn't use both autoscalers.

```python
from tutorpod_autoscaling.hooks import AUTOSCALING_CONFIG

@AUTOSCALING_CONFIG.add()
def _add_my_autoscaling(autoscaling_config):
    autoscaling_config["lms-worker"].update({
      "enable_hpa": False,
    })
    autoscaling_config["cms-worker"].update({
      "enable_hpa": False,
    })
    return autoscaling_config
```

### Enable flower

For troubleshooting purposes, you can enable a flower deployment to monitor in realtime the Celery queues
times and performance:

```yaml
CELERY_FLOWER: true
```

#### Enable Flower Prometheus Integration

If you are running grafana you can use the attached [config map](resources/configmap.yaml) to import a custom Grafana dashboard to monitor
celery metrics such as:

- Total Queue Length
- Queue Length by task name
- Celery Worker Status
- Number of Tasks Currently Executing at Worker
- Average Task Runtime at Worker
- Task Prefetch Time at Worker
- Number of Tasks Prefetched at Worker
- Tasks Success Ratio
- Tasks Failure Ratio

If you are using the [Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator) you can enable a ServiceMonitor resource to automatically configure a scrape target for the flower service.

```yaml
CELERY_FLOWER_SERVICE_MONITOR: true
```

License

---

This software is licensed under the terms of the AGPLv3.
