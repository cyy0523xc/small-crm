# -*- coding: utf-8 -*-
#
# 数据库相关工具库
# Author: alex
# Created Time: 2018年11月01日 星期四 11时48分35秒


def get_obj_all_attrs(obj):
    """获取对象的所有属性"""
    all_attrs = dict(vars(obj))
    return [a[0] for a in all_attrs.items()
            if callable(getattr(obj, a[0])) is False and a[0].startswith('_') is False]


def set_obj_all_attrs(obj):
    """设置所有属性"""
    attrs = get_obj_all_attrs(obj)
    res = {}
    for k in attrs:
        v = getattr(obj, k)
        if v is not None:
            res[k] = v

    return res
