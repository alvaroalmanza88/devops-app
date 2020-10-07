# devops-app

This project pretends to show how to deploy and application using :

1. AWS as a Infraestructure provider
2. EKS / K8S Service as orchestrator
3. Python application to insert messages in a rabbitmq


## How to execute the project

Download from Docker hub the Jekins-word:

```docker pull alvaroalmanza/jenkins-sword:v1```

This container is an image of Jenkins with pre-install software:

1. python3
2. aws cli V2
3. ansible
4. kubectl

Execute the container mounting the aws, the code:

```docker run --name jenkins-sword -p 8080:8080 -p 50000:50000 -v $HOME/repos/jenkins-home:/var/jenkins_home jenkins/jenkins```


