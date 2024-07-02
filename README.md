# Celery plugin for [Tutor](https://docs.tutor.edly.io)

A tutor plugin to extend the default LMS and CMS celery workers that comes
with tutor.

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

By default, tutor-contrib-celery enables the following queues for the services
with independent deployments for each:

- **CMS**: default, high, low
- **LMS**: default, high, low

> [!NOTE]
> We recommend using [tutor-contrib-pod-autoscaling](https://github.com/eduNEXT/tutor-contrib-pod-autoscaling)
> to setup requested resources and limits.

In case you are using different celery queues than the defaults on Open edX, you can
extend the list by setting `CELERY_WORKER_VARIANTS` on your `config.yml`. The format is the following:

```yaml
CELERY_WORKER_VARIANTS:
  lms:
    - high
    - low
  cms:
    - high
    - low
```

License
*******

This software is licensed under the terms of the AGPLv3.
