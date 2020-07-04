# coding:utf-8
import logging

import pytest

from CommLib.reporter import report_PASS,report_FAIL
from Data.Api_data import Api_data
from page.BasePage import BasePage
from page.H5LoginPage import H5LoginPage
from page.H5MainPage import H5MainPage
from page.WebLoginPage import LoginPage
from page.WebMainPage import MainPage
from testcase.BaseTestCase import BaseTestCase

product_data=['模板短信','移动认证']
solution_data=['家庭智能连接']
# product_data=Api_data.get_prodata()
# solution_data=Api_data.get_soludata()
# product_data=['模板短信','中间号','挂机彩信','QoS加速','拨打验证','视频短信','语音通知/验证码','语音会议','点击拨号','来/去电身份提示','移动认证','资金归集','和包支付能力','AndLink','中移和物','OneNET视频能力','物联网应用开发','物联卡管理','信用服务能力','地图搜索导航SDK','URI地图能力','统一地图JSAPI能力','智能终端定位能力','AIRITA','中移舆情','智能问答（知了）','大云搜索引擎','中移商情','语音识别处理','视频云点播/直播','云空间','中移云客服','选号入网','宽带办理','基本业务订购','萤火·魔方','飞书必达消息推送平台','互联网消息推送','互联网广告平台']
# solution_data=['公车管家','O2O中间号','政务行业方案','电商一点对接','在线教育','智能语音云','视频云点播','“云+”视频','行业“视频+”','家庭智能连接','人员管家','二次号校验','本机一键登录','共享设备管理','智慧电动车','智能水表系统','物联卡状态服务','物联卡流量服务','和包贷','和包资金归集','和包支付','出入库数字化','运配数字化','冷链数字化','签收数字化','物流通知','酒店快速入住','免押骑行','信用购机']
h5_product=[('https://open.10086.cn/mobile/#/capability/info/4',"模板短信")]
h5_solution=[('https://open.10086.cn/mobile/#/solution/info/72',"O2O中间号")]

# logger = logging.getLogger('mylogger')
# logger.setLevel(logging.DEBUG)
# ch = logging.StreamHandler()
# formatter = logging.Formatter('[%(asctime)s][%(filename)s][line: %(lineno)d][%(levelname)s] ## %(message)s')
# ch.setFormatter(formatter)
# logger.addHandler(ch)

class Test_webhomepage(BaseTestCase):

    ##########################################################初始化准备
    # ############################################################

    @classmethod
    def setup_class(cls):
        # logger.info("初始化准备")
        basepage=BasePage()
        basepage.open_url("https://open.10086.cn")

    def test_webmainpage(self):
        mainpage = MainPage()
        if mainpage.mainpagecheck()==True:
            report_PASS('web首页巡检通过')
        else:
            report_FAIL('web首页巡检失败')

    ########################################################web产品页测试############################################################
    @pytest.mark.parametrize("product", product_data)
    def test_webgopro(self,product):
        # logger.info("测试web能力产品页面")
        mainpage = MainPage()
        if mainpage.gotoproduct(product)==True:
            report_PASS(product + '能力页面巡检通过')
        else:
            report_FAIL(product + '能力页面巡检失败')


    ########################################################web解决方案页测试############################################################
    @pytest.mark.parametrize("solution", solution_data)
    def test_webgosolu(self,solution):
        # logging.info("测试web解决方案页面")

        mainpage = MainPage()
        if mainpage.gotosolution(solution) == True:
            report_PASS(solution + '解决方案页面巡检通过')
        else:
            report_FAIL(solution + '解决方案页面巡检失败')


    #########################################################web登录页测试############################################################
    def test_weblogin(self):
        # logger.info("测试web登录页面")
        loginpage=LoginPage()
        if loginpage.gotologinpage()==True:
            report_PASS('web登录页面巡检通过')
        else:
            report_FAIL('web登录页面巡检失败')

    #########################################################h5能力页测试############################################################
    @pytest.mark.parametrize("url,product", h5_product)
    def test_h5gopro(self, url, product):
        # logger.info("测试h5能力产品页面")
        h5mainpage = H5MainPage()
        if h5mainpage.goto_H5product(url, product) == True:
            report_PASS('H5' + product+ '能力页面巡检通过')
        else:
            report_FAIL('H5' + product + '能力页面巡检失败')

    #########################################################h5解决方案页测试############################################################
    @pytest.mark.parametrize("url,solution", h5_solution)
    def test_h5gosolu(self, url, solution):
        # logger.info("测试web解决方案页面")
        h5mainpage = H5MainPage()
        if h5mainpage.goto_H5solution(url, solution) == True:
            report_PASS('H5' + solution + '解决方案页面巡检通过')
        else:
            report_FAIL('H5' + solution + '解决方案页面巡检失败')

    #########################################################h5登录页测试############################################################
    def test_h5login(self):
        # logger.info("测试web登录页面")
        h5loginpage = H5LoginPage()
        if h5loginpage.gotologinpage() == True:
            report_PASS('H5登录页面巡检通过')
        else:
            report_FAIL('H5登录页面巡检失败')
    def test_h5mainpage(self):
        # logger.info("测试web登录页面")
        h5mainpage = H5MainPage()
        if h5mainpage.gotoh5mainpage() == True:
            report_PASS('H5首页巡检通过')
        else:
            report_FAIL('H5首页巡检失败')

    #########################################################关闭浏览器############################################################
    @classmethod
    def teardown_class(cls):
        # logger.info("关闭浏览器")
        basepage = BasePage()
        basepage.quitBrowser()
#


if __name__ == '__main__':
    pytest.main(["-s","Test_homepage.py","-n=3"])
    # "s", "--browser=chrome",


