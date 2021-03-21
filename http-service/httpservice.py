import json
import datetime
import logging

import sys
import os
import base64

import cherrypy

from flask import Flask, jsonify, request
from flask_cors import CORS

logger = logging.getLogger(__name__)

class httpService:

    def __init__(self, host, port, dataservice):        

        self.host = host
        self.port = port      
        self.dataService = dataservice

        self.web_app = Flask(__name__)
        self.cors = CORS(self.web_app)
        self.web_app.config["PROPAGATE_EXCEPTIONS"] = True

        cherrypy.tree.graft(self.web_app.wsgi_app, "/")

        cherrypy.config.update({
            "server.socket_host": host,
            "server.socket_port": port,
            "server.thread_pool": 5,
            "engine.autoreload.on": False,
            "tools.gzip.on": True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'application/json'), ('Access-Control-Allow-Origin', f'http://{host}')]
        })

        self.web_app.add_url_rule("/angularBase/services/runGetTest", "runGetTest",
                                  self.runGetTest, methods=["GET"])
        self.web_app.add_url_rule("/angularBase/services/runPostTest", "runPostTest",
                                  self.runPostTest, methods=["POST"])
        self.web_app.add_url_rule("/angularBase/services/runDB_Write", "runDB_Write",
                                  self.runDB_Write, methods=["GET"])
        self.web_app.add_url_rule("/angularBase/services/runDB_Read", "runDB_Read",
                                  self.runDB_Read, methods=["GET"])

        
        logging.debug(f"REST: init done")

    def runGetTest(self):

        logging.debug(f"REST: => runGetTest()")

        return jsonify(result="runGetTest"), 200

    def runPostTest(self):
    
        logging.debug(f"REST: => runPostTest()")

        data = json.loads(request.data)

        result = data["TestMsg"]

        return jsonify(result=result), 200

    def runDB_Write(self):
    
        logging.debug(f"REST: => runDB_Write()12345")

        sql = "insert into new_table (value) values('TestName')"

        self.dataService.sqlCmd(sql)

        return jsonify(result="runDB_Write => Done!!!"), 200

    def runDB_Read(self):

        logging.debug(f"REST: => runDB_Read()")

        sql = "SELECT * FROM angularBase.new_table"

        result = self.dataService.sqlFetchAll(sql)

        return jsonify(result=result), 200
        
    