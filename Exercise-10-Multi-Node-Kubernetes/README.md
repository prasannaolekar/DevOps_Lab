\# Exercise 10: Multi-Node Kubernetes Cluster with Multiple Applications and ReplicaSets



\## Objective

Deploy two Flask applications on a three-node Minikube Kubernetes cluster using Docker images, Deployments, Services, and ReplicaSets.



\## Applications

1\. \*\*Product Catalog:\*\* Provides a list of products through the `/products` endpoint.

2\. \*\*Shopping Cart:\*\* Supports retrieving cart items using `GET /cart` and adding items using `POST /cart`.



\## Technologies Used

\- Docker

\- Kubernetes

\- Minikube

\- Python

\- Flask

\- YAML



\## Cluster Configuration

\- 1 control-plane node

\- 2 worker nodes

\- Product Catalog: 2 replicas

\- Shopping Cart: 3 replicas

\- NodePort Services for both applications

\- Pod anti-affinity to distribute replicas across nodes



\## Project Structure

```text

Exercise-10-Multi-Node-Kubernetes/

├── product-catalog/

│   ├── Dockerfile

│   └── product\_catalog.py

├── shopping-cart/

│   ├── Dockerfile

│   └── shopping\_cart.py

├── k8s/

│   ├── product-catalog.yaml

│   ├── shopping-cart.yaml

│   ├── product-catalog-service.yaml

│   └── shopping-cart-service.yaml

├── screenshots/

└── README.md

```



\## Deployment Commands

```powershell

minikube start --nodes 3 -p devops-multinode --driver=docker

minikube -p devops-multinode addons enable registry



docker build -t product-catalog:latest -f product-catalog/Dockerfile product-catalog

docker build -t shopping-cart:latest -f shopping-cart/Dockerfile shopping-cart



minikube -p devops-multinode image load product-catalog:latest

minikube -p devops-multinode image load shopping-cart:latest



kubectl --context=devops-multinode apply -f k8s/product-catalog.yaml

kubectl --context=devops-multinode apply -f k8s/shopping-cart.yaml

kubectl --context=devops-multinode apply -f k8s/product-catalog-service.yaml

kubectl --context=devops-multinode apply -f k8s/shopping-cart-service.yaml

```



\## Verification

```powershell

kubectl --context=devops-multinode get nodes

kubectl --context=devops-multinode get pods -o wide

kubectl --context=devops-multinode get deployments

kubectl --context=devops-multinode get services

```



\## Test Results

\- All three Kubernetes nodes reached the Ready state.

\- Product Catalog: 2/2 replicas running.

\- Shopping Cart: 3/3 replicas running.

\- Product Catalog `/products` endpoint returned three products.

\- Shopping Cart `/cart` endpoint returned the expected JSON response after adding a laptop.



\## Screenshots

Screenshots demonstrating the cluster, images, pod distribution, deployments, services, and application responses are available in the `screenshots/` directory.





