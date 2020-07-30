#!/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest
import os

'''
from GoogsControl import goodsdetails
from LoginController import appRegisterForSmallB
from LoginController import toBRegister
from OrderController import orderSubmit
from PayController import orderPay
from PayController import sendWechatCoupon
from PayController import wechatAppletOrderPay
from PayController import wechatH5OederPay

def suite():
    suite = unittest.TestSuite()
    suite.addTest(goodsdetails.goodsdetails("test_goodsdetails"))
    suite.addTest(appRegisterForSmallB.appRegisterForSmallB("test_appRegisterForSmallB"))
    suite.addTest(toBRegister.toBRegister("test_toBRegister"))
    suite.addTest(orderSubmit.orderSubmit("test_orderSubmit"))
    suite.addTest(orderPay.orderPay("test_orderPay"))
    suite.addTest(sendWechatCoupon.sendWechatCoupon("test_sendWechatCoupon"))
    suite.addTest(wechatAppletOrderPay.wechatAppletOrderPay("test_wechatAppletOrderPay"))
    suite.addTest(wechatH5OederPay.wechatH5OederPay("test_wechatH5OederPay"))
    return suite

'''





import GoogsControl
import LoginController
import OrderController
import PayController


def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()      #用例加载器
    suite.addTest(loader.loadTestsFromModule(GoogsControl))  #通过模块加载
    suite.addTest(loader.loadTestsFromModule(LoginController))
    suite.addTest(loader.loadTestsFromModule(OrderController))
    suite.addTest(loader.loadTestsFromModule(PayController))
    return suite
    print('suite=',suite)


if __name__ == '__main__':
    suite()















#项目路径/测试模块路径，定位到上级APP_TEST目录
case_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) 


#def suite():
 #   suite = unittest.defaultTestLoader.discover(case_path,pattern="test*.py",top_level_dir=None)
  #  print(suite)
  #  return suite












