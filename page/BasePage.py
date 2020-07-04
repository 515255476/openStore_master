# coding:utf-8
from time import sleep

from driver.Driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import  yaml


class BasePage(object):
    def __init__(self):
        self.driver = Driver._driver
        self.driver.maximize_window()
        # self.driver.get('https:/open.10086.cn')


    def find(self,key):
        return self.driver.find_element_by_xpath(key)


    def loadStep(self,op_path,key,**kwargs):
        file=open(op_path)
        po_data=yaml.load(file)
        po_method=po_data[key]
        for step in po_method:
            location=step['location']
            for k,v in kwargs.items():
                location=str(step['location']).replace('$%s' %k, v)
            element= self.driver.find_element_by_xpath(location)
            action= str(step['action'])
            print(action)
            if action=='click':
                sleep(2)
                element.click()
                sleep(2)
            elif action=='none':
                return element
            else:
                "unknow commond"





    # def find(self,kv):
    #     return self.driver.find_element(*kv)


    def back(self):

        self.driver.back()
        return self

    def forward(self):

        self.driver.forward()
        return self

    def open_url(self, url):

        self.driver.get(url)
        return self




    def quitBrowser(self):

        self.driver.quit()
        return self
