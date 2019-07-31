#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'gy_hejp'
__mtime__ = '2019/7/31'
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
from time import sleep


def test_login(base):
#打开登录界面http://qa.yansl.com/#/login
    base.get("打开登录界面",'http://qa.yansl.com')
#输入用户名
    base.send_keys("输入用户名",'//input[@name="username"]',"admin")
#输入密码
    base.send_keys("输入密码",'//input[@name="password"]',"123456")
#点击登录
    base.click("点击登录",'''(//span[contains(text(),'登录')])[1]''')
#点击残忍拒绝
    base.click("点击残忍拒绝",'''//span[text()='残忍拒绝']''')
#点击登录
    base.click("点击登录",'''(//span[contains(text(),'登录')])[1]''')
    sleep(3)
#点击商品
    base.click("点击商品", '''(//span[@slot="title"])[1]''')
#点击添加商品
    base.click("点击添加商品", '''(//span[text()="添加商品"])[1]''')
#商品分类
    base.click("点击商品分类", '''//span[@class="el-cascader__label"]''')
    base.click("点击服装", '''//li[text()="服装"]''')
    base.click("点击外套", '''//li[contains(text(),"外套")]''')

# 输入商品名称
    base.send_keys("输入商品名称", '''//label[contains(text(),"商品名称")]/..//input''',"aaaa")
# 输入副标题
    base.send_keys("输入副标题", '''//label[contains(text(),"副标题")]/..//input''',"哈哈")
# 商品品牌
    base.click("点击商品品牌", '''//input[@placeholder="请选择品牌"]"]''')
    base.click("点击小米", '''//li/span[text()="小米"]''')
#断言

















