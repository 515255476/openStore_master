#coding:utf-8

import json
import requests
from CommLib.reporter import report_PASS,report_FAIL

class Api_data():

    @classmethod
    def get_prodata(self):
        try:
            url = "https://open.10086.cn/api/content/capabilityData"
            headers = {'Content-Type': 'application/json;charset=UTF-8'}
            response = requests.get(url, headers=headers)
            # print response.json()
            data = response.text
            # print data
            j = json.loads(data)
            body = j["body"]
            pro_data=[]
            for i in body:
                for j in i["children"]:
                    for m in j["children"]:
                        pro_data.append(m["label"])
            return pro_data
        except Exception as e:
            print("无法获取能力数据")
            report_FAIL("无法获取能力数据")

    @classmethod
    def get_soludata(self):
        try:
            url = "https://open.10086.cn/api/solution/level"
            headers = {'Content-Type': 'application/json;charset=UTF-8'}
            response = requests.get(url, headers=headers)
            data = response.text
            print(data)
            j = json.loads(data)
            body = j["body"]
            solu_data=[]
            for i in body:
                for j in i["children"]:
                    solu_data.append(j["label"])
            return solu_data
        except Exception as e:
            print("无法获取解决方案数据")
            report_FAIL("无法获取解决方案数据")


