#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging
import logging.config

from util.transactionLogger import TransactionLogger


logging.config.fileConfig(os.path.join(os.path.dirname(__file__), "..", "conf", 'log.conf'))
temp = logging.getLogger('web.server')
logger = TransactionLogger(temp)
del logging
del os