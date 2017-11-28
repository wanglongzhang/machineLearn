#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, request, g
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api
import json
import datetime
import time
import jwt
import traceback
import logging
import dateutil

from util.logger import logger
from util.transactionLogger import new_transaction


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:111111@10.108.92.136:3306/service_profile"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)
Base = db.Model
Base.to_dict = lambda x: {c.name: getattr(x, c.name, None) for c in x.__table__.columns}


class CustomizedJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, str):
            return obj
        elif isinstance(obj, Base):
            return obj.to_dict()
        else:
            return json.JSONEncoder.default(self, obj)

app.config["RESTPLUS_JSON"] = {"cls": CustomizedJsonEncoder}


api = Api(app, version="1.0", title="Distributed Configuration Management API",
          description="")


def pre_auth_username(request):
    """
    Used only during first time user evaluation for new API requests. In other cases use user_context()
    """
    api_key = request.headers.get("Authentication")
    if api_key is None:
        return request.remote_addr
    try:
        identity = jwt.decode(api_key, verify=False)
        return identity['user']
    except (jwt.exceptions.DecodeError, KeyError):
        return request.remote_addr


@app.before_request
def received_new_request():
    g.start = time.time()
    username = pre_auth_username(request)
    new_transaction(user_id=username)
    request_data = ['Url={}'.format(request.url),
                    'Method={}'.format(request.method),
                    'Body={}'.format((str(request.json) or str(request.data))),
                    'Form={}'.format(str(request.form.to_dict())),
                    'Headers={}'.format({x[0]: x[1] for x in request.headers.items()})]
    logger.debug("Received a new request " + ", ".join(request_data))
    return


@app.after_request
def sending_response(response):
    #time.sleep(70)
    response_time = "%.2f" % (time.time() - g.start)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,PATCH')
    logger.debug("Response Code={} to URL={} URL_Rule={}, Elapsed={} second".format(response.status_code,
                                                                      request.path,
                                                                      request.url_rule,
                                                                      response_time))
    return response

@app.errorhandler(Exception)
def exceptions(e):
    ts = time.strftime('[%Y-%b-%d %H:%M]')
    tb = traceback.format_exc()
    logger.error('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s',
                  ts,
                  request.remote_addr,
                  request.method,
                  request.scheme,
                  request.full_path,
                  tb)
    return "Internal Server Error", 500


from controller.appController import ns_app
from controller.authController import ns_auth

#api.add_namespace(ns_app)

