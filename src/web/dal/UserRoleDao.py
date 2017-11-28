#!/usr/bin/python
# -*- coding: utf-8 -*-

from dal.BaseDao import BaseDAO
from model import UserRole


class UserRoleDAO(BaseDAO):
    def __init__(self):
        super(UserRoleDAO, self).__init__(UserRole)