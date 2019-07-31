#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'gy_hejp'
__mtime__ = '2019/7/24'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
# 发送一个请求的包名，工具requests
# 安装requests包
# 导入
import requests

# a={
#   "password": "123456",
#   "username": "admin"
# }
# b=requests.post("http://qa.yansl.com:8080/admin/login",json=a)
# print(b.text)

# #键值对post请求，data
# c={'adminId':36,'permissionIds':[2,3]}
# d=requests.post("http://qa.yansl.com:8080/admin/permission/update",data=c)
# print(d.text)

#get请求传数据，params
e={'name':'admin','pageSize':5,'pageNum':1}
f=requests.get('http://qa.yansl.com:8080/admin/list',params=e)
print(f.text)


