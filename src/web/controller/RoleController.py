#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restplus import Resource, fields
from controller.baseController import api
from middleware import api_key_required
from dal.RoleDao import RoleDAO

roleModel = api.model("role", {
    "name": fields.String(required=True, description="The role name"),
    "description": fields.String(description="The role desc"),
    "status": fields.Integer(description="The role status")
})

roleDao = RoleDAO()


ns_role = api.namespace("role", description="roleController")

@ns_role.route("/")
@api.header("Authentication", "authentication header", required=True)
class RoleList(Resource):
    @api_key_required("role:readonly")
    def get(self):
        """List all tasks"""
        # import pdb; pdb.set_trace()
        return roleDao.get_all_entry()


    @ns_role.expect(roleModel)
    @api_key_required("role:readwrite")
    def post(self):
        """Create a new task"""
        return roleDao.create(api.payload), 201


@ns_role.route("/<int:id>")
@ns_role.response(404, "Role not found")
@ns_role.param("id", "The task identifier")
@api.header("Authentication", "authentication header", required=True)
class Role(Resource):
    @api_key_required("role:readonly")
    def get(self, id):
        """Fetch a given resource"""
        tmp = roleDao.get_one_entry(id)
        return tmp

    @ns_role.response(204, "Role deleted")
    @api_key_required("role:readwrite")
    def delete(self, id):
        """Delete a task given its identifier"""
        roleDao.delete(id)
        return "", 204

    @ns_role.expect(roleModel)
    @api_key_required("role:readwrite")
    def put(self, id):
        """Update a task given its identifier"""
        return roleDao.update(id, api.payload)