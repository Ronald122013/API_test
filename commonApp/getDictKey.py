#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

#将json转化为字典
#with open('./LoginController/text01.json','r',encoding='utf-8') as f:
    #dic = json.load(f)

#格式转换
null = None               
true = True
false = False

#获取字典的key，并检测key的类型，如果key是dict()，则继续获取嵌套的key
lis = []
def get_dict_Key(dic):
    for i in dic.keys():
        data = dic[i]               #遍历每一项value                                    
        if isinstance(data,dict):   #如果data属于dict类型，进行回归      
            get_dict_Key(data)
        elif isinstance(data,list):  #处理嵌套列表
            get_dict_Key(dict(data))
        lis.append(i)               #获取key
    return(sorted(lis))             #排个序



if __name__ == '__main__':
    lis_new = get_dict_Key(dic)
    print(lis_new)




