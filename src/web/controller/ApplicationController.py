#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restplus import Resource, fields
from controller.baseController import api
from middleware import api_key_required
from dal.ApplicationDao import ApplicationDAO

applicationModel = api.model("App", {
    "name": fields.String(required=True, description="The application name"),
    "description": fields.String(description="The application desc"),
    "status": fields.Integer(description="The application status")
})

applicationDao = ApplicationDAO()


ns_application = api.namespace("application", description="applicationController")

@ns_application.route("/")
@api.header("Authentication", "authentication header", required=True)
class ApplicationList(Resource):
    @api_key_required("application:readonly")
    def get(self):
        """List all tasks"""
        # import pdb; pdb.set_trace()
        return applicationDao.get_all_entry()


    @ns_application.expect(applicationModel)
    @api_key_required("application:readwrite")
    def post(self):
        """Create a new task"""
        return applicationDao.create(api.payload), 201


@ns_application.route("/<int:id>")
@ns_application.response(404, "Application not found")
@ns_application.param("id", "The task identifier")
@api.header("Authentication", "authentication header", required=True)
class Application(Resource):
    @api_key_required("application:readonly")
    def get(self, id):
        """Fetch a given resource"""
        tmp = applicationDao.get_one_entry(id)
        return tmp

    @ns_application.response(204, "Application deleted")
    @api_key_required("application:readwrite")
    def delete(self, id):
        """Delete a task given its identifier"""
        applicationDao.delete(id)
        return "", 204

    @ns_application.expect(applicationModel)
    @api_key_required("application:readwrite")
    def put(self, id):
        """Update a task given its identifier"""
        return applicationDao.update(id, api.payload)