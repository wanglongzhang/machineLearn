#!/usr/bin/python
# -*- coding: utf-8 -*-

from dal.BaseDao import BaseDAO
from model import Environment


class EnvironmentDAO(BaseDAO):
    def __init__(self):
        super(EnvironmentDAO, self).__init__(Environment)