# coding:utf-8
import re

import requests
from collections import OrderedDict
import json
from urllib3 import encode_multipart_formdata


class Login_api():
    def GetMiddleStr(self,content, startStr, endStr):
        patternStr = r'%s(.+?)%s' % (startStr, endStr)
        p = re.compile(patternStr, re.IGNORECASE)
        m = re.match(p, content)
        if m:
            return m.group(1)
    def get_imagecode(self):
        r=requests.get(
            "http://10.34.41.201/api/account/imgCodeProducer?type=2")
        # print(r.headers['Set-Cookie'])
        return r.headers['Set-Cookie']
    def get_tokensession(self):
        content=Login_api.get_imagecode(self)
        XSRF_TOKEN = Login_api.GetMiddleStr(self,content, 'XSRF-TOKEN=', ';')
        startstr = 'XSRF-TOKEN=' + XSRF_TOKEN + '; Path=/, SESSION='
        SESSION = Login_api.GetMiddleStr(self,content, startstr, ';')
        return XSRF_TOKEN,SESSION
    def login_api(self):
        list=Login_api.get_tokensession(self)
        XSRF_TOKEN=list[0]
        SESSION=list[1]
        params = OrderedDict([("loginType",(None,'1')),
                              ("username", (None,
                                            'Jbcl3e1d7xOOHgrLxRzBlQk+NWTxxaiuSGdziwaflXRiyED7Hu6itPnJXhvwRO2BmKeXn1Sax9iTyEh6JyExeqcKczZhAmX3sNP+UhNf82v56WcyACDj2iNmWZP+fB5qYEW8iDcF/S9jHdZnJFqxAW++0OlcYqDsqPIY7ZFwI0U=')),
                              ("password", (None,
                                            'PuswN1cTaJ+CODOebXePfpNPCwoj+V+4HMivr6GHVzIcig8/wZeS1pwYA5TbZBDmhcnFn9F916Afu82Lpayz6AcTnvnp0Elt1rSsKO/gRp4FKyKpx600gcpHf5zlQalpwuIb3b7ISZEd7srfYUuGCZnV8fshgXGnfbGFveGy6j4=')),
                              ("img_code", (None, '123456')),
                              ("channel", (None, '001'))
                              ])
        m = encode_multipart_formdata(params, boundary='----WebKitFormBoundaryy3AFbtauUKYgjE72')
        url = "http://10.34.41.201/api/account/login"
        pro = {
            # 'https': 'https://open.10086.cn',
            'https': 'https://127.0.0.0:8888'
        }
        headers = {'X-XSRF-TOKEN': XSRF_TOKEN, "Content-Type": m[1]}
        cookies = {'udata_account_300011876758': 'HqOhWYnjRefyf%2BQmt%2FotJkRZt1gQFLZVkrQgJWUcx2g%3D',
                   'userid_300011876758':'1591842631758504908',
                   'udata_s_300011876758':'1592551274606595345',
                   'XSRF-TOKEN':XSRF_TOKEN,
                   'SESSION':SESSION,
                   'WT_FPC':'id=2d541b72c5782658f201591842631574:lv=1593698079126:ss=1593698079126'}

        r = requests.post(url=url, data=m[0], headers=headers, cookies=cookies, proxies=pro).headers
        SESSION=Login_api.GetMiddleStr(self,r['Set-Cookie'],'SESSION=',';')
        return SESSION
#
#
# test = Login_api()
# content=test.login_api()
# print(content)
# print(content)
# print(content)
# XSRF_TOKEN=test.GetMiddleStr(content,'XSRF-TOKEN=',';')
# startstr='XSRF-TOKEN='+XSRF_TOKEN+'; Path=/, SESSION='
# SESSION=test.GetMiddleStr(content,startstr,';')
# print(XSRF_TOKEN)
# print(SESSION)
# test.login_api(XSRF_TOKEN,SESSION)


