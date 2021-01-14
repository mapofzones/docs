# Add new node to Proxy server

Add a parameter after the list of available nodes:

acl k8 src <ip address node>/32

Reconfigure squid:
  squid -k reconfigure

# Using proxy from kubernetes

Add enviroment to container

  env:
    - name: http_proxy
      value: http://46.101.95.106:9999
    - name: https_proxy
      value: http://46.101.95.106:9999

#Check logs to access data from node:
  tail /var/log/squid/access.log