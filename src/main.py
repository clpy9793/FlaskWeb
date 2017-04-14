#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-12 10:28:16
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
import os

from flask import Flask
from flask import session
from flask import redirect
from flask.ext.sqlalchemy import SQLAlchemy
from views import *


app = Flask(__name__)
database_path = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), 'data.sqlite')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(database_path)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
db.create_all()



if __name__ == '__main__':
    app.run(debug=True, port=8888)
