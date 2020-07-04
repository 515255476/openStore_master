# coding:utf-8
from time import sleep
from page.BasePage import BasePage
from page.WebMainPage import MainPage


class LoginPage(MainPage):
    def gotologinpage(self):
        try:
            # self.driver.find_element_by_xpath('//a[text()="登录"]').click()
            # self.driver.find_element_by_xpath('//button[@class="ant-btn ant-btn-primary ant-btn-block"]')
            # self.find('//a[text()="登录"]').click()
            # sleep(2)
            # self.find('//button[@class="ant-btn ant-btn-primary ant-btn-block"]')
            self.loadStep('.././Data/WebLoginPage.yaml','gotologinpage')
            return True

        except Exception as e:
            print("无法打开登录页面")
            return False