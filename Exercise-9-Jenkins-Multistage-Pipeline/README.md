\# Exercise 9: Jenkins Multistage Pipeline



\## Objective

Build and test a Python Flask application using a Jenkins Declarative Pipeline with multiple stages.



\## Technologies Used

\- Jenkins

\- Docker

\- Python

\- Flask

\- pytest

\- Git and GitHub



\## Project Structure

```text

Exercise-9-Jenkins-Multistage-Pipeline/

├── Jenkinsfile

├── python-flask-app/

│   ├── app.py

│   ├── requirements.txt

│   └── test\_app.py

├── screenshots/

└── README.md

```



\## Pipeline Stages

The Jenkinsfile defines these stages:

1\. \*\*Build\*\* — prepares the Python application environment and installs dependencies.

2\. \*\*Test\*\* — executes application tests.

3\. \*\*Deploy\*\* — runs the pipeline's deployment step.

4\. \*\*Run Application\*\* — starts the Flask application.

5\. \*\*Test Application\*\* — checks the running application.



\## Jenkins Configuration

\- Pipeline type: Pipeline script from SCM

\- SCM: Git

\- Repository: `https://github.com/prasannaolekar/DevOps\_Lab.git`

\- Branch: `\*/master`

\- Script path: `Exercise-9-Jenkins-Multistage-Pipeline/Jenkinsfile`



\## Verification

Use the Jenkins build console to review each pipeline stage and its result. Screenshots are available in the `screenshots/` directory.



\*\*Note:\*\* A successful pipeline run should be confirmed in Jenkins. The README documents the pipeline configuration and stages; it does not by itself confirm a successful build.



