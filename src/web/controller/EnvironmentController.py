#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restplus import Resource, fields
from controller.baseController import api
from middleware import api_key_required
from dal.EnvironmentDao import EnvironmentDAO

environmentModel = api.model("environment", {
    "name": fields.String(required=True, description="The environment name"),
    "description": fields.String(description="The environment desc"),
    "status": fields.Integer(description="The environment status")
})

environmentDao = EnvironmentDAO()


ns_environment = api.namespace("environment", description="environmentController")

@ns_environment.route("/")
@api.header("Authentication", "authentication header", required=True)
class EnvironmentList(Resource):
    @api_key_required("environment:readonly")
    def get(self):
        """List all tasks"""
        # import pdb; pdb.set_trace()
        return environmentDao.get_all_entry()


    @ns_environment.expect(environmentModel)
    @api_key_required("environment:readwrite")
    def post(self):
        """Create a new task"""
        return environmentDao.create(api.payload), 201


@ns_environment.route("/<int:id>")
@ns_environment.response(404, "Environment not found")
@ns_environment.param("id", "The task identifier")
@api.header("Authentication", "authentication header", required=True)
class Environment(Resource):
    @api_key_required("environment:readonly")
    def get(self, id):
        """Fetch a given resource"""
        tmp = environmentDao.get_one_entry(id)
        return tmp

    @ns_environment.response(204, "Environment deleted")
    @api_key_required("environment:readwrite")
    def delete(self, id):
        """Delete a task given its identifier"""
        environmentDao.delete(id)
        return "", 204

    @ns_environment.expect(environmentModel)
    @api_key_required("environment:readwrite")
    def put(self, id):
        """Update a task given its identifier"""
        return environmentDao.update(id, api.payload)