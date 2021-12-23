FROM debian:buster

WORKDIR /app

ADD main.py /app
ADD requirements.txt /app
ADD templates/index.html /app/templates/index.html

RUN apt-get update -y
RUN apt-get install -y python3-dev python3-pip
RUN pip3 install -r requirements.txt

ENV FLASK_APP=main
ENV FLASK_ENV=development

EXPOSE 5000

ENTRYPOINT flask run -h 0.0.0.0 -p 5000