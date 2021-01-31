import json
import datetime

import sys
import os
import base64

import cherrypy

from flask import Flask, jsonify, request
from flask_cors import CORS

class httpService:

    def __init__(self, host, port, logging, dataservice):
        self.host = host
        self.port = port
        self.log = logging        
        self.dataService = dataservice
        self.DateTimeNow = ''

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

        self.web_app.add_url_rule("/hydroclear/services/runGetTest", "runGetTest",
                                  self.runGetTest, methods=["GET"])
        self.web_app.add_url_rule("/hydroclear/services/runPostTest", "runPostTest",
                                  self.runPostTest, methods=["POST"])

    def runGetTest(self):

        self.DateTimeNow = datetime.datetime.now()
        self.log.info(f'{self.DateTimeNow}:\tRunning runGetTest()')

        return jsonify(result="runGetTest"), 200

    def runPostTest(self):
    
        self.DateTimeNow = datetime.datetime.now()
        self.log.info(f'{self.DateTimeNow}:\tRunning runPostTest()')

        data = json.loads(request.data)

        result = data["TestMsg"]

        return jsonify(result=result), 200
        
    