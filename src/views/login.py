#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-14 10:50:32
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
import os
from views import app

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass

if __name__ == '__main__':
    pass
