# -*- coding: utf-8 -*-
# 本模块负责测试结果记录
# 创建于 2018.5.9， 作者帅健
import json
import logging
import sys
import os
import time

from CommLib import DB_msql
import inspect

# reload(sys)
# sys.setdefaultencoding('utf-8')
logging.basicConfig(level=logging.INFO)

def report_PASS(msg):
    s = inspect.stack()
    envcode = 'S'
    bathID = ''
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    logging.info(msg)

    if 1==1:
        DB_msql.BOOL_insertResult(os.path.basename(s[1][1]), 'PASS', msg, envcode, bathID)
        print(os.path.basename(s[1][1]) + " " + msg)
    else:
        pass
def report_FAIL(msg):
    createTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    s = inspect.stack()
    envcode = 'S'
    bathID = ''
    logging.info(msg)
    DB_msql.BOOL_insertResult(os.path.basename(s[1][1]), 'FAIL', msg, envcode, bathID)



if __name__=='__main__':
    print(report_PASS('未能打开浏览器，PC精品专区巡检忽略'))
