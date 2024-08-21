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
extend the list by setting `CELERY_WORKER_VARIANTS` on your `config.yml`. The format is the following:

```yaml
CELERY_WORKER_VARIANTS:
  lms:
    - high
    - high_mem
    - lms_custom_queue
  cms:
    - high
    - low
    - cms_custom_queue
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

Make sure to enable the ServiceMonitor resource to inform Prometheus to scrape metrics from the flower service

```yaml
CELERY_FLOWER_PROMETHEUS: true
```

License
*******

This software is licensed under the terms of the AGPLv3.
