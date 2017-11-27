#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import request
from controller.baseController import api


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