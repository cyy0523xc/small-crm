# -*- coding: utf-8 -*-
#
# 全局配置文件
# Author: alex
# Created Time: 2018年09月26日 星期三 18时32分16秒

# 版本号
version = 'v1.0'
build_at = '20181110'

# 数据库配置
db_name = 'eyemodel_engine'
db_user = 'root'
db_passwd = 'scut2018'
db_host = '172.17.0.1'


class DBConfig:
    """数据库配置"""
    URI = 'mysql://%s:%s@%s/%s?charset=utf8' % (db_user, db_passwd, db_host, db_name)
    TB_PREFIX = 'scrm_'  # 表名前缀
    DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
