#!/usr/bin/python3
import hashlib
from data.get_data import GetData
import time
import uuid
import base.md5_32
import random
#该方法只针对无依赖接口计算MD5值
#api签名：每个接口都带?apikey={{apikey}}&timestamp={{timestamp}}&nonce={{nonce}}&sign={{sign}}，其中时间戳timestamp为秒时间戳；这个为MD5签名
# （newSSign = "apikey=" + apikey + "&" + "apisecret=" + apisecret + "&" + sign),其中sign为所有params和body升序）；sign += key + "=" + paramSorted[key] + "&"
#print(time.time())
class sing_md5:
    def __init__(self):

        self.data = GetData()
        # self.send_email = SendEmail()

    def newsign(self,row):
        request_data = self.data.get_request_data(row)
        #request_data = row
        params=self.data.get_params(row)
        timestamp1=str(time.time())[0:10]
        apikey="fendaitripjota2020"
        apisecret="93d31fc184436a5ce61ab74363260e26c48cd5c4"
        #once值设置为uuid20位
        #nonce=str(uuid.uuid4()).replace("-","")[:20]
        nonce="123123123123"


        if request_data!=None and params!=None:
            json1 = request_data.update(params)
            json1["timestamp"]=timestamp1
            json1["nonce"]=nonce
            newjson1 = sorted(json1)
            sign = ""
            for x in newjson1:
                if type(request_data[x]) == type("abc"):
                    sign += x + "=" + request_data[x] + "&"
                else:
                    sign += x + "=" + str(request_data[x]) + "&"
            newSSign = "apikey=" + apikey + "&" + "apisecret=" + apisecret + "&" + sign
            newSign = newSSign[:-1]
            #md5=hashlib.md5(newSign.encode('utf-8')).hexdigest().upper()
            md5 = base.md5_32.md5(newSign.encode(encoding="utf-8"))
            url0 = "?"+"apikey=" + apikey + "&" + "timestamp=" + timestamp1 + "&" + "nonce=" + nonce + "&" + "sign=" + md5
            return url0
        elif request_data==None and params!=None:

            params["timestamp"] = timestamp1
            params["nonce"] = nonce
            newjson1 = sorted(params)
            sign = ""
            for x in newjson1:
                #sign += x + "=" + params[x] + "&"
                if type(params[x]) == type("abc"):
                    sign += x + "=" + params[x] + "&"
                else:
                    sign += x + "=" + str(params[x]) + "&"
            newSSign = "apikey=" + apikey + "&" + "apisecret=" + apisecret + "&" + sign
            newSign = newSSign[:-1]
            #md5 = hashlib.md5(newSign.encode('utf-8')).hexdigest().upper()
            md5 = base.md5_32.md5(newSign.encode(encoding="utf-8"))
            url0 = "?" + "apikey=" + apikey + "&" + "timestamp=" + timestamp1 + "&" + "nonce=" + nonce + "&" + "sign=" + md5
            return url0
        elif request_data!=None and params==None:
            #print(request_data,1123)
            request_data["timestamp"] = timestamp1
            request_data["nonce"] = nonce
            newjson1 = sorted(request_data)
            sign = ""
            for x in newjson1:
                if type(request_data[x]) == type("abc"):
                    sign += x + "=" + request_data[x] + "&"
                else:
                    sign += x + "=" + str(request_data[x]) + "&"

            newSSign = "apikey=" + apikey + "&" + "apisecret=" + apisecret + "&" + sign
            newSign = newSSign[:-1]
            #print(123, newSign)
            #md5 = hashlib.md5(newSign.encode('utf-8')).hexdigest().upper()
            md5 = base.md5_32.md5(newSign.encode(encoding="utf-8"))
            url0 = "?" + "apikey=" + apikey + "&" + "timestamp=" + timestamp1 + "&" + "nonce=" + nonce + "&" + "sign=" + md5
            return url0
        elif request_data==None and params==None:
            newSSign = "apikey=" + apikey + "&" + "apisecret=" + apisecret + "&" + "nonce=" + nonce+"&" + "timestamp=" + timestamp1
            #print(newSSign)
            md5 = base.md5_32.md5(newSSign.encode(encoding="utf-8"))
            url0 = "?" + "apikey=" + apikey + "&" + "timestamp=" + timestamp1 + "&" + "nonce=" + nonce + "&" + "sign=" + md5
            return url0
