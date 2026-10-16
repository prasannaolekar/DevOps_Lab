\# Exercise 3: Scaling Flask App on a Single Node Using ReplicaSets



\## Objective

Deploy a Flask-based flash sale application on Minikube using a Kubernetes ReplicaSet and Service. Demonstrate scaling, health checks, and automatic Pod replacement.



\## Application Features

\- `/` — Displays the welcome message, Pod hostname, and timestamp.

\- `/buy?user=Prasanna` — Simulates a purchase and returns the selected product, user, status, and serving Pod.

\- `/health` — Checks application health and returns the Pod hostname.



\## Technologies Used

\- Python and Flask

\- Docker

\- Kubernetes ReplicaSet and Service

\- Minikube



\## Implementation Steps

1\. Created the Flask application and Dockerfile.

2\. Built the `flashsale:1.0` image inside Minikube.

3\. Created a Kubernetes ReplicaSet with an initial three replicas.

4\. Configured a ClusterIP Service to expose the application internally.

5\. Tested the application using port forwarding and verified the `/`, `/health`, and `/buy` endpoints.

6\. Scaled the ReplicaSet from three to five replicas.

7\. Deleted one Flash Sale Pod and verified that Kubernetes automatically created a replacement.

8\. Used `kubectl get pods -o wide` to verify that all five Pods run on the single Minikube node.



\## Commands Used



```powershell

minikube image build -t flashsale:1.0 "Exercise-3-Flash-Sale"



kubectl apply -f "Exercise-3-Flash-Sale\\k8s\\flashsale-replicaset.yaml"



kubectl get rs flashsale-rs

kubectl get pods -l app=flashsale



kubectl port-forward service/flashsale-svc 8085:80



kubectl scale rs flashsale-rs --replicas=5



kubectl get pods -l app=flashsale -o wide

```



\## Results

\- All five replicas reached the Running state and passed readiness checks.

\- The application endpoints returned successful responses.

\- The ReplicaSet automatically replaced a deleted Pod, restoring the desired replica count.

\- All five Pods were scheduled on the single Minikube node.



\## Screenshots

1\. `screenshots/01-three-replicas.png` — Initial three replicas.

2\. `screenshots/02-five-replicas.png` — Scaling to five replicas.

3\. `screenshots/03-pod-replaced.png` — Automatic Pod replacement.

4\. `screenshots/04-pod-distribution.png` — Five Pods on the single Minikube node.



\## Conclusion

The exercise demonstrates Kubernetes ReplicaSet scaling and self-healing for a Flask application running on a single-node Minikube cluster.



