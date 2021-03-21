#! /usr/bin/python3

import sys
sys.path.append("..")
import os
import getpass
import datetime
import yaml
import cherrypy
import time as t

os.chdir(os.path.dirname(__file__))

from mysqldrv import *
from logSetup import *
from httpservice import *

configs = {}

with open(f'../config/http-service-conf.yaml') as fp:
    configs = yaml.load(fp, Loader=yaml.FullLoader)

#Project Info
projectName = configs["projectName"]

#logfiles informations
logFilename = configs["filename"]
logLevel = configs["level"]
dateTime = datetime.datetime.now()

#dataBase informations
userName = configs["dbuserName"]
password = str(configs["dbpassword"])
db_host = configs["dbhost"]
db_port = configs["dbport"]
db = configs["dbname"]

#Http details
httpHost = configs["chpHost"]
httpPort = configs["chpPort"]

#SetupLogging

t.sleep(5)

loggerSetup = logSetupClass(projectName, logFilename, logLevel)
logger = logging.getLogger(__name__)
logging.debug(f"initiate http-service now")
sqlDrv = mysqlDrv(userName, password, db_host, db_port, db)
logging.debug(f"initiate mysqlDriver now")
http = httpService(httpHost, httpPort, sqlDrv)

logging.debug(f"initiate CherryPy now")
cherrypy.engine.start()
cherrypy.engine.block()


