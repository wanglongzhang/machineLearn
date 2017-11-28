#!/usr/bin/python
# -*- coding: utf-8 -*-

from dal.BaseDao import BaseDAO
from model import Permission


class PermissionDAO(BaseDAO):
    def __init__(self):
        super(PermissionDAO, self).__init__(Permission)