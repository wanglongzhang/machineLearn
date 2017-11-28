#!/usr/bin/python
# -*- coding: utf-8 -*-

from dal.BaseDao import BaseDAO
from model import UserPermission


class UserPermissionDAO(BaseDAO):
    def __init__(self):
        super(UserPermissionDAO, self).__init__(UserPermission)