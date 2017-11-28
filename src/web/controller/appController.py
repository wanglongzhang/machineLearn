#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restplus import Resource, fields
from controller.baseController import api
from middleware import api_key_required
from dal.appDao import AppDAO

appModel = api.model("App", {
    "name": fields.String(required=True, description="The app name"),
    "description": fields.String(description="The app desc"),
    "status": fields.Integer(description="The app status")
})

appDao = AppDAO()


ns_app = api.namespace("app", description="appController")

@ns_app.route("/")
@api.header("Authentication", "authentication header", required=True)
class AppList(Resource):
    @api_key_required("app:readonly")
    def get(self):
        """List all tasks"""
        # import pdb; pdb.set_trace()
        return appDao.get_all_entry()


    @ns_app.expect(appModel)
    @api_key_required("app:readwrite")
    def post(self):
        """Create a new task"""
        return appDao.create(api.payload), 201


@ns_app.route("/<int:id>")
@ns_app.response(404, "App not found")
@ns_app.param("id", "The task identifier")
@api.header("Authentication", "authentication header", required=True)
class App(Resource):
    @api_key_required("app:readonly")
    def get(self, id):
        """Fetch a given resource"""
        tmp = appDao.get_one_entry(id)
        return tmp

    @ns_app.response(204, "App deleted")
    @api_key_required("app:readwrite")
    def delete(self, id):
        """Delete a task given its identifier"""
        appDao.delete(id)
        return "", 204

    @ns_app.expect(appModel)
    @api_key_required("app:readwrite")
    def put(self, id):
        """Update a task given its identifier"""
        return appDao.update(id, api.payload)