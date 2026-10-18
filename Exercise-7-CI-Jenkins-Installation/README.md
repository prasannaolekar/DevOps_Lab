# Exercise 7: Introduction to Continuous Integration (CI) and Jenkins Installation



## 1. Objective



To understand Continuous Integration (CI), its benefits and workflow, explore CI/CD tools, and verify Jenkins installation using Docker.



## 2. What is Continuous Integration (CI)?



Continuous Integration is a software development practice in which developers frequently integrate code changes into a shared repository. Automated builds and tests help identify errors early and improve software quality.



## 3. Key Features of CI



1\. **Frequent Code Integration:** Developers regularly commit changes to a shared repository.

2\. **Automated Builds:** Builds verify incoming code changes.

3\. **Automated Testing:** Tests check whether functionality continues to work.

4\. **Immediate Feedback:** Build and test results help developers fix issues promptly.



## 4. Benefits of CI



\- **Early Bug Detection:** Identifies integration issues early.

\- **Improved Collaboration:** Helps developers integrate code changes smoothly.

\- **Faster Development Cycles:** Automates repetitive build and testing tasks.

\- **Better Software Quality:** Automated testing helps prevent regressions.



## 5. How CI Works



1\. A developer writes code and pushes changes to a version control system.

2\. The CI server detects changes or receives a build trigger.

3\. The server builds the application and resolves dependencies.

4\. Automated tests validate the code.

5\. Results are reported to the development team.



## 6. CI/CD Tools



\- **GitLab CI/CD:** CI/CD integrated with GitLab repositories.

\- **CircleCI:** Cloud-based automation with container and parallel execution support.

\- **Travis CI:** CI service with configuration-based builds.

\- **Bamboo:** Atlassian CI/CD tool.

\- **TeamCity:** CI server from JetBrains.

\- **Azure Pipelines:** CI/CD service in Azure DevOps.

\- **GitHub Actions:** Repository-integrated workflow automation.

\- **Spinnaker:** Continuous delivery for cloud-native applications.

\- **Buildkite:** CI platform supporting self-hosted agents.

\- **Drone:** Container-oriented CI/CD platform.



## 7. Introduction to Jenkins



Jenkins is an open-source automation server used to automate software building, testing, and deployment tasks. It supports Continuous Integration and Continuous Delivery through pipelines and plugins.



### Why Jenkins?



\- Automates repetitive tasks.

\- Supports Continuous Integration.

\- Provides extensibility through plugins.

\- Supports distributed builds using agents.



### Key Jenkins Concepts



1\. **Job/Project:** A task configured in Jenkins.

2\. **Build:** An execution of a job or pipeline.

3\. **Pipeline:** A sequence of automated steps.

4\. **Plugins:** Extensions that add Jenkins functionality.

5\. **Nodes:** Machines that execute Jenkins workloads.



## 8. Jenkins Installation Using Docker



Jenkins is running in a Docker container using the `jenkins/jenkins:lts-jdk17` image.



### Check the running container



```powershell

docker ps

```



### Verify Java



```powershell

docker exec jenkins java -version

```



### Retrieve the initial administrator password, if required



```powershell

docker exec jenkins cat /var/jenkins\_home/secrets/initialAdminPassword

```



### Access Jenkins



Open this URL in your browser:



http://localhost:8080



The Jenkins dashboard was successfully accessed using the existing installation.



> **Note:** The existing Jenkins container and persistent configuration are reused from Exercise 6. Do not create a duplicate container or delete the existing Jenkins volume.



## 9. Installation Screenshot



The `screenshots` directory contains the Jenkins dashboard screenshot.



!\[Jenkins Dashboard](screenshots/jenkins-dashboard.png)



## 10. Result



Studied Continuous Integration concepts, benefits, workflow, and common CI/CD tools. Verified the existing Jenkins installation, Java runtime, Docker container, and Jenkins dashboard.






