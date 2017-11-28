#!/usr/bin/python
# -*- coding: utf-8 -*-

from dal.BaseDao import BaseDAO
from model import Role


class RoleDAO(BaseDAO):
    def __init__(self):
        super(RoleDAO, self).__init__(Role)