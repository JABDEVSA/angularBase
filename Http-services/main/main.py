#! /home/jab/.local/share/virtualenvs/Http-services-cA07RAHM/bin/python3

import sys
import os
import datetime
import yaml
import cherrypy

from http_services.mysqldrv import *
from http_services.logger import *
from http_services.httpservice import *

configs = {}
pwd = os.getcwd()
with open(f'{pwd}/config/hydroConf.yaml') as fp:
    configs = yaml.load(fp, Loader=yaml.FullLoader)

#logfiles informations
logFileLocation = configs["logFileLocation"]
infoLogFile = configs["infoLogFile"]
debuglogFile = configs["debuglogFile"]
dateTime = datetime.datetime.now()

#dataBase informations
userName = configs["dbuserName"]
password = str(configs["dbpassword"])
host = configs["dbhost"]
db = configs["dbname"]

#Http details
httpHost = configs["chpHost"]
httpPort = configs["chpPort"]

def checkLogFiles():

    try:               
        with open(f'{logFileLocation}{infoLogFile}', 'r') as fp:
            result = fp.read()
        
    except:                
        os.system(f'mkdir -p {logFileLocation}')

checkLogFiles()

log = logging(logFileLocation, infoLogFile, debuglogFile)
sqlDrv = mysqlDrv(userName, password, host, db, log)

http = httpService(httpHost, httpPort, log, sqlDrv)

log.info(f'{dateTime}\t------------------HydroClear api Starting-----------------')
log.debug(f'{dateTime}\t------------------HydroClear api Starting-----------------')

cherrypy.engine.start()
cherrypy.engine.block()


