#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    sql 查询从不订购的客户
"""

# sql 语句， 使用 not in 来解决, 453ms
"""
    select Name as Customers from Customers where ID not in (select distinct CustomerId from Orders); 
"""

# 思路2 使用左连接, 441ms
"""
    select t1.Name as Customers from Customers t1 left join Orders t2 on t1.Id = t2.CustomerId where t2.Id is null;
"""