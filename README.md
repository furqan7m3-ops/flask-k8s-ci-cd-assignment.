# Flask App Kubernetes Deployment

## Project Description

This project demonstrates deploying a simple Flask application using Docker and Kubernetes.
It covers key Kubernetes features such as:

* **Automated Rollouts:** Rolling updates for deployments to ensure zero downtime.
* **Scaling:** Multiple replicas for handling increased load.
* **Load Balancing:** NodePort service to distribute traffic across pods.

The repository includes:

* `deployment.yaml` – Kubernetes Deployment manifest with rolling update strategy, replicas, and resource limits.
* `service.yaml` – NodePort Service for exposing the application.
* `Dockerfile` – Docker image definition for the Flask app.
* `app.py` – Simple Flask "Hello World" application.

---

## Build and Run Locally Using Docker

1. **Build the Docker image**

```bash
docker build -t flask-app:latest .
```

2. **Run the Docker container**

```bash
docker run -p 5000:5000 flask-app:latest
```

3. **Access the application**
   Open a browser or use curl:

```
http://localhost:5000/
```

---

## Deploy to Kubernetes

> Note: Jenkins pipeline is ignored for now. Manual deployment instructions:

1. **Ensure Minikube is running**

```bash
minikube start
```

2. **Apply Kubernetes manifests**

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

3. **Verify deployment**

```bash
kubectl rollout status deployment/flask-app-deployment
kubectl get pods
kubectl get services
```

4. **Access the application through NodePort**

```bash
minikube service flask-app-service
```

---

## Kubernetes Features Explained

### Automated Rollouts

* The Deployment uses a **rolling update strategy** with:

  * `maxSurge: 1` – One extra pod can be created during updates.
  * `maxUnavailable: 1` – At most one pod can be unavailable during updates.
* This ensures updates happen gradually without downtime.

### Scaling

* The deployment has multiple replicas (`replicas: 3` by default).
* You can scale the deployment manually:

```bash
kubectl scale deployment flask-app-deployment --replicas=5
kubectl get pods
```

* Kubernetes ensures traffic is distributed among all pods.

### Load Balancing

* The **NodePort service** exposes the application on a port (default: 30080).
* Kubernetes automatically load balances traffic across all running pods in the deployment.

---

## Notes

* Make sure Docker and kubectl are installed on your machine.
* For local testing, Minikube must be running.
* All manifests and scripts are located in the root of this repository.
