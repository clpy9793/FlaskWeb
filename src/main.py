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

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return redirect("http://www.baidu.com/")


if __name__ == '__main__':
    app.run(debug=True, port=8888)
