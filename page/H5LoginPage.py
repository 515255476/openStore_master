# coding:utf-8
from time import sleep
from page.BasePage import BasePage
from page.WebMainPage import MainPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class H5LoginPage(BasePage):
    def gotologinpage(self):
        try:
            self.driver.get("https://open.10086.cn/mobile/#/home")
            sleep(3)
            # self.find('//i[@class="iconfont"]//img[@src="assets/images/icon-user.svg"]').click()
            # # self.driver.find_element_by_xpath('//i[@class="iconfont"]//img[@src="assets/images/icon-user.svg"]').click()
            # sleep(3)
            # self.find('//a[@class="am-button am-button-primary"]//span[text()="登 录"]')
            # # self.driver.find_element_by_xpath('//a[@class="am-button am-button-primary"]//span[text()="登 录"]')
            po_path='.././Data/H5LoginPage.yaml'
            self.loadStep(po_path,'gotologinpage')
            return True

        except Exception as e:
            print("无法打开登录页面")
            return False
