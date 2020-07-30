#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Get_Domain():
    def Domain(self, number):
        self.number = number
        #156测试环境
        if self.number == "156":
            domain = "http://ec2-52-83-156-42.cn-northwest-1.compute.amazonaws.com.cn:30001/app"
        #类生产环境
        elif self.number == 'uat':
            domain = 'https://gmms-uat.galanz.com'
        #正式环境
        elif self.number == 'frontend':
            domain = 'https://gmms.galanz.com/frontend'
        else:
            print("Plz input valid url domain!!!")
        return domain