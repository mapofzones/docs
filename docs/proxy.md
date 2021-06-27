# Proxy

## Add new node to Proxy server

Add a parameter after the list of available nodes:
```squid
acl k8 src <ip address node>/32
```
And reconfigure squid:
```squid
  squid -k reconfigure
```
## Using proxy from kubernetes

Add enviroment to container

```kubernetes
   env:
    - name: http_proxy
      value: http://46.101.95.106:9999
    - name: https_proxy
      value: http://46.101.95.106:9999
```
## Check logs to access data from node:
  tail /var/log/squid/access.log