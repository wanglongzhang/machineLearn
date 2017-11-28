#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restplus import Resource, fields
from controller.baseController import api
from middleware import api_key_required
from dal.ConfigurationDao import ConfigurationDAO

configurationModel = api.model("configuration", {
    "name": fields.String(required=True, description="The configuration name"),
    "description": fields.String(description="The configuration desc"),
    "status": fields.Integer(description="The configuration status")
})

configurationDao = ConfigurationDAO()


ns_configuration = api.namespace("configuration", description="configurationController")

@ns_configuration.route("/")
@api.header("Authentication", "authentication header", required=True)
class ConfigurationList(Resource):
    @api_key_required("configuration:readonly")
    def get(self):
        """List all tasks"""
        # import pdb; pdb.set_trace()
        return configurationDao.get_all_entry()


    @ns_configuration.expect(configurationModel)
    @api_key_required("configuration:readwrite")
    def post(self):
        """Create a new task"""
        return configurationDao.create(api.payload), 201


@ns_configuration.route("/<int:id>")
@ns_configuration.response(404, "Configuration not found")
@ns_configuration.param("id", "The task identifier")
@api.header("Authentication", "authentication header", required=True)
class Configuration(Resource):
    @api_key_required("configuration:readonly")
    def get(self, id):
        """Fetch a given resource"""
        tmp = configurationDao.get_one_entry(id)
        return tmp

    @ns_configuration.response(204, "Configuration deleted")
    @api_key_required("configuration:readwrite")
    def delete(self, id):
        """Delete a task given its identifier"""
        configurationDao.delete(id)
        return "", 204

    @ns_configuration.expect(configurationModel)
    @api_key_required("configuration:readwrite")
    def put(self, id):
        """Update a task given its identifier"""
        return configurationDao.update(id, api.payload)