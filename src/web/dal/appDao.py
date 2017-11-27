#!/usr/bin/python
# -*- coding: utf-8 -*-

from dal.baseDao import BaseDAO
from model import App


class AppDAO(BaseDAO):
    def __init__(self):
        super(AppDAO, self).__init__(App)