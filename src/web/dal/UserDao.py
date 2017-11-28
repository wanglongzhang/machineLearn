#!/usr/bin/python
# -*- coding: utf-8 -*-

from dal.BaseDao import BaseDAO
from model import User


class UserDAO(BaseDAO):
    def __init__(self):
        super(UserDAO, self).__init__(User)