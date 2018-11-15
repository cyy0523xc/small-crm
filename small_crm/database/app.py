# -*- coding: utf-8 -*-
#
#
# Author: alex
# Created Time: 2018年09月26日 星期三 18时30分03秒
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from .tables import db, app

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
