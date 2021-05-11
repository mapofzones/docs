# Architecture

## System context architecture

![Architecture-system](img/map-of-zones-System context.png)

## Solution architecture

![Architecture-prod](img/map-of-zones-Deploy kube.png)

## Service adaptor architecture

![Architecture-adaptor](img/map-of-zones-Adaptor.png)

* triggered every 10 sec(+runtime)
* calls database functions
* functions calculate all statistics from database engine tables
* new statistics are returned to the adapter
* inserts a pack of upcoming stats items into the DB flat tables

## Service endpoint checker

![Architecture-endpoint-checker](img/map-of-zones-Endpoint checker.png)

* triggered every 10 sec(+runtime)
* gets endpoints data from core database tables
* makes requests to the cosmos network for the received endpoints
* checks if endpoints are working correctly
* updates endpoint information in database core tables