#!/usr/bin/python
# -*- coding: utf-8 -*-

from dal.BaseDao import BaseDAO
from model import RolePermission


class RolePermissionDAO(BaseDAO):
    def __init__(self):
        super(RolePermissionDAO, self).__init__(RolePermission)