#!/usr/bin/env python
# -*- coding:utf-8 -*-
#通过账号密码登录接口获取实时token
import requests

import getDomain as c
domain = c.Get_Domain().Domain('156')

def getToken():
    url = domain + '/app_login'
    form = {
        "username":"13751753979",
        "password":"app123",
        "appUserTypeEnum":"B"
    }
    headers = {
        "Content-Type":"application/json;charset=UTF-8",
        "uuid":"",
        "sign":"",
    }
    r = requests.post(url = url,headers=headers,json=form)

    #调试用
    print("response",r.text)
    print('status_code=',r.status_code)

    #return (r.json()['data']['token'])



if __name__ == '__main__':
    token = getToken()
    