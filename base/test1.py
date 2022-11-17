#!/usr/bin/python3
import json
import time
from aip import AipOcr
import requests
import re
from selenium import webdriver
from PIL import ImageGrab
#本方法实现通用文字识别
#由于验证码底图原因，识别验证码准确率低。无法使用自动
class basicGeneralUrl:
    def post(self):

        """ 你的 APPID AK SK """
        APP_ID = '17542401'
        API_KEY = 'FAs0yQLEfaL9i14nbKVATWT1'
        SECRET_KEY = 'mYuqi3iXpur1K6ypR3dKzTFroq2LKe7D '
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        for i in range(1,2):
            """ 读取图片 """
            def get_file_content(filePath):
                with open(filePath, 'rb') as fp:
                    return fp.read()
            #image=get_file_content(r'G:\1\\' + str(i) + '.jpg')
            url="http://192.168.75.25:8090/fiota/v1/sys/randomImage/123456"
            herders = {'content-type': 'application/json;charset=utf-8',
                       'Accept': 'application/json;charset=utf-8'
                       }
            result1 = requests.get(url)
            url1=(re.sub(r"=data:image.*","=",str(result1.json()["result"])))
            driver = webdriver.Chrome()
            # 设置窗口最大化
            driver.maximize_window()
            # 访问被测网页
            driver.get(url1)
            time.sleep(10)
            bbox = (580, 350, 780, 550)
            im = ImageGrab.grab(bbox)

            # 参数 保存截图文件的路径
            im.save('as.png')
            driver.quit()
            """ 调用通用文字识别, 图片参数为本地图片 """
            #result=client.basicGeneral(image)
            image = get_file_content(r'D:\python\python36-64\project\TWS-API\base\as.png')
            tic=time.clock()
            """ 如果有可选参数 """
            options = {}
            options["language_type"] = "CHN_ENG"
            options["detect_direction"] = "true"
            options["detect_language"] = "true"
            options["probability"] = "true"
            """  带参数调用通用文字识别, 图片参数为本地图片  """
            result = client.basicGeneral(image)
            try:
                list1 = result["words_result"]
                for x1 in list1:
                    print(x1)
            except:
                pass
            #print(result)
            #print(result1.json()["result"])
            #return url1
for x in range(1,10):
    ss = basicGeneralUrl()
    print(ss.post())


