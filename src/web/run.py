#!/usr/bin/python
# -*- coding: utf-8 -*-

from controller.baseController import app

print(app.url_map)
app.run(debug=True)