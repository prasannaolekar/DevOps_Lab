

\# Exercise 6: Real-Time Operations Monitoring and Alerting



\## Objective

Build a real-time delivery monitoring system using Prometheus, Grafana, Python, and Jenkins.



\## Technologies Used

\- Python

\- Prometheus

\- Grafana

\- Jenkins

\- Docker



\## Project Components



\### 1. Python Metrics Exporter

The `delivery\_metrics.py` application exposes delivery metrics on port 8000 using the Prometheus client library.



Metrics include:

\- Total deliveries

\- Pending deliveries

\- On-the-way deliveries

\- Average delivery time



\### 2. Prometheus Monitoring

The `prometheus.yml` file configures Prometheus to scrape the delivery service metrics and its own metrics.



The `alert\_rules.yml` file defines:

\- \*\*HighPendingDeliveries:\*\* Triggers when pending deliveries exceed 10 for 15 seconds.

\- \*\*HighAverageDeliveryTime:\*\* Triggers when average delivery time exceeds 30 seconds for 15 seconds.



\### 3. Grafana Dashboard

The `ZAPPTTO Delivery Monitoring` dashboard visualizes the four delivery metrics using Grafana connected to Prometheus.



\### 4. Jenkins Pipeline

The `Delivery-Monitoring-Pipeline` validates the monitoring configuration files and checks Prometheus health.



The successful pipeline execution is recorded in Jenkins build #5.



\## Screenshots

Screenshots are available in the `screenshots/` directory:

\- `jenkins-success.png`

\- `grafana-dashboard.png`

\- `prometheus-alerts.png`

\- `prometheus-alert-details.png`



\## Result

Successfully configured Python metrics collection, Prometheus monitoring and alert rules, Grafana visualization, and a Jenkins pipeline that completed successfully.



