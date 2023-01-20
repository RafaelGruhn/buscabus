FROM python:3.7

LABEL maintainer="Rafael Müller Gruhn"

# definir variáveis ​​de ambiente 
ENV PYTHONDONTWRITEBYTECODE 1 
ENV PYTHONUNBUFFERED 1 

RUN apt-get update -y && \
    apt-get install -y python3-dev && \
    pip install -U pip && \
    apt-get install -y less build-essential \
    libxml2-dev libxmlsec1-dev libgraphviz-dev libaio1 \
    postgresql postgresql-contrib libpq-dev gcc

ARG MODE

COPY build/ /temp/
RUN /temp/build.sh

ADD . /code

WORKDIR /code/

# Django service
EXPOSE 8080
