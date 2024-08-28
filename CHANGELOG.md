# CHANGELOG

## v18.2.1 (2024-08-28)

### Fix

* fix: remove unnecessary schema property for service monitor (#9)

* fix: remove unnecessary schema property for service monitor

* chore: update celery monitoring dashboard name

* chore: update default refresh rate to 5m ([`089ca1f`](https://github.com/eduNEXT/tutor-contrib-celery/commit/089ca1fcd429a4258738868656dbe756c0758817))

## v18.2.0 (2024-08-22)

### Chore

* chore(release): preparing 18.2.0 ([`78f8b72`](https://github.com/eduNEXT/tutor-contrib-celery/commit/78f8b72e451730af65e15d72df4152b11ce8fab8))

### Feature

* feat: allow to enable prometheus integration (#8)

* feat: allow to enable prometheus integration

* docs: add prometheus documentation and custom dashboard

* chore: address PR suggestions

* fix: address PR suggestions

* fix: address PR suggestions

* chore: disable flower monitoring by default

* chore: remove extra spaces

* chore: improve docs ([`0c3a7c2`](https://github.com/eduNEXT/tutor-contrib-celery/commit/0c3a7c2df2965e64dee9df4562b65697e1a53950))

## v18.1.0 (2024-08-22)

### Chore

* chore(release): preparing 18.1.0 ([`9a46d7f`](https://github.com/eduNEXT/tutor-contrib-celery/commit/9a46d7f9c30979566f33d54e12fa97a19770b49b))

### Feature

* feat: add flower host ([`b3e3e49`](https://github.com/eduNEXT/tutor-contrib-celery/commit/b3e3e4952a6e32a06be6a8930f7af98d05994091))

* feat: enable basic auth ([`ff22bed`](https://github.com/eduNEXT/tutor-contrib-celery/commit/ff22bed93fc241acc615346630b56ab52f3bf142))

* feat: allow to customize flower docker image ([`909725d`](https://github.com/eduNEXT/tutor-contrib-celery/commit/909725dd984fac59b1deaaafe234ea58bdd5fde1))

* feat: allow to customize flower docker image ([`00e7d81`](https://github.com/eduNEXT/tutor-contrib-celery/commit/00e7d8120944aa5b0bd502f5b8bfc6aca1cc16c4))

* feat: allow to deploy flower ([`0644980`](https://github.com/eduNEXT/tutor-contrib-celery/commit/0644980908d3fb130c8ff5ab1a30ada9372050bb))

### Fix

* fix: add port name for metrics ([`944b821`](https://github.com/eduNEXT/tutor-contrib-celery/commit/944b8219f6b1978c34f4a6c9561f8a49300b7e34))

* fix: allow to disable multiqueue tuning ([`43f3f1d`](https://github.com/eduNEXT/tutor-contrib-celery/commit/43f3f1d5b2324b87ce1902fc4ba3fd66c0f20227))

### Unknown

* Merge pull request #5 from eduNEXT/cag/flower-improvements

feat: add flower host ([`e3815ab`](https://github.com/eduNEXT/tutor-contrib-celery/commit/e3815abd9ad84efc36271eeda3c22c7eeba70b16))

* Merge pull request #4 from eduNEXT/cag/release

chore: add release workflow ([`dbf1288`](https://github.com/eduNEXT/tutor-contrib-celery/commit/dbf1288833211c5220c18c540889c62c8179fa44))

* Merge pull request #3 from eduNEXT/cag/flag

fix: allow to disable multiqueue tuning ([`b7c3e1e`](https://github.com/eduNEXT/tutor-contrib-celery/commit/b7c3e1e42bdc04a43b4c5fd29826a2f381b001bf))

* Merge pull request #2 from eduNEXT/cag/add-flower

feat: allow to deploy flower ([`211c58b`](https://github.com/eduNEXT/tutor-contrib-celery/commit/211c58b0369adb046f6f0ac0584ff0bb6ff3e68f))

## v18.0.0 (2024-07-10)

### Feature

* feat: allow to run multiple celery queues and workers ([`ad0a4b0`](https://github.com/eduNEXT/tutor-contrib-celery/commit/ad0a4b08ddbfdc7f466442b2eb61c048c52ad39b))

### Fix

* fix: split tasks from lms and cms ([`1d80bbc`](https://github.com/eduNEXT/tutor-contrib-celery/commit/1d80bbc404cb963f3a71c2c6df7abdba03a2f16d))

* fix: use nameerror instead of attributeerror ([`d12e0bf`](https://github.com/eduNEXT/tutor-contrib-celery/commit/d12e0bf1400e67d5c744f286d50ae7210ca8a356))

* fix: use only valid queue names ([`7ca3225`](https://github.com/eduNEXT/tutor-contrib-celery/commit/7ca32254e77c7438c6627c63555f73f0a8368603))

* fix: only add explicity queues for production settings ([`2053dec`](https://github.com/eduNEXT/tutor-contrib-celery/commit/2053decb55dc66aa33987fb3400451c497d81ec3))

* fix: use readme.md ([`c23ed8f`](https://github.com/eduNEXT/tutor-contrib-celery/commit/c23ed8f803dc29208d5cd864c7f8e9246df23838))

### Unknown

* Merge pull request #1 from eduNEXT/cag/celery-queue

feat: allow to run multiple celery queues and workers ([`ceb9e3b`](https://github.com/eduNEXT/tutor-contrib-celery/commit/ceb9e3b7b6eb7eda9fa4fc6fcdbbf6e1b851d638))
