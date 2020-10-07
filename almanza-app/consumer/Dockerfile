#docker run -d --hostname aalmanza-rabbit --name aalmanza-rabbit -p 5672:5672 rabbitmq
#docker run -d --hostname almanza-app --name almanza-app -p 8080:8080 --env RABBITMQ=172.17.0.2 almanza-app
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./consumer.py" ]
