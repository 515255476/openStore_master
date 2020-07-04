from collections import OrderedDict

import requests
from urllib3 import encode_multipart_formdata
from api.Login_api import Login_api

class Mycart_api():

    def mycart_api(self):
        login_api = Login_api()
        XSRF_TOKEN=login_api.get_tokensession()[1]
        SESSION=login_api.login_api()
        params = OrderedDict([("ids", (None, '50'))
                              ])
        m = encode_multipart_formdata(params, boundary='----WebKitFormBoundaryy3AFbtauUKYgjE72')
        url="http://10.34.41.201/api/shoppingCart/add"
        headers = {'X-XSRF-TOKEN': XSRF_TOKEN, "Content-Type": m[1]}
        cookies = {'udata_account_300011876758': 'HqOhWYnjRefyf%2BQmt%2FotJkRZt1gQFLZVkrQgJWUcx2g%3D',
                   'userid_300011876758': '1591842631758504908',
                   'udata_s_300011876758': '1592551274606595345',
                   'XSRF-TOKEN': XSRF_TOKEN,
                   'SESSION': SESSION,
                   'WT_FPC': 'id=2d541b72c5782658f201591842631574:lv=1593698079126:ss=1593698079126'}
        r=requests.post(url=url, data=m[0], headers=headers, cookies=cookies,).text
        print(r)

if __name__ == '__main__':
    mycart=Mycart_api()
    mycart.mycart_api()