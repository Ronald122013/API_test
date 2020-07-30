#!usr/bin/env python
# -*- coding:utf-8 -*-

import logging
logging.basicConfig(level=logging.DEBUG,format=' %(asctime)s - %(levelname)s- %(message)s')
# logging. disable(logging.CRITICAL)    # 禁用日志
logging.debug('>>>>>>Start of program<<<<<<')

import unittest
import json
import requests
from assertpy import assert_that

from commonApp import getDomain as c 
from commonApp import getStatusCode as s

domain = c.Get_Domain().Domain('156')

class sendWechatCoupon(unittest.TestCase):
    def setUp(self):
        #self.url = domain + '/toBRegister'
        #self.headers = {"Content-Type":"application/json;charset=UTF-8"}
        print(">>>>>>BEGIN toBRegister TEST<<<<<<")


    def test_sendWechatCoupon(self):
        self.url = domain + '/toBRegister'
        self.headers = {"Content-Type":"application/json;charset=UTF-8"}
        with open('./PayController/sendWechatCoupon.json','r',encoding='utf-8') as f:
            data = json.load(f)
        self.form = data
        #print(data)   #调试用

        #开始发数据
        r = requests.post(self.url,json = self.form,headers = self.headers)
        print(r.text)                               #打印返回参数
        print('接口响应时间：',r.elapsed.total_seconds())     #打印接口响应时间
        null = None                                 #兼容
        dic = eval(r.text)                          #str转化为dict
        code = dic["code"]                          #提取status里面的code值
        s.getStatusCode(code)                  #打印code值
        try:
            assert_that(code).is_equal_to(200)      #当前值判断接口返回状态
        except AssertionError as e:
            raise AssertionError(e)


if __name__ == '__main__':
    #unittest.main()
    runTest = sendWechatCoupon()
    runTest.test_sendWechatCoupon()









logging.debug('>>>>>>End of program<<<<<<')