#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-12 15:44:16
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
import os
from main import app, db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integet, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    passwd = db.Column(db.String(64), nullable=False)
    born = db.Column(db.Date)

    

    def __repr__(self):
        return 'id:{}, name:{}'.format(self.id, self.username)




if __name__ == '__main__':
    pass
