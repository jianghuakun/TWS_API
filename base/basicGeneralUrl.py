#!/usr/bin/python3
import json
import time
import requests
from aip import AipOcr
#本方法实现通用文字识别
class basicGeneralUrl:
    """ 你的 APPID AK SK """
    APP_ID = '17542401'
    API_KEY = 'FAs0yQLEfaL9i14nbKVATWT1'
    SECRET_KEY = 'mYuqi3iXpur1K6ypR3dKzTFroq2LKe7D '
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    url1="http://192.168.75.25:8090/fiota/v1/sys/randomImage/123456"
    herders={'content-type':'application/json;charset=utf-8',
          'Accept':'application/json;charset=utf-8'
          }
    result1=requests.get(url1,herders=herders)
    print(result1.json())
    for i in range(1, 3):
        """ 读取图片 """
        def get_file_content(filePath):
            with open(filePath, 'rb') as fp:
                return fp.read()
        url = "https//www.x.com/sample.jpg"
        """ 调用通用文字识别, 图片参数为本地图片 """
        result = client.basicGeneral(url)





