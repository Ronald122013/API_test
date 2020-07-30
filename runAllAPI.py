#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import HTMLTestRunner
import sys
import time
import os

from commonApp.suite import suite

#获取项目的绝对路径
path = os.path.split(os.path.realpath(__file__))[0]

#获取时间
now = time.strftime("%Y-%m-%d_%H%M%S")

#report路径拼接
file_name = path + '\\' + 'TestReport' + '\\' +'report' + '_' + now + '.html'

suite = suite()

if __name__ == "__main__":
    #with open(file_name,"wb+") as re:
    re = open(file_name,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=re, verbosity=2,title='测试报告', description='详情')
    runner.run(suite)
    re.close()
    

print("测试报告路径：" + ' ' + file_name)