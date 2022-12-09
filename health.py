#!/usr/bin/python3
from base.runmethon import runmethon
import requests
import json
run_method = runmethon()
def code(request_data):
    method='POST'
    url="http://192.168.75.242:9002/api/resource/params"
    request_data=request_data
    herders = {'content-type': 'application/json;charset=utf-8',
               'Accept': 'application/json;charset=utf-8'
               }
    res= run_method.run_main(method, url, request_data, herders)
    #print(111,res)
    re1=res["retstring"]["params"]
    print(222,re1)
    return re1
def gettoken(params):
    method = 'POST'
    params1=params
    #url = "http://192.168.75.242:9001/api/register"
    url = "http://192.168.75.242:9001/api/account/login"
    request_data={
    "params":params1
}
    herders = {'content-type': 'application/json;charset=utf-8',
               'Accept': 'application/json;charset=utf-8'
               }
    res = run_method.run_main(method, url, request_data, herders)
    #print(333,res)
    return res["retstring"]["token"]
login_data={
    "platformid":"FDHP001",
    "account":"13691699127",
    "password":"123456",
    "channelid":"4564617417928562564",
    "appid":"20125"
}
herders = {'content-type': 'application/json;charset=utf-8',
               'Accept': 'application/json;charset=utf-8'
               }

token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2Njg3NTI4ODQsIm5iZiI6MTY2ODc1Mjg4NCwiZXhwIjoxNjY5MzU3Njg0LCJkYXRhIjp7InBsYXRmb3JtaWQiOiIyMDEyNSIsInVzZXJpZCI6IkhQMDAxYWViOWZhMSJ9fQ.gxCXDatxMPd4FSnVg9IqLZCYr0eTpiYArwVEaM-CaGM"
'''
#血氧概要上传
summget_save={
    "platformid":"FDHP001",
    "appid":"20125",
    "userid":"HP001aeb9fa1",
    "data":[
         {
            "date":"2021-08-25",
            "timestamp":"1629648000",
            "mac":"01-80-C2-00-00-01",
            "hight":"10",
            "low":"64",
            "avg":"75"
        }
    ]
}
params=code(summget_save)
#print(444,params)
url="http://192.168.75.242:9002/api/spo2/summary/save"
request_data1={
    "token":token,
    "params":params
}
res = run_method.run_main("POST", url, request_data1, herders)
print(params,res)
#获取血氧概要
summget_data1={
    "platformid":"FDHP001",
     "appid":"20125",
    "userid":"HP001aeb9fa1",
     "begin":"2020-07-25"
}
params=code(summget_data1)
#print(444,params)
#获取token
#token=gettoken(params)
url="http://192.168.75.242:9002/api/spo2/summary/get"
request_data1={
    "token":token,
    "params":params
}
res = run_method.run_main("POST", url, request_data1, herders)
print(params,res)

#获取血氧明细
summget_data1={
    "platformid":"FDHP001",
     "appid":"20125",
    "userid":"HP001aeb9fa1",
     "start_time":"2020-07-25",
      "end_time":"2022-11-19"
}
params=code(summget_data1)
#print(444,params)
#获取token
#token=gettoken(params)
url="http://192.168.75.242:9002/api/spo2/detail/get"
request_data1={
    "token":token,
    "params":params
}
res = run_method.run_main("POST", url, request_data1, herders)
print("获取血氧明细",res)

#获取血氧数据统计信息（日、周、月、年）
summget_data1={
    "platformid":"FDHP001",
     "appid":"20125",
    "userid":"HP001aeb9fa1",
     "by":"month",
     "date":"2021-08-25",
      "end_date":"2022-11-19"
}
params=code(summget_data1)
#print(444,params)
#获取token
#token=gettoken(params)
url="http://192.168.75.242:9002/api/spo2/statistics"
request_data1={
    "token":token,
    "params":params
}
res = run_method.run_main("POST", url, request_data1, herders)
print("获取血氧数据统计信息（日、周、月、年）",res)

#主页相关接口
#用户卡片编辑
card_data={
    "platformid":"FDHP001",
     "appid":"20125",
    "userid":"HP001aeb9fa1",
    "data":"HP001aeb9fa1"
}
params=code(card_data)
#print(444,params)
#获取token
#token=gettoken(params)
url="http://192.168.75.242:9002/api/home/card/save"
request_data1={
    "token":token,
    "params":params
}
res = run_method.run_main("POST", url, request_data1, herders)
print("用户卡片编辑",res)

#用户卡片获取
card_data={
    "platformid":"FDHP001",
     "appid":"20125",
    "userid":"HP001aeb9fa1"
}
params=code(card_data)
#print(444,params)
#获取token
#token=gettoken(params)
url="http://192.168.75.242:9002/api/home/card/"
request_data1={
    "token":token,
    "params":params
}
res = run_method.run_main("POST", url, request_data1, herders)
print("用户卡片获取",res)

#产品相关接口
#增加产品接口
addproduct_data={
    "platformid":"FDHP001",
     "appid":"20125",
    "userid":"HP001aeb9fa1",
     "type":1,
    "name":"智能手环",
    "logo":"test",
    "info":"FD188产品介绍",
    "myorder":12
}
params=code(addproduct_data)
#print(444,params)
#获取token
#token=gettoken(params)
url="http://192.168.75.242:9002/api/products/save"
request_data1={
    "token":token,
    "params":params
}
res = run_method.run_main("POST", url, request_data1, herders)
print("增加产品接口",res)

#获取产品列表详情接口
productlist_data={
    "platformid":"FDHP001",
     "appid":"20125",
    "userid":"HP001aeb9fa1"
}
params=code(productlist_data)
#print(444,params)
#获取token
#token=gettoken(params)
url="http://192.168.75.242:9002/api/products/get"
request_data1={
    "token":token,
    "params":params
}
res = run_method.run_main("POST", url, request_data1, herders)
print("获取产品列表详情接口",res)

#压力相关
#压力明细数据上传
presdetail_data={
        "data":[
             {
                "pres_value":1,
                "time":1668761600,
                "mac":"01-80-C2-00-00-01"
            },
{
                "pres_value":2,
                "time":1668761900,
                "mac":"01-80-C2-00-00-01"
            }
        ]
    }
params=code(presdetail_data)
#print(444,params)
#获取token
#token=gettoken(params)
url="http://192.168.75.242:9002/api/pres/detail/save"
request_data1={
    "token":token,
    "params":params
}
res = run_method.run_main("POST", url, request_data1, herders)
print("压力明细数据上传122222",res)
#压力明细数据获取
presdetail_get={
                "start_time":"2021-08-23",
                "mac":"01-80-C2-00-00-01"
    }
params=code(presdetail_get)
#print(444,params)
#获取token
#token=gettoken(params)
url="http://192.168.75.242:9002/api/pres/detail/get"
request_data1={
    "token":token,
    "params":params
}
res = run_method.run_main("POST", url, request_data1, herders)
print("压力明细数据获取",res)

#压力概要数据上传
pressummarydata={
                "data":[
                    {
                "pres_avg":90,
                "date":1668960000,
                "mac":"01-80-C2-00-00-01"
                    },
{
                 "pres_avg":95,
                "date":1668873600,
                "mac":"01-80-C2-00-00-01"
                    }
                ]

    }
params=code(pressummarydata)
#print(444,params)
#获取token
#token=gettoken(params)
url="http://192.168.75.242:9002/api/pres/summary/save"
request_data1={
    "token":token,
    "params":params
}
res = run_method.run_main("POST", url, request_data1, herders)
print("压力概要数据上传",res)

#压力概要数据获取
pressummarydata={
            "start_time":"2019-08-23",
            "mac":"01-80-C2-00-00-01"}
params=code(pressummarydata)
#print(444,params)
#获取token
#token=gettoken(params)
url="http://192.168.75.242:9002/api/pres/summary/get"
request_data1={
    "token":token,
    "params":params
}
res = run_method.run_main("POST", url, request_data1, herders)
print("压力概要数据获取",res)

#获取压力数据统计信息（日、周、月、年）
pressummarydata={
            "by":"month",
            "date":"2021-08-16",
             "end_date":"2022-12-16"}
params=code(pressummarydata)
#print(444,params)
#获取token
#token=gettoken(params)
url="http://192.168.75.242:9002/api/pres/statistics"
request_data1={
    "token":token,
    "params":params
}
res = run_method.run_main("POST", url, request_data1, herders)
print("获取压力数据统计信息（日、周、月、年）",res)

#周月年报
'''



