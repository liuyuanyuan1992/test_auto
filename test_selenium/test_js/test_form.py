from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep




class TestSelenium:
    # 采用谷歌浏览器的debug模式跳过扫码登录
    # def setup(self):
    #     chrome_options = webdriver.ChromeOptions()
    #     chrome_options.debugger_address = "127.0.0.1:9999"
    #     self.driver = webdriver.Chrome(options=chrome_options)
    #     self.driver.implicitly_wait(5)
    #     # self.driver.get("https://testerhome.com/account/sign_in")
    #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame#material/image")

    # 采用cookie的模式跳过扫码登录
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    # def test_form_login(self):
    #     # 表单简单处理方法一：
    #     self.driver.find_element_by_css_selector("#user_login").send_keys("liuyuanyuan1992")
    #     self.driver.find_element_by_css_selector("#user_password").send_keys("lyy19920829@")
    #     self.driver.find_element_by_css_selector("#user_remember_me").click()
    #     self.driver.find_element_by_css_selector("#new_user > div.form-actions > input").click()
    #     value = login.get_attribute("value")  # get_attribute()是获取该元素的属性值
    #     print(value)
    #     self.driver.find_element(By.Name, "commit").click() #同理上句
    #
    #     # 复选表单简单处理方法二：Select类实例  未执行成功，待确认
    #     selector = Select(self.driver.find_element_by_css_selector("#user_login"))
    #
    #     sleep(5)

    # def test_upload(self):
    #     element_add = self.driver.find_element_by_xpath("//*[@id='materialMain']/div/div/div[1]/div[1]/a/span")
    #     self.driver.execute_script("arguments[0].click();", element_add)
    #     self.driver.find_element_by_css_selector("#js_upload_input")\
    #         .send_keys("/Users/liuyuanyuan/Project/Browser_Selenium/test_selenium/image/travel.jpg")
    #     # print(self.driver.page_source) #page_source为获取网页的源代码
    #     WebDriverWait(self.driver, 10).until(
    #         EC.invisibility_of_element_located((By.CSS_SELECTOR, ".material_picCard_cnt_cancelBtn js_uploadProgress_cancel"))
    #
    #     )
    #
    #     self.driver.execute_script("arguments[0].click()",
    #                                self.driver.find_element_by_xpath("//div/a[@d_ck='submit']"))
    #     sleep(5)


    def test_cookie(self):
        url = "https://work.weixin.qq.com/wework_admin/loginpage_wx#contacts"
        self.driver.get(url)
        cookie_add = {
            "wwrtx.sid": "8fL6FeBNWJNgaRTVvZ8Pcp1SraXZAUtuF7fb2whx5_qy2pHRzxDQtmiMtMyxa-Ee",
            "wwrtx.vst": "o71wwRwaAtR_aGGxK2LJi0rnXPKgOCTULR_aet22Ei9QCIyNWh14-4oXF8IHFTjVoi5sb5Lv9zvGyuK_5P6OCDDcqX0WMHrrbhcpNp4G3hN1MdyFfuewgGiN74eP5Fh0C5xGDtkewFqe-VMp_JSZOH0IgLMchse49yIcCLFQ78CzUNGS801Gt8whbnUyxhWyBiQFetacmFzjtJirf8XH6NNChed2-5X6-QMN3pcom8z-zet7zuB8IV014a12N5UOwMjWwapQ5knUCTmtFpyByA",
            "wwrtx.logined": "true"
        }


        for k, v in cookie_add.items():
            self.driver.add_cookie({"name": k, "value": v})

        self.driver.get(url)

        sleep(10)



    def teardown(self):
        self.driver.quit()
