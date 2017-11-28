#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import request
from controller.baseController import api
from util.transactionLogger import update_user_context, user_context


def api_key_required(permission, type="permission"):
    def deco(func):
        def func_wrapper(*args, **kwargs):
            api_key = request.headers.get("Authentication")
            if api_key != permission:
                return api.abort(403)
            return func(*args, **kwargs)
        setattr(func_wrapper, "__doc__", func.__doc__)
        return func_wrapper
    return deco

def auth_required(func):
    def func_wrapper(*args, **kwargs):
        api_key = request.headers.get("Authorization")
        if api_key:
            try:
                identity = authenticate_user(api_key)
                if user_context() != identity.id:
                    logger.warning("Mismatched user context. PreAuth=[{}], PostAuth=[{}]".format(user_context(), identity.id))
                    update_user_context(identity.id)
                identity_changed.send(app, identity=identity)
                return func(*args, **kwargs)
            except InvalidAuthKey:
                return Response("Invalid auth key", 401)
        return Response("An api key is required", 401)
    return func_wrapper