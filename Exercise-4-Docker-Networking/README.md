\# Exercise 4: Docker Networking with Multiple Containers



\## Objective

Understand Docker networking and configure a multi-container application using a custom bridge network.



\## Scenario

The application consists of three containers:

\- \*\*Flask:\*\* Python REST API server

\- \*\*MySQL:\*\* Database container

\- \*\*Redis:\*\* Cache container



\## Technologies Used

\- Docker and Docker Bridge Networking

\- Python and Flask

\- MySQL 8.4

\- Redis 7



\## Implementation



1\. Created a custom bridge network named `my-bridge-net`.

2\. Inspected the network configuration, including its subnet and gateway.

3\. Built the Flask image using `flask-api:1.0`.

4\. Launched the MySQL, Redis, and Flask containers on the same network.

5\. Exposed Flask port 5001 on the host.

6\. Tested the REST API using the `/about` endpoint.

7\. Inspected the bridge network to confirm that all three containers were connected.

8\. Tested Docker's internal DNS by resolving the MySQL and Redis container names from Flask.



\## Commands Used



```powershell

docker build -t flask-api:1.0 ".\\Exercise-4-Docker-Networking"



docker network create --driver bridge my-bridge-net

docker network ls

docker network inspect my-bridge-net



docker run -d --name mysql --network my-bridge-net -e MYSQL\_ROOT\_PASSWORD=DevOpsLab123! -e MYSQL\_DATABASE=labdb mysql:8.4

docker run -d --name redis --network my-bridge-net redis:7

docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api:1.0



curl.exe http://localhost:5001/about

docker network inspect my-bridge-net



docker exec flask python -c "import socket; print('mysql:', socket.gethostbyname('mysql')); print('redis:', socket.gethostbyname('redis'))"

```



\## Results



\- The custom bridge network was created successfully.

\- All three containers were running and connected to the network.

\- The Flask API returned the expected JSON response.

\- Docker's internal DNS resolved `mysql` to `172.18.0.2` and `redis` to `172.18.0.3`.

\- Flask was accessible from the host through port 5001.



\## Lab Questions and Answers



\### 1. What is the purpose of the `--net` flag in `docker run`?

It specifies the Docker network to which the container should connect. The equivalent modern option is `--network`.



\### 2. How do containers communicate with each other on the same network?

Containers on a user-defined bridge network can communicate using container names or IP addresses. Docker's internal DNS resolves container names.



\### 3. What is the difference between a bridge network and a host network?

\- \*\*Bridge network:\*\* Containers communicate through an isolated virtual network.

\- \*\*Host network:\*\* The container shares the host's network namespace, without the usual separate container IP and port mapping.



\### 4. How can you expose a container's port to the host machine?

Use the `-p` option. For example, `-p 5001:5001` maps host port 5001 to container port 5001.



\## Screenshots



1\. `screenshots/01-bridge-network.png` — Bridge network listing.

2\. `screenshots/02-network-inspect.png` — Network configuration.

3\. `screenshots/03-flask-api.png` — Flask API response.

4\. `screenshots/04-connected-containers.png` — All three containers attached to the network.

5\. `screenshots/05-dns-connectivity.png` — Container-name resolution test.



\## Conclusion

The exercise demonstrates how to create a custom Docker bridge network, run multiple containers on it, expose a Flask API port, and verify container communication through Docker's internal DNS.



