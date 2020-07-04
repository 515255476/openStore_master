# coding:utf-8
import requests

class MainApi():
    def get_product(self):
        r=requests.get("http://open.10086.cn/api/content/capabilityData").json()
        return r['message']
    def get_solution(self):
        r=requests.get("https://open.10086.cn/api/solution/level").json()
        return r['message']
    def get_bottom(self):
        r=requests.get("https://open.10086.cn/api/bottomLink").json()
        return r['message']