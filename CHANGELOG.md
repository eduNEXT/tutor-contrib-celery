# CHANGELOG

<!--
All enhancements and changes will be documented in this file.  It adheres to
the structure of http://keepachangelog.com/ ,

This project adheres to Semantic Versioning (http://semver.org/).
-->

## Unreleased

See the fragment files in the [changelog.d/ directory](./changelog.d).

<!-- scriv-insert-here -->

<a id='changelog-21.0.0'></a>
## 21.0.0 — 2026-01-28

### Added

- Support for the Ulmo release

<a id='changelog-20.0.0'></a>
## 20.0.0 — 2025-12-02

### Added

- Support for the Teak release.

<a id='changelog-19.0.0'></a>
## v19.0.0 (2024-12-18)

### Features

- Add support for sumac ([#13](https://github.com/eduNEXT/tutor-contrib-celery/pull/13),
  [`3d050c4`](https://github.com/eduNEXT/tutor-contrib-celery/commit/3d050c47d206ec4056985216317130ac03bc791e))

- Sumac release
  ([`7ace1d3`](https://github.com/eduNEXT/tutor-contrib-celery/commit/7ace1d317766758c950297693cc7f3ef68bd6568))


## v18.4.0 (2024-12-12)

### Chores

- **release**: Preparing 18.4.0
  ([`1c8cf03`](https://github.com/eduNEXT/tutor-contrib-celery/commit/1c8cf036ff10bbc9659ddfa7969e2ef45c670be4))

### Features

- Allow to pass extra parameters for celery workers
  ([#11](https://github.com/eduNEXT/tutor-contrib-celery/pull/11),
  [`f523906`](https://github.com/eduNEXT/tutor-contrib-celery/commit/f523906d4887bf96b02de9ed28d848f2dd1b9077))

(cherry picked from commit c858d5d0a7e285f050eda6057b214a5313691b0d)

docs: add section with extra parameters

refactor!: use new filter to define celery command

(cherry picked from commit 53fafef821a33979f24b867228487f812eb8524c)


## v18.3.0 (2024-09-12)

### Chores

- **release**: Preparing 18.3.0
  ([`c7732e5`](https://github.com/eduNEXT/tutor-contrib-celery/commit/c7732e56037c26de79a7f838b7d8f3c301bac4a4))

### Features

- Add keda autoscaling support ([#10](https://github.com/eduNEXT/tutor-contrib-celery/pull/10),
  [`d2c2f84`](https://github.com/eduNEXT/tutor-contrib-celery/commit/d2c2f846e88e92774bffe7de113df903ed794872))

* feat: add keda autoscaling support

* refactor: use a hook to extend celery config

* docs: update documentation with new filter

* fix: use not required validation

* fix: use listLength as string

* docs: add pod-autoscaling notes

* fix: allow to scale default workers

* chore: quality fixes

(cherry picked from commit b529b0c1a23bb80115ba4fe1a30690df4918fb7a)

* refactor: use enable_keda key per variant

(cherry picked from commit b52f142baeb821fc2779b89184503da25b1ef483)

* fix: only apply overrides if default variant is set

* fix: add missing enable_keda to typed dict

* feat: removing CELERY_MULTIQUEUE_ENABLED

* docs: clarify key entries for workers config

(cherry picked from commit 70aae3b563f669971b2076257347a5f377aef2c3)

---------

Co-authored-by: jfavellar90 <jhony.avella@edunext.co>


## v18.2.1 (2024-08-28)

### Bug Fixes

- Remove unnecessary schema property for service monitor
  ([#9](https://github.com/eduNEXT/tutor-contrib-celery/pull/9),
  [`089ca1f`](https://github.com/eduNEXT/tutor-contrib-celery/commit/089ca1fcd429a4258738868656dbe756c0758817))

* fix: remove unnecessary schema property for service monitor

* chore: update celery monitoring dashboard name

* chore: update default refresh rate to 5m

### Chores

- **release**: Preparing 18.2.1
  ([`317d8ae`](https://github.com/eduNEXT/tutor-contrib-celery/commit/317d8aeb1350e9bb433e52681bd45c4ae06e8651))


## v18.2.0 (2024-08-22)

### Chores

- **release**: Preparing 18.2.0
  ([`78f8b72`](https://github.com/eduNEXT/tutor-contrib-celery/commit/78f8b72e451730af65e15d72df4152b11ce8fab8))

### Features

- Allow to enable prometheus integration
  ([#8](https://github.com/eduNEXT/tutor-contrib-celery/pull/8),
  [`0c3a7c2`](https://github.com/eduNEXT/tutor-contrib-celery/commit/0c3a7c2df2965e64dee9df4562b65697e1a53950))

* feat: allow to enable prometheus integration

* docs: add prometheus documentation and custom dashboard

* chore: address PR suggestions

* fix: address PR suggestions

* chore: disable flower monitoring by default

* chore: remove extra spaces

* chore: improve docs


## v18.1.0 (2024-08-22)

### Bug Fixes

- Add port name for metrics
  ([`944b821`](https://github.com/eduNEXT/tutor-contrib-celery/commit/944b8219f6b1978c34f4a6c9561f8a49300b7e34))

- Allow to disable multiqueue tuning
  ([`43f3f1d`](https://github.com/eduNEXT/tutor-contrib-celery/commit/43f3f1d5b2324b87ce1902fc4ba3fd66c0f20227))

### Chores

- **release**: Preparing 18.1.0
  ([`9a46d7f`](https://github.com/eduNEXT/tutor-contrib-celery/commit/9a46d7f9c30979566f33d54e12fa97a19770b49b))

### Features

- Add flower host
  ([`b3e3e49`](https://github.com/eduNEXT/tutor-contrib-celery/commit/b3e3e4952a6e32a06be6a8930f7af98d05994091))

- Allow to customize flower docker image
  ([`909725d`](https://github.com/eduNEXT/tutor-contrib-celery/commit/909725dd984fac59b1deaaafe234ea58bdd5fde1))

- Allow to customize flower docker image
  ([`00e7d81`](https://github.com/eduNEXT/tutor-contrib-celery/commit/00e7d8120944aa5b0bd502f5b8bfc6aca1cc16c4))

- Allow to deploy flower
  ([`0644980`](https://github.com/eduNEXT/tutor-contrib-celery/commit/0644980908d3fb130c8ff5ab1a30ada9372050bb))

- Enable basic auth
  ([`ff22bed`](https://github.com/eduNEXT/tutor-contrib-celery/commit/ff22bed93fc241acc615346630b56ab52f3bf142))


## v18.0.0 (2024-07-10)

### Bug Fixes

- Only add explicity queues for production settings
  ([`2053dec`](https://github.com/eduNEXT/tutor-contrib-celery/commit/2053decb55dc66aa33987fb3400451c497d81ec3))

- Split tasks from lms and cms
  ([`1d80bbc`](https://github.com/eduNEXT/tutor-contrib-celery/commit/1d80bbc404cb963f3a71c2c6df7abdba03a2f16d))

- Use nameerror instead of attributeerror
  ([`d12e0bf`](https://github.com/eduNEXT/tutor-contrib-celery/commit/d12e0bf1400e67d5c744f286d50ae7210ca8a356))

- Use only valid queue names
  ([`7ca3225`](https://github.com/eduNEXT/tutor-contrib-celery/commit/7ca32254e77c7438c6627c63555f73f0a8368603))

- Use readme.md
  ([`c23ed8f`](https://github.com/eduNEXT/tutor-contrib-celery/commit/c23ed8f803dc29208d5cd864c7f8e9246df23838))

### Features

- Allow to run multiple celery queues and workers
  ([`ad0a4b0`](https://github.com/eduNEXT/tutor-contrib-celery/commit/ad0a4b08ddbfdc7f466442b2eb61c048c52ad39b))
