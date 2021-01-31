import datetime
import mysql.connector
from mysql.connector import errorcode

class mysqlDrv:    

    def __init__(self, userName, password, host, db, logger):

        self.uName = userName
        self.passwd = password
        self.host = host
        self.db = db
        self.result = ''
        self.log = logger
        self.DateTimeNow = ''

        self.cnx = mysql.connector.connect(user = self.uName, password = self.passwd , host = self.host, database = self.db)
        self.cnx.close()

    def conDB(self):

        self.DateTimeNow = datetime.datetime.now()
        
        self.log.info(f'{self.DateTimeNow}:\tSQLDRV: Creating Connection')
        try:
            self.cnx = mysql.connector.connect(user = self.uName, password = self.passwd , host = self.host, database = self.db)
            self.log.info(f'{self.DateTimeNow}:\tSQLDRV: Connection Created')
        except mysql.connector.Error as err:
            self.log.info(f'{self.DateTimeNow}:\tSQLDRV: Error: {err}')
        

    def sqlCmd(self, sql):

        self.DateTimeNow = datetime.datetime.now()

        self.log.info(f'{self.DateTimeNow}:\tSQLDRV: Starting sqlCmd Function')
        self.log.info(f'\n{self.DateTimeNow}:\tSQLDRV: sqlStr: {sql}\n')

        try:
            self.conDB()        
            cursor = self.cnx.cursor()
            cursor.execute(sql)
            self.cnx.commit()
            self.cnx.close()
            self.log.info(f'{self.DateTimeNow}:\tSQLDRV: sqlCmd Function Completed : "Success"\n')
            return "Success"
        except mysql.connector.Error as err:
            self.log.info(f'\n{self.DateTimeNow}:\tSQLDRV: Error: {err}\n')
            return "Failed"

    def sqlFetchAll(self, sql):

        self.DateTimeNow = datetime.datetime.now()

        self.log.info(f'{self.DateTimeNow}:\tSQLDRV: Starting sqlFetchAll Function')
        self.log.info(f'\n{self.DateTimeNow}:\tSQLDRV: sqlStr: {sql}\n')

        try:
            self.conDB()        
            cursor = self.cnx.cursor(dictionary=True)
            cursor.execute(sql)
            sqlResult =  cursor.fetchall()
            #self.cnx.commit()
            self.cnx.close()

            ResultPrint = [dict(r) for r in sqlResult]
            
            self.log.info(f'{self.DateTimeNow}:\tSQLDRV: sqlFetchAll Function Completed : "Success"\n')
            #self.log.info(f"\n{self.DateTimeNow}:\tSQLDRV: {ResultPrint}\n")

            return ResultPrint

        except mysql.connector.Error as err:
            self.log.info(f'{self.DateTimeNow}:\tSQLDRV: Error: {err}')
            return "Error"
        

