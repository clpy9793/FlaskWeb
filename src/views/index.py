#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-14 10:50:48
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$
import os
from views import app
from flask import redirect


@app.route('/', methods=['GET'])
def index():
    return redirect("http://www.baidu.com/")


if __name__ == '__main__':
    pass
