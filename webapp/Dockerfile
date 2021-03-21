FROM ubuntu:18.04

RUN apt-get update && \
apt-get install python3 python3-pip nano bash -y &&\
apt-get clean



RUN python3 -m pip install virtualenv 

WORKDIR /app

COPY ./ ./