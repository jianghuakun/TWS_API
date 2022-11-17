#!/usr/bin/python3
import hashlib
from data.get_data import GetData
import time
import uuid
import base.md5_32
import random
#该方法对依赖接口，通过更换后的请求重新计算sign
#api签名：每个接口都带?apikey={{apikey}}&timestamp={{timestamp}}&nonce={{nonce}}&sign={{sign}}，其中时间戳timestamp为秒时间戳；这个为MD5签名
# （newSSign = "apikey=" + apikey + "&" + "apisecret=" + apisecret + "&" + sign),其中sign为所有params和body升序）；sign += key + "=" + paramSorted[key] + "&"
#print(time.time())
class md5_depend:
    def __init__(self):

        self.data = GetData()
        # self.send_email = SendEmail()

    def sign_depend(self,request_data_new,params_new):
        request_data = request_data_new
        #print("md5_depend",request_data)
        #request_data = row
        params=params_new
        timestamp1=str(time.time())[0:10]
        apikey="fendaitripjota2020"
        apisecret="93d31fc184436a5ce61ab74363260e26c48cd5c4"
        #once值设置为uuid20位
        #nonce=str(uuid.uuid4()).replace("-","")[:20]
        nonce="123123123123"


        if request_data!=None and params!=None:
            base_dict = {"timestamp": timestamp1, "nonce": nonce}
            #print(34521,base_dict)
            base_dict.update(request_data)
            #print(34522,base_dict)
            base_dict.update(params)
            #print(34523,base_dict)
            #json1 = request_data.update(params)
            #json1["timestamp"]=timestamp1
            #json1["nonce"]=nonce
            newjson1 = sorted(base_dict)
            sign = ""
            for x in newjson1:
                #print(x,request_data[x])
                if type(base_dict[x]) == type("abc"):
                    sign += x + "=" + base_dict[x] + "&"
                else:
                    sign += x + "=" + str(base_dict[x]) + "&"
            newSSign = "apikey=" + apikey + "&" + "apisecret=" + apisecret + "&" + sign
            newSign = newSSign[:-1]
            #md5=hashlib.md5(newSign.encode('utf-8')).hexdigest().upper()
            md5 = base.md5_32.md5(newSign.encode(encoding="utf-8"))
            url0 = "?"+"apikey=" + apikey + "&" + "timestamp=" + timestamp1 + "&" + "nonce=" + nonce + "&" + "sign=" + md5
            #print(34524, url0)
            return url0
        elif request_data==None and params!=None:

            params["timestamp"] = timestamp1
            params["nonce"] = nonce
            newjson1 = sorted(params)
            sign = ""
            for x in newjson1:
                sign += x + "=" + params[x] + "&"
            newSSign = "apikey=" + apikey + "&" + "apisecret=" + apisecret + "&" + sign
            newSign = newSSign[:-1]
            #md5 = hashlib.md5(newSign.encode('utf-8')).hexdigest().upper()
            md5 = base.md5_32.md5(newSign.encode(encoding="utf-8"))
            url0 = "?" + "apikey=" + apikey + "&" + "timestamp=" + timestamp1 + "&" + "nonce=" + nonce + "&" + "sign=" + md5
            return url0
        elif request_data!=None and params==None:

            base_dict={"timestamp":timestamp1,"nonce":nonce}
            #request_data["timestamp"] = timestamp1
            #request_data["nonce"] = nonce
            json1 = base_dict.update(request_data)
            #print(json1, 1123,base_dict)
            newjson1 = sorted(base_dict)
            sign = ""
            for x in newjson1:
                #print(x, base_dict[x])
                if type(base_dict[x]) == type("abc"):
                    sign += x + "=" + base_dict[x] + "&"
                else:
                    sign += x + "=" + str(base_dict[x]) + "&"

            newSSign = "apikey=" + apikey + "&" + "apisecret=" + apisecret + "&" + sign
            newSign = newSSign[:-1]
            #print(123, newSign)
            #md5 = hashlib.md5(newSign.encode('utf-8')).hexdigest().upper()
            md5 = base.md5_32.md5(newSign.encode(encoding="utf-8"))
            url0 = "?" + "apikey=" + apikey + "&" + "timestamp=" + timestamp1 + "&" + "nonce=" + nonce + "&" + "sign=" + md5

            #print("md5_depend_1", request_data)
            return url0
        elif request_data==None and params==None:
            newSSign = "apikey=" + apikey + "&" + "apisecret=" + apisecret + "&" + "nonce=" + nonce+"&" + "timestamp=" + timestamp1
            #print(newSSign)
            md5 = base.md5_32.md5(newSSign.encode(encoding="utf-8"))
            url0 = "?" + "apikey=" + apikey + "&" + "timestamp=" + timestamp1 + "&" + "nonce=" + nonce + "&" + "sign=" + md5
            return url0
