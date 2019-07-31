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
from time import sleep

from selenium import webdriver

from config.conf import DRIVER_PATH


def open_browser():
    # 打开浏览器
    driver = webdriver.Chrome(DRIVER_PATH)

    # 调整浏览器窗口大小(最大化，推荐使用)
    driver.maximize_window()
    return driver

def quit_browser(driver):
    # 关闭浏览器
    driver.quit()



driver = open_browser()
def url_demo():

    driver.get("D:\\softwareData\\python\\gy_hejp\\demo.html")
def text_demo():
    # 操作页面元素
    # 定位元素//input[@type="text"]
    text = driver.find_element_by_xpath('//input[@type="text"]')
    #操作元素
    #清空
    text.clear()
    text.send_keys("wenzhubielang")
    # #获取属性值
    # print(text.get_attribute("value"))
    # sleep(2)

def file_demo():
    # 操作页面元素
    # 定位元素//input[@type="text"]
    file = driver.find_element_by_xpath('//input[@type="file"]')
    #操作元素
    #清空
    file.clear()
    file.send_keys("D:\\softwareData\\timg.jpg")

def radio_demo():
    # 操作页面元素
    # 定位元素//input[@type="text"]
    radio = driver.find_element_by_xpath('(//input[@type="radio"])[1]')
    radio.click()

def checkbox_demo():

    radio = driver.find_element_by_xpath('//input[@type="checkbox"][1]')
    radio.click()
    radio = driver.find_element_by_xpath('//input[@type="checkbox"][2]')
    radio.click()

def button_demo():

    button = driver.find_element_by_xpath('//input[@type="button"]')
    button.click()

def password_demo():
    password = driver.find_element_by_xpath('//input[@type="password"]')
    password.click()
    password.send_keys("qwertyu")

def number_demo():
    number = driver.find_element_by_xpath('//input[@type="number"]')
    number.click()
    number.send_keys("123456")


def date_demo():
    js='''var xpath = '//input[@type="date"]';var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.setAttribute("value","2019-07-30");'''
    driver.execute_script(js)

def time_demo():
    time = driver.find_element_by_xpath('//input[@type="time"]')
    time.clear()
    time.send_keys('17:10')

def textarea_demo():
    textarea = driver.find_element_by_xpath('//td/textarea')
    textarea.clear()
    textarea.send_keys('asdfgh')

def select_demo():
    select = driver.find_element_by_xpath('//td/select/option[1]')
    select.click()
    # select = driver.find_element_by_xpath('//td/select/option[2]')
    # select.click()

def href_demo():
    # href = driver.find_element_by_xpath('//td/a[1]')
    # href.click()
    href = driver.find_element_by_xpath('//td/a[2]')
    href.click()

if __name__ == '__main__':
    url_demo()
    sleep(2)
    # text_demo()
    # sleep(2)
    # file_demo()
    # sleep(2)
    # radio_demo()
    # sleep(2)
    # checkbox_demo()
    # sleep(2)
    # # button_demo()
    # # sleep(2)
    # password_demo()
    # sleep(2)
    # number_demo()
    # sleep(2)
    date_demo()
    sleep(2)
    time_demo()
    sleep(2)
    textarea_demo()
    sleep(2)
    select_demo()
    sleep(2)
    href_demo()
    sleep(2)

    quit_browser(driver)
