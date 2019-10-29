# -*- coding:UTF-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import logging
import pytest
from time import sleep

# logging.basicConfig函数对日志的输出格式及方式做相关配置
# filename: 指定日志文件名，如my.log 或my.txt
# filemode: 和file函数意义相同，指定日志文件的打开模式，'w'或'a'
# format: 指定输出的格式和内容，format可以输出很多有用信息，如下例所示:
# datefmt: 指定时间格式，同time.strftime()
# level: 设置日志级别，默认为logging.WARNING
# stream: 指定将日志的输出流，可以指定输出到sys.stderr,sys.stdout或者文件，默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略

# format的格式设置
# %(levelno)s: 打印日志级别的数值
# %(levelname)s: 打印日志级别名称
# %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s: 打印当前执行程序名
# %(funcName)s: 打印日志的当前函数
# %(lineno)d: 打印日志的当前行号
# %(asctime)s: 打印日志的时间
# %(thread)d: 打印线程ID
# %(threadName)s: 打印线程名称
# %(process)d: 打印进程ID
# %(message)s: 打印日志信息

# logging.basicConfig(level=logging.DEBUG,
#                     filename='logging.txt',
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# logging.info("print logging info")
# logging.warning("print logging warning")
# logging.debug("print loggin debug")
# logging.error("print logging error")
# logging.critical("print logging critical")



# 第一个简单的selenium小程序
# def test_browser():
#     # browser = webdriver.Chrome()
#     browser = webdriver.Firefox()
#
#     browser.get('https://testerhome.com')
#     search = browser.find_element_by_name('q')  # 元素的定位
#     search.send_keys("selenium")# 输入信息
#     search.send_keys(Keys.ENTER)
#     sleep(20)

# 7/25日基础课程的可见作业
# def test_testerhome():
#     driver = webdriver.Firefox()
#     driver.get("https://testerhome.com/")
#     driver.find_element(By.LINK_TEXT, "先到先得！第五届中国移动互联网测试开发大会 PPT 提供下载啦").click()
#     driver.find_element(By.LINK_TEXT, "https://testerhome.com/topics/19664").click()
#
# test_testerhome()



# 7/28日进阶篇selenium
# 1. css的定位

# class Test_selenium:
#     def test_selenium1(self):
#         driver = webdriver.Firefox()
#         ActionChains(self.driver).click_and_hold()

# 课后作业;
from selenium.webdriver.common.keys import Keys


# class Test_testerhome(object):
#
#
#     def setup_method(self):
#         self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(5)
#         self.driver.get("https://testerhome.com/")
#         # self.driver.maximize_window()
#
#     # 社区访问霍格沃兹测试学院，断言未登录是被拒绝的
#     # 错误用户名和密码登陆
#     def test_browser(self):
#         self.driver.find_element_by_xpath("(//ul[@class='nav user-bar navbar-nav navbar-right']/li/a)[2]").click()
#         self.driver.find_element_by_xpath("//div[@class='form-group']/input[@id='user_login']").send_keys('jjj')
#         self.driver.find_element_by_xpath("//div[@class='form-group']/input[@id='user_password']").send_keys('111')
#         self.driver.find_element_by_xpath("//div[@class='form-actions']/input[@name='commit']").click()
#
#         alert = self.driver.find_element_by_xpath("//div[@class='alert alert-warning']").text
#         print(alert)
#         assert (alert == "没有该用户，请您重新注册。")
#         sleep(3)
#
#     # 搜索”测试媛“，找到成立的那个帖子，进去后断言标题与搜索出来的标题是对应的
#     def test_webtitle(self):
#         Search_bar = self.driver.find_element_by_xpath("//div/input[@class='form-control']")
#         Search_bar.send_keys('测试媛')
#         Search_bar.send_keys(Keys.ENTER)
#         self.driver.find_element_by_partial_link_text("组织成立啦").click()
#         title_name = self.driver.find_element_by_xpath("(//span[@class='title'])[1]").text
#         assert '测试媛组织成立啦' in title_name
#
#
#     def teardown_method(self):
#         self.driver.quit()



