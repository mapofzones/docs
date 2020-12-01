# CI/CD/CD

## Continuous Integration

Continuous integration has several main stages:

* When changes are pushed to the master branch of the repositories at [github.com/mapofzones](https://github.com/mapofzones), **GitHub Actions** are triggered.
* **GitHub Actions** builds, tests, creates docker images and publishes them in our container registry on DigitalOcean - `registry.digitalocean.com/mapofzones`.
* After completing the job, **GitHub Actions** sends a notification to the telegram chat about the success or failure of the execution.

**GitHub Actions** workflow settings are described in each repository in the `.github/workflows` directory.

Each GitHub repository has secret keys for publishing images, for sending messages to telegrams, etc.

## Continuous Delivery

## Continuous Deployment