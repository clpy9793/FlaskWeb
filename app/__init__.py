#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-14 13:32:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
import os
from flask import Flask
from flask import Blueprint
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()
mail = Mail()


def create_app(config_name):
    """"""
    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    mail.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app


if __name__ == '__main__':
    pass
