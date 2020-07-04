# coding:utf-8
import json
import os
import datetime
import pymysql
import time
import inspect
import platform
# sysstr = platform.system()
# if (sysstr =="Windows"):
#     #HOST = ''
#     HOST = '10.34.41.10' #if len(sys.argv)>=2 and sys.argv[1] == 'V' else '15.146.38.175'
# else:
#     HOST = '10.34.41.10'
HOST = '10.34.41.10'
#print  HOST
# if len(sys.argv) >= 3 and str(sys.argv[2]).startswith("TEST_") ==False:
#     HOST = '10.106.0.6'
# else:
#     HOST = '15.146.38.85'
PORT = 3306
USER = 'open_store_jf'
PASSWORD = 'Opensotre123!'
DB = 'hpeopendb'
CHARSET = 'utf8'

#################OPEN_UAT############




#根据用例名称从mysql数据库 TC_TESTDATA 表获取该用例的测试数据
def GET_TC_DATA(*arg) :
    s = inspect.stack()
    TC_Name = os.path.basename(s[1][1])
    if len(sys.argv) > 1 and sys.argv[1] !='V':
        str_envcode = sys.argv[1]
    else:
        str_envcode = 'S'
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset=CHARSET)
    except Exception as e:
        print('\033[1;41mGET_TC_DATA连接mysql数据库失败，测试结束；\033[0m' + str(e))
        return False
    cursor = conn.cursor()
    str_sql = "select tc_data from TC_TESTDATA where binary tc_name =%s and env_code =%s"
    #print str_sql
    cursor.execute(str_sql,(TC_Name,str_envcode))
    row_1 = cursor.fetchall()
    if len(row_1) == 0:
        cursor.close()
        conn.close()
        return False
    dataType = 'dic' if len(arg) == 0 else 'else'
    row_1 = json.loads(row_1[0][0]) if dataType == 'dic' else row_1[0][0].strip(arg[0]).split(arg[0])
    cursor.close()
    conn.close()
    return row_1

#print (JN_GET_TC_DATA('APP_FligthTest1') )
#根据参数名从mysql数据库 TC_TESTDATA 表获取公共环境配置信息
def JN_GET_Config_DATA(str_Param_NAME) :
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset=CHARSET)
    except Exception as e:
        print('\033[1;41mJN_GET_Config_DATA连接mysql数据库失败，测试结束；\033[0m' + str(e))
        return False
    cursor = conn.cursor()
    str_sql = "select ParaValue from Config where ParaName ='"+ str(str_Param_NAME)+"'"
    #print str_sql
    cursor.execute(str_sql)
    row_1 = cursor.fetchmany(1)
    if len(row_1) == 0:
        cursor.close()
        conn.close()
        return False
    row_1 = json.loads(row_1[0][0])
    cursor.close()
    conn.close()
    return row_1

# 从mysql数据库 TestSuite 表获取要运行的测试套
def LST_GET_TestSuite(str_envcode,BuildName):
    LST_Suite = []
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset=CHARSET)
    except Exception as e:
        print('\033[1;41mLST_GET_TestSuite连接mysql数据库失败，测试结束；\033[0m' + str(e))
        return False
    cursor = conn.cursor()
    if BuildName == '':
        str_sql = "select TsName,NotRunOn from TestSuite where IsUItest !='Y'"
    else:
        str_sql = "select TsName,NotRunOn from TestSuite WHERE BuildName like '%"+str(BuildName).strip()+"%' and IsUItest !='Y'"
    #print str_sql
    cursor.execute(str_sql)
    row_1 = cursor.fetchall()
    if len(row_1) == 0:
        cursor.close()
        conn.close()
        return False
    for i in range(0,len(row_1)):
        if str_envcode not in row_1[i][1]:
            LST_Suite.append(row_1[i][0])
    #row_1 = json.loads(row_1[0][0])
    cursor.close()
    conn.close()
    if len(LST_Suite) == 0:
        return False
    return LST_Suite

def LST_GET_TestSuiteForUItest(str_envcode,BuildName):
    LST_Suite = []
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset=CHARSET)
    except Exception as e:
        print('\033[1;41mLST_GET_TestSuite连接mysql数据库失败，测试结束；\033[0m' + str(e))
        return False
    cursor = conn.cursor()
    if BuildName == '':
        str_sql = "select TsName,NotRunOn from TestSuite where IsUItest ='Y'"
    else:
        str_sql = "select TsName,NotRunOn from TestSuite WHERE BuildName like '%"+str(BuildName).strip()+"%' and IsUItest ='Y'"
    #print str_sql
    cursor.execute(str_sql)
    row_1 = cursor.fetchall()
    if len(row_1) == 0:
        cursor.close()
        conn.close()
        return False
    for i in range(0,len(row_1)):
        if str_envcode not in row_1[i][1]:
            LST_Suite.append(row_1[i][0])
    #row_1 = json.loads(row_1[0][0])
    cursor.close()
    conn.close()
    if len(LST_Suite) == 0:
        return False
    return LST_Suite

# 从mysql数据库 TestCase 表获取要运行的测试用例集,返回列表形式，存储所有属于该测试套的测试用例路径
def LST_GET_TestCase(str_SuiteName,str_envcode):
    LST_Case = []
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset=CHARSET)
    except Exception as e:
        print('\033[1;41mLST_GET_TestCase连接mysql数据库失败，测试结束；\033[0m' + str(e))
        return False
    cursor = conn.cursor()
    str_sql = "select path,NotRunOn from TestCase where TestSuite = '"+str_SuiteName+"'"
    #print str_sql
    cursor.execute(str_sql)
    row_1 = cursor.fetchall()
    if len(row_1) == 0:
        cursor.close()
        conn.close()
        return False
    for i in range(0,len(row_1)):
        if str_envcode not in row_1[i][1]:
            LST_Case.append(row_1[i][0])
    #row_1 = json.loads(row_1[0][0])
    cursor.close()
    conn.close()
    if len(LST_Case) == 0:
        return False
    return LST_Case

#获取所有TC以及存储路径，字典形式
def TU_GET_AllTestCase():
    TU_Caselist = {}
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset=CHARSET)
    except Exception as e:
        print('\033[1;41mTU_GET_AllTestCase连接mysql数据库失败，测试结束；\033[0m' + str(e))
        return False
    cursor = conn.cursor()
    str_sql = "select TcName,path from TestCase"
    #print str_sql
    cursor.execute(str_sql)
    row_1 = cursor.fetchall()
    if len(row_1) == 0:
        cursor.close()
        conn.close()
        return False
    for i in range(0,len(row_1)):
        TU_Caselist[row_1[i][0]]=row_1[i][1]
    cursor.close()
    conn.close()
    if TU_Caselist == {}:
        return False
    return TU_Caselist



#获取测试用例的最后更新时间
def date_GetCaseLastTime(str_TcName):
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset=CHARSET)
    except Exception as e:
        print('BOOL_DeleteCaseFromDB连接mysql数据库失败，测试结束；' + str(e))
        return False
    cursor = conn.cursor()
    str_sql = "select lastUpdate from TestCase where binary TcName =%s"
    cursor.execute(str_sql,(str_TcName))
    row_1 = cursor.fetchone()
    cursor.close()
    conn.close()
    return row_1[0]

#检查特定用例是否已注册到数据库
def BOOL_CheckInDB(str_TcName):
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset=CHARSET)
    except Exception as e:
        print('BOOL_CheckInDB连接mysql数据库失败，测试结束；' + str(e))
        return False
    cursor = conn.cursor()
    str_sql = "select COUNT(1) from TestCase where binary TcName =%s"
    cursor.execute(str_sql,(str_TcName))
    row_1 = cursor.fetchone()
    if row_1[0] == 0:
        return False
    cursor.close()
    conn.close()
    return True



#将测试结果写入TestResult表
def BOOL_insertResult(str_TcName,result,msg,envcode,batchID):
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset=CHARSET)
    except Exception as e:
        print('\033[1;41mBOOL_insertCase连接mysql数据库失败，测试结束；\033[0m' + str(e))
        return False
    cursor = conn.cursor()
    str_sql_check = "select count(1) from TestResult where binary TcName = '"+str_TcName+ "' AND batchID = '"+batchID+"'"
    #print str_sql_check
    cursor.execute(str_sql_check)
    # if cursor.fetchone()[0] == 0:
    #     str_sql_IN = "insert into TestResult (TcName,result,msg,envcode,batchID) values('" + str_TcName + "'," + "'" + result + "'," +"'" + msg + "',"+"'" + envcode + "',"+"'" + batchID + "')"
    # else:
    #     str_sql_IN = "update TestResult set result ='" +result+"', msg = '"+ msg+"' where binary TcName = '"+str_TcName+ "' AND batchID = '"+batchID+"'"
    # str_sql_IN = "insert into TestResult (TcName,result,msg,envcode,batchID) values('" + str_TcName + "'," + "'" + result + "'," + "'" + msg + "'," + "'" + envcode + "'," + "'" + batchID + "')"
    #print str_sql
    str_sql_IN = "insert into TestResult (TcName,result,msg,envcode,batchID,createTime) values(%s,%s,%s,%s,%s,%s)"
    # print str_sql
    nowtime = str(datetime.datetime.now())
    cursor.execute(str_sql_IN, (str_TcName, result, msg, envcode, batchID, nowtime))
    conn.commit()
    cursor.close()
    conn.close()
    return True




#根据批次号和测试结果返回测试结果列表
def TU_resultList(batchID,result):
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset=CHARSET)
    except Exception as e:
        print('\033[1;41mTU_resultList连接mysql数据库失败，测试结束；\033[0m' + str(e))
        return False
    str_sql = "select TcName from TestResult where batchID = '"+ batchID+"'and result = '"+result+"'"
    cursor =conn.cursor()
    cursor.execute(str_sql)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# 将测试结果写入Local_TestLog表
def BOOL_insertLocalLog(str_TcName, msg, envcode, batchID,BIPCODE):
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset=CHARSET)
    except Exception as e:
        print('\033[1;41mBOOL_insertLocalLog连接mysql数据库失败，测试结束；\033[0m' + str(e))
        return False
    cursor = conn.cursor()
    nowtime = str(datetime.datetime.now())
    #str_sql_IN = "insert into Local_TestLog (TcName,logMessage,envcode,createTime,batchID) values('" + str_TcName + "'," + "'" + msg + "'," + "'" + envcode + "'," +"'" + nowtime + "',"+ "'" + batchID + "')"
    str_sql_IN = "insert into Local_TestLog (TcName,logMessage,envcode,createTime,batchID,BIPCODE) values(%s,%s,%s,%s,%s,%s)"
    #print str_sql_IN
    cursor.execute(str_sql_IN,(str_TcName,msg,envcode,nowtime,batchID,BIPCODE))
    conn.commit()
    cursor.close()
    conn.close()
    return True

# 将测试结果写入CI_TestLog表
def BOOL_insertCILog(str_TcName, msg, envcode, batchID,BIPCODE):
    try:
        conn = pymysql.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB, charset=CHARSET)
    except Exception as e:
        print('\033[1;41mBOOL_insertCILog连接mysql数据库失败，测试结束；\033[0m' + str(e))
        return False
    cursor = conn.cursor()
    nowtime = str(datetime.datetime.now())
    #str_sql_IN = "insert into CI_TestLog (TcName,logMessage,envcode,createTime,batchID) values('" + str_TcName + "'," + "'" + msg + "'," + "'" + envcode + "'," + "'" + nowtime + "'," + "'" + batchID + "')"
    str_sql_IN = "insert into CI_TestLog (TcName,logMessage,envcode,createTime,batchID,BIPCODE) values(%s,%s,%s,%s,%s,%s)"
    # print str_sql_IN
    cursor.execute(str_sql_IN, (str_TcName, msg, envcode, nowtime, batchID,BIPCODE))
    conn.commit()
    cursor.close()
    conn.close()
    return True
