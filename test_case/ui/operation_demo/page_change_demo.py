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

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from config.conf import DRIVER_PATH

# 打开浏览器
driver = webdriver.Chrome(DRIVER_PATH)

# 调整浏览器窗口大小(最大化，推荐使用)
driver.maximize_window()

def url_demo():

    driver.get("D:\\softwareData\\python\\gy_hejp\\demo.html")





def open_a():
    baidu=driver.find_element_by_partial_link_text("度娘")
    dangdang=driver.find_elements_by_partial_link_text("当当")
    jingdong=driver.find_element_by_partial_link_text("京东")
    b=ActionChains(driver)
    b.key_down(Keys.CONTROL).click(baidu).click(dangdang).click(jingdong).key_up(Keys.CONTROL).perform()
    sleep(2)

def windows_change_demo():
    c=driver.window_handles
    for d in c:
        driver.switch_to.window(d)
        sleep(2)
        if(driver.title.__contains__("当当")):
            break

def reset_demo():
    # 操作页面元素
    # 定位元素//input[@type="text"]
   driver.find_element_by_xpath('//input[@type="reset"]').click()

def alert_demo():
    f=driver.switch_to.alert
    f.accept()

def reset_button_demo():
    # 操作页面元素
    # 定位元素//input[@type="text"]
   driver.find_element_by_xpath('//input[@type="button"]').click()

def alert_button_demo():
    g=driver.switch_to.alert
    g.send_keys("HAHAHA")
    g.accept()





if __name__ == '__main__':
    url_demo()
    sleep(2)
    # open_a()
    # windows_change_demo()
    # reset_demo()
    # sleep(2)
    # alert_demo()
    # sleep(2)
    reset_button_demo()
    sleep(2)
    alert_button_demo()
    sleep(2)
    driver.quit()
