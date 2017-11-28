#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restplus import Resource, fields
from controller.baseController import api
from middleware import api_key_required
from dal.PermissionDao import PermissionDAO

permissionModel = api.model("permission", {
    "name": fields.String(required=True, description="The permission name"),
    "description": fields.String(description="The permission desc"),
    "status": fields.Integer(description="The permission status")
})

permissionDao = PermissionDAO()


ns_permission = api.namespace("permission", description="permissionController")

@ns_permission.route("/")
@api.header("Authentication", "authentication header", required=True)
class PermissionList(Resource):
    @api_key_required("permission:readonly")
    def get(self):
        """List all tasks"""
        # import pdb; pdb.set_trace()
        return permissionDao.get_all_entry()


    @ns_permission.expect(permissionModel)
    @api_key_required("permission:readwrite")
    def post(self):
        """Create a new task"""
        return permissionDao.create(api.payload), 201


@ns_permission.route("/<int:id>")
@ns_permission.response(404, "Permission not found")
@ns_permission.param("id", "The task identifier")
@api.header("Authentication", "authentication header", required=True)
class Permission(Resource):
    @api_key_required("permission:readonly")
    def get(self, id):
        """Fetch a given resource"""
        tmp = permissionDao.get_one_entry(id)
        return tmp

    @ns_permission.response(204, "Permission deleted")
    @api_key_required("permission:readwrite")
    def delete(self, id):
        """Delete a task given its identifier"""
        permissionDao.delete(id)
        return "", 204

    @ns_permission.expect(permissionModel)
    @api_key_required("permission:readwrite")
    def put(self, id):
        """Update a task given its identifier"""
        return permissionDao.update(id, api.payload)