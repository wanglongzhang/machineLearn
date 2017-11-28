#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restplus import Resource, fields
from controller.baseController import api
from middleware import api_key_required
from dal.UserDao import UserDAO

userModel = api.model("user", {
    "name": fields.String(required=True, description="The user name"),
    "description": fields.String(description="The user desc"),
    "status": fields.Integer(description="The user status")
})

userDao = UserDAO()


ns_user = api.namespace("user", description="userController")

@ns_user.route("/")
@api.header("Authentication", "authentication header", required=True)
class UserList(Resource):
    @api_key_required("user:readonly")
    def get(self):
        """List all tasks"""
        # import pdb; pdb.set_trace()
        return userDao.get_all_entry()


    @ns_user.expect(userModel)
    @api_key_required("user:readwrite")
    def post(self):
        """Create a new task"""
        return userDao.create(api.payload), 201


@ns_user.route("/<int:id>")
@ns_user.response(404, "User not found")
@ns_user.param("id", "The task identifier")
@api.header("Authentication", "authentication header", required=True)
class User(Resource):
    @api_key_required("user:readonly")
    def get(self, id):
        """Fetch a given resource"""
        tmp = userDao.get_one_entry(id)
        return tmp

    @ns_user.response(204, "User deleted")
    @api_key_required("user:readwrite")
    def delete(self, id):
        """Delete a task given its identifier"""
        userDao.delete(id)
        return "", 204

    @ns_user.expect(userModel)
    @api_key_required("user:readwrite")
    def put(self, id):
        """Update a task given its identifier"""
        return userDao.update(id, api.payload)