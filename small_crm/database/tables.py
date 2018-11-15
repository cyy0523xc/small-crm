# -*- coding: utf-8 -*-
#
# 数据表定义
# Author: alex
# Created Time: 2018年11月15日 星期四 21时17分08秒
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from small_crm.data_struct import Color, Shape
from small_crm.settings import DBConfig
from small_crm.app import app

db = SQLAlchemy(app)
tb_prefix = DBConfig.TB_PREFIX


class Product(db.Model):
    """商品基本信息表"""
    __tablename__ = tb_prefix + 'product'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True, comment='名称')
    color = db.Column(db.Enum(Color), nullable=False, index=True, comment='颜色')
    shape = db.Column(db.Enum(Shape), nullable=False, index=True, comment='形状')
    price = db.Column(db.DECIMAL(8, 2), comment='进货价格')
    sell_price = db.Column(db.DECIMAL(8, 2), comment='销售价格')
    remark = db.Column(db.String(100), comment='备注')
    created_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    updated_at = db.Column(db.DateTime, index=True, default=datetime.now, onupdate=datetime.now, comment='最后更新时间')


class ProductStock(db.Model):
    """商品库存表"""
    __tablename__ = tb_prefix + 'product_stock'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_id = db.Column(db.Integer, unique=True, nullable=False)
    quantum = db.Column(db.Integer, default=0, index=True)
    amount = db.Column(db.DECIMAL(15, 2), comment='库存总价值')
    purchase_at = db.Column(db.DateTime, comment='最后进货时间')
    sell_at = db.Column(db.DateTime, comment='最后销售时间')


class PurchaseRecord(db.Model):
    """进货记录表"""
    __tablename__ = tb_prefix + 'purchase_record'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_id = db.Column(db.Integer, unique=True, nullable=False)
    quantum = db.Column(db.Integer, default=0)
    amount = db.Column(db.DECIMAL(15, 2), comment='总价值')
    price = db.Column(db.DECIMAL(8, 2), comment='进货价格')
    supplier = db.Column(db.String(20), nullable=False, index=True)
    contact = db.Column(db.String(20), nullable=False, comment='联系方式')
    remark = db.Column(db.String(100), comment='备注')
    created_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')


class OrderRecord(db.Model):
    """出货订单表表"""
    __tablename__ = tb_prefix + 'order_record'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    product_id = db.Column(db.Integer, unique=True, nullable=False)
    quantum = db.Column(db.Integer, default=0)
    amount = db.Column(db.DECIMAL(15, 2), comment='总价值')
    price = db.Column(db.DECIMAL(8, 2), comment='进货价格')
    sell_price = db.Column(db.DECIMAL(8, 2), comment='出货价格')
    seller = db.Column(db.String(20), nullable=False, index=True)
    customer = db.Column(db.String(20), nullable=False, index=True)
    contact = db.Column(db.String(20), nullable=False, comment='联系方式')
    remark = db.Column(db.String(100), comment='备注')
    created_at = db.Column(db.DateTime, default=datetime.now, comment='创建时间')


class ProductClass(db.Model):
    """商品类别表"""
    __tablename__ = tb_prefix + 'product_class'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True, comment='名称')
    remark = db.Column(db.String(100), comment='备注')
