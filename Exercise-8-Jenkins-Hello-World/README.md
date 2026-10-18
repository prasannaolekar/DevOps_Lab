# Exercise 8: Creating a Hello World Jenkins Job



## 1. Objective

To create and execute a Jenkins Freestyle job that runs a shell script and displays a message in the build console.



## 2. Script

File: `hello-world.sh`



```bash

#!/bin/bash

echo "Hello, Jenkins!"

```



## 3. Jenkins Job Configuration

\- **Job Name:** HelloWorld

\- **Job Type:** Freestyle project

\- **Source Code Management:** Git

\- **Repository:** https://github.com/prasannaolekar/DevOps\_Lab.git

\- **Branch:** `*/master`

\- **Build Step:** Execute shell



Build commands:



```bash

cd Exercise-8-Jenkins-Hello-World

sh hello-world.sh

```



## 4. Execution

The job was triggered manually using **Build Now**.



Expected console output:



```text

Hello, Jenkins!

Finished: SUCCESS

```



## 5. Screenshots



### GitHub Script

!\[GitHub Hello World Script](screenshots/github-hello-world.png)



### Jenkins Job Configuration

!\[Jenkins Job Configuration](screenshots/jenkins-job-configuration.png)



### Jenkins Console Output

!\[Jenkins Console Output](screenshots/jenkins-console-output.png)



## 6. Result

The HelloWorld Jenkins Freestyle job executed successfully and printed `Hello, Jenkins!` in the console output.


