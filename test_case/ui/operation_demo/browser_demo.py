#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'gy_hejp'
__mtime__ = '2019/7/30'
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
# 打开浏览器
from time import sleep

from selenium import webdriver

from config.conf import DRIVER_PATH, GY_WEB_URL

driver = webdriver.Chrome(DRIVER_PATH)

#调整浏览器窗口大小
driver.maximize_window()
sleep(2)
  # 自定义窗口大小（不推荐使用）
#driver.set_window_size(1280,960)

# 打开网址
driver.get(GY_WEB_URL)
sleep(3)
driver.get("https://www.baidu.com")
sleep(3)
driver.get("https://www.taobao.com")

#后退
driver.back()
sleep(2)

#前进
driver.forward()
sleep(2)

#刷新
driver.refresh()
sleep(2)

sleep(5)
#关闭浏览器
driver.close()
#退出驱动
driver.quit()
