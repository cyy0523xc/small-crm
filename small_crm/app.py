# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2018年11月15日 星期四 21时09分26秒
from flask import Flask
from .settings import DBConfig

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = DBConfig.URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 上传文件大小限制: 25M
app.config['MAX_CONTENT_LENGTH'] = 25 * 1024 * 1024
# fixed: MySQL server has gone away
app.config['SQLALCHEMY_POOL_SIZE'] = 128  # 线程池大小
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 90  # 超时时间
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3  # 空闲连接自动回收时间
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 128  # 控制在连接池达到最大值后可以创建的连接数。

# 测试
app.config['SQLALCHEMY_ECHO'] = True
