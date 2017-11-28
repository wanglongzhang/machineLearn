#!/usr/bin/python
# -*- coding: utf-8 -*-

from controller.baseController import api, db
import json
import time


class BaseDAO(object):
    def __init__(self, model_clazz):
        self.model_clazz = model_clazz

    def get_query_obj(self):
        return self.model_clazz.query

    def get_one_entry(self, id):
        entry = self.get_query_obj().filter_by(id=id).first()
        if entry is None:
            api.abort(404, "{} {} doesn't exist".format(self.model_clazz, id))
        return entry

    def get_all_entry(self):
        return self.get_query_obj().all()

    def get_partial_entry(self, start, offset):
        api.abort(404, "{} {} doesn't exist".format(self.model_clazz, id))

    def create(self, data):
        new_obj = self.model_clazz()
        # if hasattr(self.model_clazz, "create_time"):
        #     data["create_time"] =
        # import pdb; pdb.set_trace()
        for each_k, each_v in data.items():
            setattr(new_obj, each_k, each_v)

        db.session.add(new_obj)
        db.session.commit()

    def update(self, id, data):
        self.get_query_obj().filter_by(id=id).update(data)
        db.session.commit()

    def delete(self, id):
        to_operate_entry = self.get_one_entry(id)
        db.session.delete(to_operate_entry)
        db.session.commit()