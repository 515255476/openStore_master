import pystache
import pytest
import requests

solution_title=['测试1','测试2','测试3','测试4']
class Admin():
    @pytest.mark.parametrize('solution_title',solution_title)
    def edit_solution(self):
        url='http://111.198.190.250:33252/open-admin/solution/editSolution'
        pro={ 'https': 'https://127.0.0.0:8888'}
        cookies = {'SESSION': 'YTlhNmRjZjItMzNkZS00ZTM0LWE4MjMtNjgwYjcxNTM4Njlk',
                   'udata_account_300011876758': 'pydvv%2FokEcukHhb2dix%2BycOqLySgAKnkX1e7VzjAIuM%3D',
                   'userid_300011876758': '1591965590516811637',
                   'XSRF-TOKEN': 'fb913eaf-c900-44f4-8ae0-a128c996a049',
                   'udata_s_300011876758': '1593999911145763650',
                   'SESSION': 'ZGNjNThmOTMtMzFhMi00NTExLWE4YjAtOGZjOWI1YzY0ODYx',
                   'WT_FPC':'id=286470f9f509321ef611594262960679:lv=1596158511330:ss=1596158284601'}
        templete=''.join(open('/Users/xinxiaoqiang/PycharmProjects/openStore/ApiData/solution.json').readlines())
        json=pystache.render(templete,{'tilte': solution_title})
        r = requests.post(url=url,  cookies=cookies, proxies=pro,json=json).json()
        if r['message']=='修改成功':
            return True
        else:
            return False