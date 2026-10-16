\# Exercise 1: Kubernetes Hello Pod



\## Objective

Deploy an Nginx application on a local Kubernetes cluster using Minikube and expose it through a NodePort Service.



\## Tools Used

\- Docker Desktop

\- Kubernetes

\- Minikube

\- kubectl

\- Nginx



\## Implementation

1\. Started the Minikube cluster using the Docker driver.

2\. Verified that the Kubernetes node was Ready.

3\. Deployed an Nginx Pod named `hello-k8s`.

4\. Verified that the Pod was running.

5\. Exposed the Pod using a NodePort Service.

6\. Opened the Nginx welcome page in a browser.

7\. Created Kubernetes YAML manifests for the Pod and Service.



\## Project Structure

```text

Exercise-1-Kubernetes/

├── README.md

├── k8s/

│   ├── pod.yaml

│   └── service.yaml

└── screenshots/

&#x20;   ├── 01-pod-running.png

&#x20;   ├── 02-service.png

&#x20;   └── 03-nginx-browser.png

```



\## Deploy Using YAML

Run these commands when the resources do not already exist:



```powershell

kubectl apply -f k8s/pod.yaml

kubectl apply -f k8s/service.yaml

kubectl get pods

kubectl get services

```



\## Screenshots

The `screenshots/` directory contains evidence of the Pod status, NodePort Service, and Nginx welcome page.



\## Result

Successfully deployed Nginx on Minikube and accessed it through a Kubernetes Service.



