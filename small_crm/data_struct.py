# -*- coding: utf-8 -*-
#
# 定义数据结构
# Author: alex
# Created Time: 2018年11月15日 星期四 21时13分51秒
from enum import Enum


class Color(str, Enum):
    red = '红色'
    yellow = '黄色'


class Shape(str, Enum):
    stripe = '条纹'
