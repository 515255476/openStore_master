# coding:utf-8
import re

import requests
from collections import OrderedDict
import json
from urllib3 import encode_multipart_formdata

from api.Login_api import Login_api


class Order_api():
    def order_api(self):
        login_api = Login_api()
        XSRF_TOKEN = login_api.get_tokensession()[1]
        SESSION = login_api.login_api()
        params = OrderedDict([("mail", (None, '18004261646@163.com')),
                              ("name", (None,
                                            '王洋')),
                              ("company", (None,
                                            'hpe')),
                              ("img_code", (None, '123456')),
                              ("sourceType", (None, '001')),
                              ("ids",(None,'50'))
                              ])
        m = encode_multipart_formdata(params, boundary='----WebKitFormBoundaryy3AFbtauUKYgjE72')
        url = "http://10.34.41.201/api/order"
        headers = {'X-XSRF-TOKEN': XSRF_TOKEN, "Content-Type": m[1]}
        cookies = {'udata_account_300011876758': 'HqOhWYnjRefyf%2BQmt%2FotJkRZt1gQFLZVkrQgJWUcx2g%3D',
                   'userid_300011876758': '1591842631758504908',
                   'udata_s_300011876758': '1592551274606595345',
                   'XSRF-TOKEN': XSRF_TOKEN,
                   'SESSION': SESSION,
                   'WT_FPC': 'id=2d541b72c5782658f201591842631574:lv=1593698079126:ss=1593698079126'}
        r=requests.post(url=url, data=m[0], headers=headers, cookies=cookies).text
        print(r)
order_api=Order_api()
order_api.order_api()
