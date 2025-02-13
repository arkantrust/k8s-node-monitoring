# K8s Node Monitoring

[![Publish GHCR](https://github.com/arkantrust/k8s-node-monitoring/actions/workflows/publish.yaml/badge.svg)](https://github.com/arkantrust/k8s-node-monitoring/actions/workflows/publish.yaml)

This project is a simple monitoring tool for Kubernetes nodes. It is a simple web application that displays the status of the nodes in a Kubernetes cluster. The application is written in FastAPI and uses psutil to get the system information.

I took inspiration from [Nasiullha's video](https://www.youtube.com/watch?v=kBWCsHEcWnc) and added WebSockets to update the status of the nodes in real-time.

To run this project using docker simply run:

``` bash
docker run -d -p 8090:8000 --name k8s-node-monitoring ghcr.io/arkantrust/k8s-node-monitoring:1.0.0
```
