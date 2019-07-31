#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'gy_hejp'
__mtime__ = '2019/7/25'
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
from tools import request_tool
from tools import assert_tool
from tools import random_tool
from tools import mysql_tool
from tools import excel_tool
from tools import log_tool
from tools import os_tool
from tools import shell_tool
import pytest
import allure
# 项目根目录建config包，里面建conf.py文件，用于配置
data={}
from config import conf

# 导包 demo_import_api
# 找模板写测试用例 demo_http_
# test_change_pwd_var方法名，可以自定义，但是必须是test_开头
# 注册
@allure.feature('后台用户管理流程')
@allure.story('注册-新用户')
def test_change_pwd_var():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/admin/register'
    username =random_tool.random_str_abc(6)
    req = {
  "email": "3309843696@qq.com",
  "icon": "string",
  "nickName": "string",
  "note": "string",
  "password": "1234",
  "username": username
}

    resp = request_tool.post_request(url, json=req)
    body = resp.json()

    # 判断响应码
    with allure.step("断言响应状态码，实际结果是：{}，预期结果为：200".format(resp.status_code)):
        pass
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    with allure.step("断言用户名，实际结果是：{}，预期结果为：{}".format(body['data']["username"],username)):
        pass
    assert_tool.assert_equal(body['data']["username"],username)
    data["id"] = body['data']["id"]


    data['ab']=username
# 分配角色
@allure.feature('后台用户管理流程')
@allure.story('给用户分配角色')

def test_user_update_role():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL +'/admin/role/update'
    req = {
        "adminId": data['id'],
        "roleIds": [1,2,3]
    }

    resp = request_tool.post_request(url, data=req)
    body = resp.json()
    # 判断响应码
    with allure.step("断言响应状态码，实际结果是：{}，预期结果为：200".format(resp.status_code)):
        pass
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    with allure.step("断言用户角色，实际结果是：{}，预期结果为：3".format(body['data'])):
        pass
    assert_tool.assert_equal(body['data'],3)

# 查询用户角色信息
@allure.feature('后台用户管理流程')
@allure.story('查询用户角色信息')
def test_change_pwd():
        # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
        url = conf.GY_API_URL+'/admin/role/{}'.format(data["id"])

        resp = request_tool.get_request(url)
        body = resp.json()
        # 判断响应码
        with allure.step("断言响应状态码，实际结果是：{}，预期结果为：200".format(resp.status_code)):
            pass
        assert_tool.assert_equal(resp.status_code, 200)
        # 自定义断言
        with allure.step("断言用户id，实际结果是：{}，预期结果为：1".format(body['data'][0]["id"])):
            pass
        assert_tool.assert_equal(body['data'][0]["id"],1)

#登录
@allure.feature('后台用户管理流程')
@allure.story('登录')
def test_change_login_var():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/admin/login'
    req = {
  "password": "1234",
  "username": data['ab']
}
    resp = request_tool.post_request(url, json=req)
    body = resp.json()
    # 判断响应码
    with allure.step("断言响应状态码，实际结果是：{}，预期结果为：200".format(resp.status_code)):
        pass
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['data'][ "tokenHead"],"Bearer ")
    data['token'] = body['data']['tokenHead'] + body['data']['token']
#获取当前登录用户信息
@allure.feature('后台用户管理流程')
@allure.story('获取当前登录用户信息')
def test_user_info():
    # config/conf.py里面配置GY_API_URL,模板快捷键demo_conf_api
    url = conf.GY_API_URL + '/admin/info'
    headers = {
            'Authorization':data['token'],
            'charset':'UTF-8'
    }
    resp = request_tool.get_request(url,headers=headers)
    body = resp.json()
    # 判断响应码
    assert_tool.assert_equal(resp.status_code, 200)
    # 自定义断言
    assert_tool.assert_equal(body['data']["username"], data['ab'])