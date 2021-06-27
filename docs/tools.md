# Tools

## ArgoCD

An example of ArgoCD port forwarding. You must specify the kubectl keys and know the argocd admin panel password.
```
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

## Grafana

An example of Grafana port forwarding. You must specify the kubectl keys and know the grafana admin panel password.
```
kubectl port-forward svc/prometheus-operator-grafana -n prometheus-operator 9090:80
```
