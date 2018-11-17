#!/bin/bash
# 
# 本地测试时可以使用
# Author: alex
# Created Time: 2018年09月30日 星期日 18时11分54秒

sudo docker rm -f mysql
sudo docker run -d --name mysql \
    -p 3306:3306 \
    -e MYSQL_ROOT_PASSWORD=ibbdnet \
    registry.cn-hangzhou.aliyuncs.com/ibbd/mariadb
