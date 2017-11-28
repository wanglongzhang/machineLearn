#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restplus import Resource, fields
from controller.baseController import api
from util.jwtHelper import generate_token, decode_token

encodeModel = api.model("AuthEncode", {
    "username": fields.String(required=True, description="username"),
    "password": fields.String(required=True, description="password"),
    "remember": fields.Boolean(required=True, description="rememberme")
})

decodeModel = api.model("AuthDecode", {
    "token": fields.String(required=True, description="token")
})

ns_auth = api.namespace("auth", description="authController")


@ns_auth.route("/")
class AuthEncode(Resource):

    @ns_auth.expect(encodeModel)
    def post(self):
        """generate auth key from payload"""
        # import pdb; pdb.set_trace()
        return generate_token(api.payload)


@ns_auth.route("/decode")
class AuthDecode(Resource):
    @ns_auth.expect(decodeModel)
    def post(self):
        """decode token"""
        header, claims = decode_token(api.payload["token"])
        claims.pop("password")
        claims.pop("remember")
        print(header, claims)
        return claims