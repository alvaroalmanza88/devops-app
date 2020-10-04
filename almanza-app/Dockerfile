#docker run -d --hostname almanza-app --name almanza-app -p 8080:8080 --env RABBITMQ=172.17.0.2 almanza-app
FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT [ "python", "./almanza-app.py" ]
