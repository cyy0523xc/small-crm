# -*- coding: utf-8 -*-
#
# 安装程序
# Author: alex
# Created Time: 2018年04月02日 星期一 17时29分45秒
from distutils.core import setup


LONG_DESCRIPTION = """
模型快速封装工具
""".strip()

SHORT_DESCRIPTION = """
模型快速封装工具""".strip()

DEPENDENCIES = [
    'flask',
    'flask_restful',
    'numpy',
    'pandas',
    'scipy',
    'sklearn',
    'fastparquet',
    'pyarrow',
    'jsonschema',
    'mysqlclient',
    'flask_sqlalchemy',
    'flask_script',
    'flask_migrate',
]

VERSION = '1.0'
URL = 'https://git.ibbd.net/model/model-flow.git'

setup(
    name='model_flow',
    version=VERSION,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,

    author='Alex Cai',
    author_email='cyy0523xc@gmail.com',
    license='Apache Software License',

    keywords='model restful api interface for python',

    packages=['model_flow',
              'model_flow.database',
              'model_flow.tracking',
              'model_flow.model',
              'model_flow.server',
              'model_flow.celery_tasks',
              ],
)
