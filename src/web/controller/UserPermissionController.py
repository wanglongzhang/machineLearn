#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restplus import Resource, fields
from controller.baseController import api
from middleware import api_key_required
from dal.UserPermissionDao import UserPermissionDAO

userpermissionModel = api.model("userpermission", {
    "name": fields.String(required=True, description="The userpermission name"),
    "description": fields.String(description="The userpermission desc"),
    "status": fields.Integer(description="The userpermission status")
})

userpermissionDao = UserPermissionDAO()


ns_userpermission = api.namespace("userpermission", description="userpermissionController")

@ns_userpermission.route("/")
@api.header("Authentication", "authentication header", required=True)
class UserPermissionList(Resource):
    @api_key_required("userpermission:readonly")
    def get(self):
        """List all tasks"""
        # import pdb; pdb.set_trace()
        return userpermissionDao.get_all_entry()


    @ns_userpermission.expect(userpermissionModel)
    @api_key_required("userpermission:readwrite")
    def post(self):
        """Create a new task"""
        return userpermissionDao.create(api.payload), 201


@ns_userpermission.route("/<int:id>")
@ns_userpermission.response(404, "UserPermission not found")
@ns_userpermission.param("id", "The task identifier")
@api.header("Authentication", "authentication header", required=True)
class UserPermission(Resource):
    @api_key_required("userpermission:readonly")
    def get(self, id):
        """Fetch a given resource"""
        tmp = userpermissionDao.get_one_entry(id)
        return tmp

    @ns_userpermission.response(204, "UserPermission deleted")
    @api_key_required("userpermission:readwrite")
    def delete(self, id):
        """Delete a task given its identifier"""
        userpermissionDao.delete(id)
        return "", 204

    @ns_userpermission.expect(userpermissionModel)
    @api_key_required("userpermission:readwrite")
    def put(self, id):
        """Update a task given its identifier"""
        return userpermissionDao.update(id, api.payload)