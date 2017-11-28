#!/usr/bin/python
# -*- coding: utf-8 -*-

from dal.BaseDao import BaseDAO
from model import Configuration


class ConfigurationDAO(BaseDAO):
    def __init__(self):
        super(ConfigurationDAO, self).__init__(Configuration)