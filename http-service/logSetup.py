
import os
import getpass
import logging
from logging.handlers import RotatingFileHandler

class logSetupClass:
    def __init__(self, projectName, logFilename, logLevel):

        whoami = getpass.getuser()

        logFilePath = f'/home/{whoami}/.var/logs/{projectName}/'
        logFileComplete = logFilePath + logFilename

        if not os.path.exists(logFilePath):
            os.system(f"mkdir -p {logFilePath}")

        logger = logging.getLogger()
        if logLevel == 'info':
            logger.setLevel(logging.INFO)
        if logLevel == 'debug':
            logger.setLevel(logging.DEBUG)

        rotHandel = RotatingFileHandler(logFileComplete, backupCount=5)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        rotHandel.setFormatter(formatter)
        logger.addHandler(rotHandel)
        rotHandel.doRollover()
        logging.debug(f"Logging Setup Done!")  