# coding:utf-8
from time import sleep

from selenium import webdriver


class Driver(object):
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('headless')
    options.add_argument('disable-dev-shm-usage')
    _driver = webdriver.Chrome(options=options)
    # _driver=webdriver.Chrome()
    @classmethod
    def start_web(cls):
        cls._driver.implicitly_wait(10)
        cls._driver.get('https:/open.10086.cn')
        sleep(2)
        return cls._driver
