#!/bin/bash
eval $(minikube -p minikube docker-env)
docker build -t flask-app:1.0 .