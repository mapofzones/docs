# CI/CD/CD

![delivery-vs-deploy](img/map-of-zones-delivery vs deploy.jpg)

>*To put it simply continuous integration is part of both continuous delivery and continuous deployment. And continuous deployment is like continuous delivery, except that releases happen automatically.*

## Continuous Integration

>*Developers merge their changes back to the main branch as often as possible. The developer's changes are validated by creating a build and running automated tests against the build. By doing so, you avoid integration challenges that can happen when waiting for release day to merge changes into the release branch.*<br>
>*Continuous integration puts a great emphasis on testing automation to check that the application is not broken whenever new commits are integrated into the main branch.*


**Continuous integration has several main stages:**

* When changes are pushed to the master branch of the repositories at [github.com/mapofzones](https://github.com/mapofzones), **GitHub Actions** are triggered.
* **GitHub Actions** builds, tests, creates docker images and publishes them in our container registry on DigitalOcean - `registry.digitalocean.com/mapofzones`.
* After completing the job, **GitHub Actions** sends a notification to the telegram chat about the success or failure of the execution.

**GitHub Actions** workflow settings are described in each repository in the `.github/workflows` directory.

Each GitHub repository has secret keys for publishing images, for sending messages to telegrams, etc.

## Continuous Delivery

>*Continuous delivery is an extension of continuous integration since it automatically deploys all code changes to a testing and/or production environment after the build stage.*<br>
>*This means that on top of automated testing, you have an automated release process and you can deploy your application any time by clicking a button or automatically.*

<!-- todo: describe out steps -->

## Continuous Deployment

>*Continuous deployment goes one step further than continuous delivery. With this practice, every change that passes all stages of your production pipeline is released to your product.*

<!-- todo: describe out steps -->