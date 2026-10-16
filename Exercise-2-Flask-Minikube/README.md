# Exercise 2: Deploy a Flask App on Minikube

## Objective
Deploy a Python Flask application on a local Kubernetes cluster using Minikube, Docker, kubectl, and YAML manifests.

## Technologies Used
- Python
- Flask
- Docker
- Kubernetes
- Minikube
- kubectl
- YAML

## Project Structure
```text
Exercise-2-Flask-Minikube/
|-- app.py
|-- Dockerfile
|-- README.md
|-- k8s/
|   |-- flask-deployment.yaml
|   `-- flask-service.yaml
`-- screenshots/
    `-- 04-flask-browser.png
```

## Flask Application
The application returns:

`Hello from Flask on Kubernetes!`

The Flask server listens on port 15000.

## Docker Image
The application uses `flask-app:latest`. The image is already available in Minikube, and the Deployment uses `imagePullPolicy: Never`.

## Kubernetes Deployment
The Deployment runs one replica of the Flask application.

Apply the Deployment:

```powershell
kubectl apply -f k8s/flask-deployment.yaml
```

Verify the Deployment and Pod:

```powershell
kubectl get deployments
kubectl get pods -l app=flask-app
```

## Kubernetes Service
The NodePort Service exposes port 15000 and forwards requests to container port 15000.

Apply the Service:

```powershell
kubectl apply -f k8s/flask-service.yaml
```

Get the service URL:

```powershell
minikube service flask-app-service --url
```

Open the generated URL in a browser.

## Verification
The application was accessed through the Minikube Service URL and returned:

`Hello from Flask on Kubernetes!`

## Screenshot
The browser verification screenshot is intended to be saved as `screenshots/04-flask-browser.png`.