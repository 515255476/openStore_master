from time import sleep

import yaml
import requests


class BaseApi(object):
    def loadapi(self,op_path,key,**kwargs):
        file=open(op_path)
        po_data=yaml.safe_load(file)
        po_method=po_data[key]
        po_method[0]['re_method']
        re_method=po_method[0]['re_method']
        url=po_method[0]['url']
        verify=po_method[0]['verify']
        requests.packages.urllib3.disable_warnings()
        r = requests.request(method=re_method,url=url,verify=False).json()
        if r['message']=='获取成功':
            return True
        else:
            return False
if __name__ == '__main__':
    base=BaseApi()
    m=base.loadapi('../ApiData/Mainprocess.yaml','get_product')
    print(m)
