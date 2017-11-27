#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api, Resource, fields
import json
import datetime
import dateutil


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:111111@127.0.0.1:3306/service_profile"






db = SQLAlchemy(app)
Base = db.Model
Base.to_dict = lambda x: {c.name: getattr(x, c.name, None) for c in x.__table__.columns}

class CustomizedJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")
        elif isinstance(obj, basestring):
            return obj
        elif isinstance(obj, Base):
            return obj.to_dict()
        else:
            return json.JSONEncoder.default(self, obj)

app.config["RESTPLUS_JSON"] = {"cls": CustomizedJsonEncoder}

api = Api(app, version="1.0", title="TodoMVC API",
          description="A simple TodoMVC API"
          )

from controller.appController import ns_app

#api.add_namespace(ns_app)

