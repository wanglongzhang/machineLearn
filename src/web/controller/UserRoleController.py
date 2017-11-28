#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restplus import Resource, fields
from controller.baseController import api
from middleware import api_key_required
from dal.UserRoleDao import UserRoleDAO

userroleModel = api.model("userrole", {
    "name": fields.String(required=True, description="The userrole name"),
    "description": fields.String(description="The userrole desc"),
    "status": fields.Integer(description="The userrole status")
})

userroleDao = UserRoleDAO()


ns_userrole = api.namespace("userrole", description="userroleController")

@ns_userrole.route("/")
@api.header("Authentication", "authentication header", required=True)
class UserRoleList(Resource):
    @api_key_required("userrole:readonly")
    def get(self):
        """List all tasks"""
        # import pdb; pdb.set_trace()
        return userroleDao.get_all_entry()


    @ns_userrole.expect(userroleModel)
    @api_key_required("userrole:readwrite")
    def post(self):
        """Create a new task"""
        return userroleDao.create(api.payload), 201


@ns_userrole.route("/<int:id>")
@ns_userrole.response(404, "UserRole not found")
@ns_userrole.param("id", "The task identifier")
@api.header("Authentication", "authentication header", required=True)
class UserRole(Resource):
    @api_key_required("userrole:readonly")
    def get(self, id):
        """Fetch a given resource"""
        tmp = userroleDao.get_one_entry(id)
        return tmp

    @ns_userrole.response(204, "UserRole deleted")
    @api_key_required("userrole:readwrite")
    def delete(self, id):
        """Delete a task given its identifier"""
        userroleDao.delete(id)
        return "", 204

    @ns_userrole.expect(userroleModel)
    @api_key_required("userrole:readwrite")
    def put(self, id):
        """Update a task given its identifier"""
        return userroleDao.update(id, api.payload)