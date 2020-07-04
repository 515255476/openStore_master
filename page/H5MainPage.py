# coding:utf-8
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from page.BasePage import BasePage


class H5MainPage(BasePage):

    def goto_H5product(self, url, product_data):
        try:
            self.driver.get(url)
            self.driver.refresh()
            sleep(3)
        # self.driver.find_element_by_xpath("//div[@class='general-bg']//h2[text()='"+product_data+"']")
        # self.find("//div[@class='general-bg']//h2[text()='"+product_data+"']")
            self.loadStep('.././Data/H5MainPage.yaml','goto_H5product',var1=product_data)
            return True
        except Exception as e:
            print("无法打开h5能力产品页面, 地址：%s" % url)
            return False


    def goto_H5solution(self,url,solution_data):
        try:
            self.driver.get(url)
            self.driver.refresh()
            sleep(3)
            # self.find("//div[@class='title']//h4[text()='" + solution_data + "']")
            # self.driver.find_element_by_xpath("//div[@class='title']//h4[text()='" + solution_data + "']")
            self.loadStep('.././Data/H5MainPage.yaml','goto_H5solution',var1=solution_data)
            return True

        except Exception as e:
            print("无法打开h5解决方案页面, 地址：%s" % url)
            return False

    def gotoh5mainpage(self):
        try:
            self.driver.get("https://open.10086.cn/mobile/#/home")
            sleep(2)
            # self.find("//div[@class='am-flexbox-item capability-section-title']")
            self.loadStep('.././Data/H5MainPage.yaml','gotoh5mainpage')
            return True

        except Exception as e:
            print("无法打开h5首页")
            return False


    def express(self):
        pass
    def cooperation(self):
        pass
    def selected(self):
        pass
    def dynamic(self):
        pass

