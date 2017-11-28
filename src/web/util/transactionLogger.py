#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
import logging
import threading
from uuid import uuid4


THREAD_LOCAL = threading.local()
TRANSACTION_KEY = 'transaction_id'
USERCONTEXT_KEY = 'user_context'


LoggerInfo = namedtuple('LoggerInfo', ['user_id', 'transaction_id'])


def new_transaction(user_id=None, transaction_id=None):
    set_thread_local(USERCONTEXT_KEY, user_id)
    set_thread_local(TRANSACTION_KEY, transaction_id)


def update_user_context(set_value=None):
    set_thread_local(USERCONTEXT_KEY, set_value)


def transaction_id():
    return str(get_thread_local(TRANSACTION_KEY, factory=uuid4))


def user_context():
    return str(get_thread_local(USERCONTEXT_KEY, factory=None))


def set_thread_local(key, set_value=None):
    try:
        delattr(THREAD_LOCAL, key)
    except AttributeError:
        pass
    if set_value:
        setattr(THREAD_LOCAL, key, set_value)


def get_thread_local(var_name, factory, *args, **kwargs):
    v = getattr(THREAD_LOCAL, var_name, None)
    if v is None and factory is not None:
        v = factory(*args, **kwargs)
        setattr(THREAD_LOCAL, var_name, v)
    return v


class TransactionLogger(logging.LoggerAdapter):
    """
    This example adapter expects the passed in dict-like object to have a
    'connid' key, whose value in brackets is prepended to the log message.
    """

    def __init__(self, logger, extra=None):
        if extra is None:
            extra = {}
        logging.LoggerAdapter.__init__(self, logger, extra)

    def process(self, msg, kwargs):
        return 'TxId=[%s] User=[%s] %s' % (transaction_id(), user_context(), msg), kwargs