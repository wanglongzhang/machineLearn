#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restplus import Resource, fields
from controller.baseController import api
from middleware import api_key_required
from dal.RolePermissionDao import RolePermissionDAO

rolepermissionModel = api.model("rolepermission", {
    "name": fields.String(required=True, description="The rolepermission name"),
    "description": fields.String(description="The rolepermission desc"),
    "status": fields.Integer(description="The rolepermission status")
})

rolepermissionDao = RolePermissionDAO()


ns_rolepermission = api.namespace("rolepermission", description="rolepermissionController")

@ns_rolepermission.route("/")
@api.header("Authentication", "authentication header", required=True)
class RolePermissionList(Resource):
    @api_key_required("rolepermission:readonly")
    def get(self):
        """List all tasks"""
        # import pdb; pdb.set_trace()
        return rolepermissionDao.get_all_entry()


    @ns_rolepermission.expect(rolepermissionModel)
    @api_key_required("rolepermission:readwrite")
    def post(self):
        """Create a new task"""
        return rolepermissionDao.create(api.payload), 201


@ns_rolepermission.route("/<int:id>")
@ns_rolepermission.response(404, "RolePermission not found")
@ns_rolepermission.param("id", "The task identifier")
@api.header("Authentication", "authentication header", required=True)
class RolePermission(Resource):
    @api_key_required("rolepermission:readonly")
    def get(self, id):
        """Fetch a given resource"""
        tmp = rolepermissionDao.get_one_entry(id)
        return tmp

    @ns_rolepermission.response(204, "RolePermission deleted")
    @api_key_required("rolepermission:readwrite")
    def delete(self, id):
        """Delete a task given its identifier"""
        rolepermissionDao.delete(id)
        return "", 204

    @ns_rolepermission.expect(rolepermissionModel)
    @api_key_required("rolepermission:readwrite")
    def put(self, id):
        """Update a task given its identifier"""
        return rolepermissionDao.update(id, api.payload)