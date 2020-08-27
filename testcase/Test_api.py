import json

import requests

from api.Mainui_api import MainApi
from CommLib.reporter import report_PASS,report_FAIL
from jsonschema import validate
from api.Admin import Admin
from api.Mycart_api import Mycart_api
from api.Order_api import Order_api
import allure


class Test_api():
    @allure.feature("测试产品接口")
    def test_productapi(self):
        mainapi=MainApi()
        if mainapi.get_product():
            report_PASS('产品接口巡检通过')
        else:
            report_FAIL('产品接口巡检失败')
    @allure.feature("测试解决方案接口")
    def test_solution(self):
        mainapi=MainApi()
        if mainapi.get_solution():
            report_PASS('解决方案接口巡检通过')
        else:
            report_FAIL('解决方案接口巡检失败')
    @allure.feature("测试底部接口")
    def test_bottom(self):
        mainapi = MainApi()
        if mainapi.get_bottom():
            report_PASS('底部接口巡检通过')
        else:
            report_FAIL('底部接口巡检失败')
    @allure.feature("编辑解决方案接口")
    def test_admin_solution(self):
        admin= Admin()
        if admin.edit_solution():
            report_PASS('编辑解决方案接口成功')
        else:
            report_FAIL('编辑解决方案接口失败')
    @allure.feature("测试加入购物车")
    def test_add_mycart(self):
        mycart = Mycart_api()
        if mycart.mycart_api()=='1':
            report_PASS("加入购物车成功")
        else:
            report_FAIL("加入购物车失败")
    @allure.feature("测试订单接口")
    def test_order(self):
        order_api = Order_api()
        if order_api.order_api():
            report_PASS("订单接口成功")
        else:
            report_FAIL("订单接口失败")
    @allure.feature("产品接口格式校验")
    def test_schema(self):
        r=requests.get("http://open.10086.cn/api/content/capabilityData",verify=False)
        schema=json.load(open("/Users/xinxiaoqiang/PycharmProjects/openStore/ApiData/list_schema.json"))
        validate(instance=r.json(),schema=schema)