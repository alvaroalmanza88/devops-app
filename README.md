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

Execute the container mounting the prepared jenkins_home on this repo on the jenkins_home of the container, mount in /var/code, the ansible code and expose de ports 8080 and 50000 as is shown un the code above:

```docker run -itd --name jenkins-sword -p 8080:8080 -p 50000:50000 -v $HOME/repos/devops-app/jenkins_home:/var/jenkins_home -v $HOME/repos/devops-app/ansible:/var/code alvaroalmanza/jenkins-sword:v1```


Once the container is mounted can access using localhost:8080 without any pass. there will be some pipeline prepared:



