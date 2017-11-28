#!/usr/bin/python
# -*- coding: utf-8 -*-

from dal.BaseDao import BaseDAO
from model import Application


class ApplicationDAO(BaseDAO):
    def __init__(self):
        super(ApplicationDAO, self).__init__(Application)
