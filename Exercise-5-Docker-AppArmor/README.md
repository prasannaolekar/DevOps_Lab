\# Exercise 5: Docker Security with AppArmor and Python



\## Objective

To build a Flask application in Docker, explore AppArmor security profiles, and use the Docker SDK for container inspection and security testing.



\## Files

\- `app.py` – Flask web application.

\- `Dockerfile` – Docker image configuration.

\- `flask-apparmor-profile` – AppArmor profile draft.

\- `docker\_security.py` – Inspects the Docker container and its reported profile.

\- `test\_restrictions.py` – Tests selected file and command operations.

\- `screenshots/` – Evidence of execution and testing.



\## Steps Performed

1\. Created a Flask application.

2\. Built the Docker image `flask-apparmor:1.0`.

3\. Started the container `flask-apparmor-test` on port 5002.

4\. Installed the Python Docker SDK.

5\. Used `docker\_security.py` to inspect the container.

6\. Used `test\_restrictions.py` to test selected operations.



\## Test Results

\- Container status: Running.

\- Custom AppArmor profile: Not reported.

\- Reading `/etc/shadow`: Succeeded.

\- Writing to `/var`: Succeeded.

\- Executing `/bin/ls`: Succeeded.



\*\*Limitation:\*\* AppArmor was not enabled in the Docker Desktop environment used for testing. Therefore, these results do not demonstrate AppArmor enforcement. The profile is a draft and requires validation on a Linux host with AppArmor enabled.



\## Questions and Answers



\### 1. What is AppArmor?

AppArmor is a Linux security module that restricts the capabilities of applications using security profiles.



\### 2. How does AppArmor improve Docker security?

It can restrict a container's access to files, capabilities, and system resources, reducing the impact of a compromised application.



\### 3. What happens when a container violates an AppArmor rule?

In enforcement mode, the kernel denies the restricted operation and may record an audit message.



\### 4. How can AppArmor profiles be customized?

Profiles can be written to define permitted and denied operations, then loaded and applied on a Linux system with AppArmor support.



\### 5. What are the limitations of AppArmor?

AppArmor depends on Linux kernel support and correct profile configuration. An overly restrictive profile can prevent an application from functioning, and a profile that is not loaded or enforced provides no intended protection.





