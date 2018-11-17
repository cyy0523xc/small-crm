#!/bin/bash
# 
# 本地测试启动脚本
# Author: alex
# Created Time: 2018年10月29日 星期一 15时06分20秒
if
    ps -ef | grep -E '00:00:00 mysqld$' | grep -v "grep"
then
    echo 'mysqld已经成功启动'
else
    echo '准备启动mysql...'
    bash ./local-mysql.sh

    # 安装最新版本
    echo
    sudo -H python3 setup.py install

    # 等待mysql成功启动
    while true; do
        if
            ps -ef | grep -E '00:00:00 mysqld$' | grep -v "grep"
        then
            echo 'mysqld已经成功启动'
            break
        else
            echo '等待mysqld的成功启动'
            sleep 1
        fi
        echo 
    done

    # 创建数据库
    echo
    echo '创建数据库：'
    sleep 1
    sudo docker exec -ti mysql \
        mysql -uroot -pibbdnet -e "create database small_crm"

    # 执行迁移脚本
    echo
    echo '执行迁移脚本：'
    cd ./model_flow/database
    rm -rf migrations
    flask db init
    flask db migrate -m 'first'
    flask db upgrade
    cd -
fi
