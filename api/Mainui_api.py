# coding:utf-8
import requests
from api.BaseApi import BaseApi

class MainApi(BaseApi):
    def get_product(self):
        # r=requests.get("http://open.10086.cn/api/content/capabilityData",verify=False).json()
        # return r['message']
        r=self.loadapi('../ApiData/Mainprocess.yaml','get_product')
        return r
    def get_solution(self):
        r=self.loadapi('../ApiData/Mainprocess.yaml','get_solution')
        return r
    def get_bottom(self):
        r=self.loadapi('../ApiData/Mainprocess.yaml','get_bottom')
        return r