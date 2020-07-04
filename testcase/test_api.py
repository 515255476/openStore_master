from api.Mainprocess_api import MainApi
from CommLib.reporter import report_PASS,report_FAIL

class Test_api():
    def test_productapi(self):
        mainapi=MainApi()
        if mainapi.get_product()=="获取成功":
            report_PASS('产品接口巡检通过')
        else:
            report_FAIL('产品接口巡检失败')
    def test_solution(self):
        mainapi=MainApi()
        if mainapi.get_solution()=="获取成功":
            report_PASS('解决方案接口巡检通过')
        else:
            report_FAIL('解决方案接口巡检失败')
    def test_bottom(self):
        mainapi = MainApi()
        print(mainapi.get_bottom())
        if mainapi.get_bottom()=="操作成功":
            report_PASS('底部接口巡检通过')
        else:
            report_FAIL('底部接口巡检失败')