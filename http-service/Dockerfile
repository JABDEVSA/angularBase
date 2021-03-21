FROM ubuntu:20.10

RUN apt-get update && \
apt-get install python3 python3-pip python3-venv nano bash -y && \
apt-get install net-tools iputils-ping -y && \
apt-get clean

WORKDIR /app

COPY ./requirements.txt ./

RUN python3 -m pip install -r requirements.txt

COPY ./ ./

CMD ["./main/main.py"]

# import mysql.connector
# from mysql.connector import errorcode
# cnx = mysql.connector.connect(user = 'root', password = '5404271' , host = 'db', database = 'angularBase', port = 3306)