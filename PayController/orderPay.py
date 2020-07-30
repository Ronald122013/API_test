#调用支付
#!usr/bin/env python
# -*- coding:utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s- %(message)s')
# logging. disable(logging.CRITICAL)    # 禁用日志
logging.debug('>>>>>>Start of program<<<<<<')

import unittest
import json
import requests
import threading
import time
from assertpy import assert_that

from commonApp import getDomain as c 
from commonApp import getStatusCode as s
from commonApp import get_dict_key as getKey
from commonApp import getToken

domain = c.Get_Domain().Domain('156')
token_value = getToken()

class orderPay(unittest.TestCase):
    def setUp(self):
        #self.url = domain + '/toBRegister'
        #self.headers = {"Content-Type":"application/json;charset=UTF-8"}
        print(">>>>>>BEGIN toBRegister TEST<<<<<<")


    def test_orderPay(self):
        self.url = domain + '/toBRegister'
        self.headers = {"Content-Type":"application/json;charset=UTF-8",
                        "token":""
                        }
        self.headers["token"][""] = token_value           #写入token
        
        with open('./PayController/orderPay.json','wr',encoding='utf-8') as f:
            data = json.load(f)
        self.form = data

        #发送数据
        r = requests.post(self.url,json = self.form,headers = self.headers)

        #获取 response code
        code = s.getStatusCode(r)

        #获取 response.keys,当前只对response的key做校验
        with open('./LoginController/toBRegister_res.json','r',encoding='utf-8') as f:
            expected_dic = json.load(f)
        actual_dic = r.text
        expected_res_key = getKey(expected_dic)       #期望得到的key
        actual_res_key = getKey(actual_dic)           #实际返回的key
        
        #断言
        Judge = 0
        if code == 200 and expected_res_key == actual_res_key :
            Judge = 200
        assert_that(Judge).is_equal_to(200)

    #并发测试
    try:
        #计数器
        i=0
        #线程数
        taskd_num = 10
        print('*'*20 + "测试启动" + "*"*20)
        time1 = time.clock()
        while i < taskd_num :
            t = threading.Thread(target=orderPay().test_orderPay())
            t.start()
            i += 1
        time2 = time.clock()
        times = time2 - time1
        print("测试总耗时：",times)
    except Exception as e:
        print(e)





if __name__ == '__main__':
    #unittest.main()
    runTest = orderPay()
    runTest.test_orderPay()









logging.debug('>>>>>>End of program<<<<<<')