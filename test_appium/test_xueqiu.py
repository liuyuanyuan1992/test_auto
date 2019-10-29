# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
# 第一个通过Appium录制的代码

from appium import webdriver
from time import sleep

from appium.webdriver.common.touch_action import TouchAction


class TestXueqiu:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "mumu"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = True

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(20)
        #等待元素出现
        self.driver.find_element_by_id("user_profile_icon")

    # 测试个人中心页面的内容
    # def test_profile(self):
    #     pass
        # self.driver.find_element_by_id("user_profile_icon").click()
        # print(self.driver.find_element_by_id("user_profile_icon").get_attribute("class"))
        # pass

    # def test_click(self):
    #
    #     self.driver.tap()

    # def test_get_attribute(self):
    #     pass
        # print(self.driver.find_element_by_id("user_profile_icon").get_attribute("class"))
        # 报错找不到class类

    # def test_selected(self):
    #
    #     self.driver.find_element_by_xpath("//*[contains(text,'行情')]").click()
    #     self.driver.find_element_by_xpath("//*[@text='行情']").click()
    #     pass

    #
    # def test_swipe(self):
    #
    #     self.driver.swipe(100, 200, 500, 800, 1000)
    #
    # def test_long_press(self):
    #
    #     el = self.driver.find_element_by_xpath("(//*[@text='基金'])[1]")
    #     TouchAction(self.driver).long_press(el).perform()
    #
    # def test_uiautomator(self):
    #
    #     self.driver.find_element_by_android_uiautomator('new UiSelector().text("Animal")')

    def test_search(self):

        self.driver.find_element_by_id("tv_search").click()
        self.driver.find_element_by_id("search_input_text").send_keys("alibaba")
        self.driver.find_element_by_id("name").click()
        list = self.driver.find_element_by_xpath("//*[contains(@resource-id,'stockCode') and @text='BABA']/../../.."
                                                 "//*[contains(@resource-id,'current_price')]").text
        print(list)
        assert float(list) > 100

    def teardown(self):

        sleep(5)
        self.driver.quit()

