import datetime
import mysql.connector
import logging

from mysql.connector import errorcode

logger = logging.getLogger(__name__)

class mysqlDrv:    

    def __init__(self, userName, password, host, db):
       
        self.uName = userName
        self.passwd = password
        self.host = host
        self.db = db
        self.result = ''
        self.cnx = mysql.connector.connect(user = self.uName, password = self.passwd , host = self.host, database = self.db)
        self.cnx.close()

        logging.debug(f"SQLDRV: init done")

    def conDB(self):
        
        logging.debug(f"SQLDRV: Creating Connection")
        try:
            self.cnx = mysql.connector.connect(user = self.uName, password = self.passwd , host = self.host, database = self.db)
            logging.debug(f"SQLDRV: Connection Created")
        except mysql.connector.Error as err:
            logging.debug(f"SQLDRV: Error: {err}")
        

    def sqlCmd(self, sql):

        logging.debug(f"SQLDRV: Starting sqlCmd Function")
        logging.debug(f"SQLDRV: sqlStr: {sql}")

        try:
            self.conDB()        
            cursor = self.cnx.cursor()
            cursor.execute(sql)
            self.cnx.commit()
            self.cnx.close()
            logging.debug(f"SQLDRV: sqlCmd Function Completed : 'Success'")
            return "Success"
        except mysql.connector.Error as err:
            logging.debug(f"SQLDRV: Error: {err}")
            return "Failed"

    def sqlFetchAll(self, sql):

        logging.debug(f"SQLDRV: Starting sqlFetchAll Function")
        logging.debug(f"SQLDRV: sqlStr: {sql}")

        try:
            self.conDB()        
            cursor = self.cnx.cursor(dictionary=True)
            cursor.execute(sql)
            sqlResult =  cursor.fetchall()
            self.cnx.close()

            ResultPrint = [dict(r) for r in sqlResult]

            logging.debug(f"SQLDRV: sqlFetchAll Function Completed : 'Success'")
            logging.debug(f"SQLDRV: {ResultPrint}")

            return ResultPrint

        except mysql.connector.Error as err:
            logging.debug(f"SQLDRV: Error: {err}")
            return "Error"
        

