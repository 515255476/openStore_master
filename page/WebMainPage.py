# coding:utf-8
from time import sleep

import pytest

from page.BasePage import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(BasePage):
    def mainpagecheck(self):
        try:
            self.driver.get("https://open.10086.cn/")
            sleep(3)
            # self.find("//div[text()='动态馆']")
            self.loadStep('.././Data/WebMainPage.yaml','mainpagecheck')
            return True
        except Exception as e:
            print("无法打开web首页")
            return False


    def gotoproduct(self,product_data):
        try:
            # self.driver.find_element_by_xpath("//li[text()='产品馆']").click()
            # self.find("//li[text()='产品馆']").click()
            # sleep(3)
            # self.find("//div[@class='index_ability_3ymPB']//a[text()='"+str(product_data)+"']").click()
            # sleep(2)
            # self.find("//div[@class='index_title_1nvtg' and text()='" + str(product_data) + "']")
            # self.driver.find_element_by_xpath("//div[@class='index_ability_3ymPB']//a[text()='"+str(product_data)+"']").click()
            # self.driver.find_element_by_xpath("//div[@class='index_title_1nvtg' and text()='" + str(product_data) + "']")
            self.loadStep('.././Data/WebMainPage.yaml','gotoproduct',var1=product_data)
            return True
        except Exception as e:
            print("无法打开能力页面：%s" % product_data)
            return False


    def gotosolution(self,solution_data):
        try:
        # self.driver.find_element_by_xpath("//li[text()='方案馆']").click()
        # sleep(4)
        # self.driver.find_element_by_xpath("//div[@class='index_solution_item_3K7aF']//a[text()='"+str(solution_data)+"']").click()
        # sleep(3)
        # self.driver.find_element_by_xpath("//div[@class='index_title_2jp90' and text()='" + str(solution_data) + "']")
            self.loadStep('.././Data/WebMainPage.yaml','gotosolution',var1=str(solution_data))

            return True
        except Exception as e:
            print("无法打开能力页面：%s" % solution_data)
            return False

    def express(self):
        pass
    def cooperation(self):
        pass
    def selected(self):
        pass
    def dynamic(self):
        pass

