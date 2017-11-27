#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restplus import Api, Resource, fields
from controller.baseController import api
from middleware import api_key_required
from dal.appDao import AppDAO

app = api.model("Todo", {
    "name": fields.String(required=True, description="The app name"),
    "description": fields.String(description="The app desc"),
    "status": fields.Integer(description="The app status")
})

appDao = AppDAO()


ns_app = api.namespace("app", description="app operations")

@ns_app.route("/")
@api.header("Authentication", "authentication header", required=True)
class AppList(Resource):

    @api_key_required("todolist:get")
    def get(self):
        """List all tasks"""
        # import pdb; pdb.set_trace()
        return appDao.get_all_entry()


    @ns_app.expect(app)
    @api_key_required("todolist:create")
    #@ns_app.doc("create app")
    def post(self):
        """Create a new task"""
        return appDao.create(api.payload), 201


@ns_app.route("/<int:id>")
@ns_app.response(404, "Todo not found")
@ns_app.param("id", "The task identifier")
@api.header("Authentication", "authentication header", required=True)
class App(Resource):
    #@ns_app.doc("get app")
    def get(self, id):
        """Fetch a given resource"""
        tmp = appDao.get_one_entry(id)
        #import pdb; pdb.set_trace()
        return tmp

    #@ns_app.doc("delete app")
    @ns_app.response(204, "Todo deleted")
    def delete(self, id):
        """Delete a task given its identifier"""
        appDao.delete(id)
        return "", 204

    #@ns_app.doc("update app")
    @ns_app.expect(app)
    def put(self, id):
        """Update a task given its identifier"""
        return appDao.update(id, api.payload)