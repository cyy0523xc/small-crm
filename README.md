# small-crm
基于graphene，sqlalchemy和flask的练手项目

ps：一直想上手一下GraphQL，却没有实际的应用机会，这次正好练手，以后真正用到产品上。

## TODO

基础功能

- [ ] 商品录入
  - 商品名称
  - 商品类别
  - 颜色
  - 形状
- [ ] 进货
  - 商品ID
  - 进货数量
  - 进货价
- [ ] 销售
  - 商品ID
  - 出货数量
  - 出货价
- [ ] 查看订单
  - 按天查看
  - 按周查看
  - 按月查看
- [ ] 查看库存
  - 实时查看种商品的库存
- [ ] 销售统计
  - 每天销售统计
  - 每周销售统计
  - 每月销售统计

## 数据表

### 商品表 product

字段       | 类型         | 允许为空 | 默认值 | 备注
----       | ---          | ---      | ---    | ----
id         | int(10)      | 否       |        | 自增主键
name       | varchar(60)  | 否       |        | 唯一索引，商品名称
color      | enum         | 否       |        | 颜色
shape      | enum         | 否       |        | 形状
price      | decimal(8,2) | 否       |        | 单价
sell_price | decimal(8,2) | 否       |        | (建议)销售价格
remark     | varchar(100) | 是       |        | 备注信息
created_at | datetime     | 是       | now    | 创建时间
updated_at | datetime     | 是       | now    | 索引，最后更新时间

### 商品库存表 product_stock

字段        | 类型          | 允许为空 | 默认值 | 备注
----        | ---           | ---      | ---    | ----
id          | int(10)       | 否       |        | 自增主键
product_id  | int(10)       | 否       |        | 商品ID，唯一索引
quantum     | int(10)       | 是       | 0      | 库存数量
amount      | decimal(15,2) | 0        |        | 库存总价值 = 库存数量 × 单价
purchase_at | datetime      | 是       | now    | 最后进货时间
sell_at     | datetime      | 是       | now    | 最后销售时间

### 进货记录表 purchase_record

字段       | 类型          | 允许为空 | 默认值 | 备注
----       | ---           | ---      | ---    | ----
id         | int(10)       | 否       |        | 自增主键
product_id | int(10)       | 否       |        | 商品ID，索引
quantum    | int(10)       | 是       | 0      | 进货数量
price      | decimal(8,2)  | 0        |        | 进货价格
amount     | decimal(15,2) | 0        |        | 进货总价值 = 进货数量 × 进货价格
supplier   | varchar(20)   | 否       |        | 供货商
contact    | varchar(20)   | 否       |        | 供货商联系方式
remark     | varchar(100)  | 是       |        | 备注信息
created_at | datetime      | 是       | now    | 创建时间


### 出货订单表 order_record


字段       | 类型         | 允许为空 | 默认值 | 备注
----       | ---          | ---      | ---    | ----
id         | int(10)      | 否       |        | 自增主键
product_id | int(10)      | 否       |        | 商品ID，索引
quantum    | int(10)      | 是       | 0      | 出货数量
cost       | decimal(8,2) | 0        |        | 成本价格
price      | decimal(8,2) | 0        |        | 销售价格
seller     | varchar(20)  | 否       |        | 客户
customer   | varchar(20)  | 否       |        | 客户
contact    | varchar(20)  | 否       |        | 供货商联系方式
remark     | varchar(100) | 是       |        | 备注信息
created_at | datetime     | 是       | now    | 创建时间


### 商品类别表 product_class

字段   | 类型         | 允许为空 | 默认值 | 备注
----   | ---          | ---      | ---    | ----
id     | int(10)      | 否       |        | 自增主键
name   | varchar(20)  | 否       |        | 唯一索引
remark | varchar(100) | 是       |        | 备注信息

