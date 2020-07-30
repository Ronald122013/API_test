#!/usr/bin/env python
# -*- coding:utf-8 -*-

def getStatusCode(return_file):

    #格式转换
    null = None
    true = True
    false = False

    #打印response
    print("response",return_file.text)  

    #打印接口响应时间                            
    print('接口响应时间：',return_file.elapsed.total_seconds())     
    
    #打印接口返回code
    status_code = return_file.status_code
    print('接口状态码: status_code =',status_code)

    #从返回的数据中提取响应code
    dic = eval(return_file.text)
    code = dic["code"]

    #打印code的实际含义
    if code == 200 :
        print("response status = 200   ok")
    elif code == 201 :
        print("response status = 201   Created")
    elif code == 401 :
        print("response status = 401   Unauthorized")
    elif code == 403 :
        print("response statue = 403   Forbidden")
    elif code == 404 :
        print("response status = 404   Not Found")
    elif code == 500 :
        print("response statue = 500   Internal Server error")
    elif code == 503 :
        print("response status = 503   Server Unavailable")
    elif code == 504 :
        print("response status = 504   Gateway Timeout")
    else:
        print("response status =",code)
    
    return (code)

    

