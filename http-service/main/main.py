#! /home/jab/projects/hydroclear/http-service/env/bin/python3

import sys
sys.path.append("..")
import os
import datetime
import yaml
import cherrypy

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

from mysqldrv import *
from logger import *
from httpservice import *

configs = {}
pwd = os.getcwd()
with open(f'../config/hydroConf.yaml') as fp:
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

print('!!!!!!!!!!!!!!!!!!!!{}:{}'.format(userName, password))

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


