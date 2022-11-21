#!/usr/bin/python3
from base.runmethon import runmethon
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependentData
from util.operation_header import OperationHeader
from util.operation_json import OperationJson
import requests
import json
from base.md51 import sing_md5
from base.md5_depend import md5_depend
import unittest
import re
import time
import base.md5_32
from config.redis127 import redis127
from config.mysql127 import db127
from data.data_create_ota import data_create_ota
from data.data_delete_ota import data_delete_ota
import unittest
class RunTest(unittest.TestCase):

    def setUp(self):
        self.run_method = runmethon()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.md51 = sing_md5()
        self.md5_depend = md5_depend()
        s1=data_create_ota()
        s1.depart_create()
        s1.user_create()
        s1.oss_file_create()
    #def __init__(self):



        # self.send_email = SendEmail()

    def test_01(self):
    #def go_on_run(self):
        """程序执行"""
        pass_count = []
        fail_count = []
        res = None


        # 获取用例数
        rows_count = self.data.get_case_lines()
        # 第一行索引为0
        for i in range(1, rows_count):
            is_run = self.data.get_is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_request_method(i)
                #request_data = self.data.get_data_for_json(i)
                request_data = self.data.get_request_data(i)
                expect = self.data.get_expcet_data(i)
                header = self.data.is_header(i)
                depend_case = self.data.is_depend(i)
                params=self.data.get_params(i)



                if depend_case != None:

                    self.depend_data = DependentData(depend_case)
                    # 获取依赖的响应数据
                    # print(self.depend_data.run_dependent())
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    #print(113322,depend_response_data)
                    # print(depend_response_data)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    """

                    """
                    # 更新请求字段
                    # print(1231,depend_key,depend_response_data)
                    depend_data_1 = depend_key.split("-")
                    request_data_1 = request_data

                    if len(depend_data_1) == 1:
                        request_data[depend_key] = depend_response_data
                        #print(113311,request_data[depend_key],request_data)
                    elif len(depend_data_1) == 2:
                        try:
                            # 第一个为数字（列表）
                            one_num = int(depend_data_1[0])
                            try:
                                # 第二个为数字（列表）
                                two_num = int(depend_data_1[1])
                                request_data[one_num][two_num] = depend_response_data
                            except:
                                # 第一个为数字（列表），第二个为字符串
                                request_data[one_num][depend_data_1[1]] = depend_response_data

                        except:
                            try:
                                # 第一个为字符串，第二个为数字（列表）
                                two_num = int(depend_data_1[1])
                                request_data[depend_data_1[0]][two_num] = depend_response_data
                            except:
                                # 2个都为字符串
                                request_data[depend_data_1[0]][depend_data_1[1]] = depend_response_data
                    elif len(depend_data_1) == 3:
                        try:
                            # 第一个为数字（列表）
                            one_num = int(depend_data_1[0])
                            try:
                                # 第二个为数字（列表）
                                two_num = int(depend_data_1[1])
                                try:
                                    # 第三个为数字（列表）

                                    three_num = int(depend_data_1[2])
                                    #print(1)
                                    request_data[one_num][two_num][three_num] = depend_response_data
                                except:

                                    # 第三个为字符串，前2个都为数字
                                    request_data[one_num][two_num][depend_data_1[2]] = depend_response_data
                                    #print(2)
                                    #print(request_data[one_num][two_num][depend_data_1[2]])

                            except:
                                # 第一个为数字（列表），第二个为字符串
                                try:
                                    # 第3个为数字
                                    three_num = int(depend_data_1[2])
                                    #print(3)
                                    request_data[one_num][depend_data_1[1]][three_num] = depend_response_data
                                except:
                                    # 第3个为字符串
                                    #print(4)
                                    request_data[one_num][depend_data_1[1]][depend_data_1[2]] = depend_response_data
                        except:
                            try:
                                # 第一个为字符串，第二个为数字（列表）
                                two_num = int(depend_data_1[1])
                                try:
                                    # 第三个为数字
                                    three_num = int(depend_data_1[2])
                                    #print(5)
                                    request_data[depend_data_1[0]][two_num][three_num] = depend_response_data
                                except:
                                    # 第三个为字符串
                                    #print(6)
                                    request_data[depend_data_1[0]][two_num][depend_data_1[2]] = depend_response_data
                            except:

                                try:
                                    # 第三个为数字
                                    three_num = int(depend_data_1[2])
                                    #print(7)
                                    request_data[depend_data_1[0]][depend_data_1[1]][
                                        three_num] = depend_response_data
                                except:
                                    # 3个都为字符
                                    #print(8)
                                    request_data[depend_data_1[0]][depend_data_1[1]][
                                        depend_data_1[2]] = depend_response_data
                    #print(112233, request_data, url)
                    # 针对已经更新的请求body重新计算MD5值
                    # print(222, request_data)
                    sign = self.md5_depend.sign_depend(request_data, params)
                    # print(444, sign,request_data)
                    url += sign
                    urls = []
                    #print(112244, request_data, url)
                    # print(params)
                    if params != None:
                        param = ''
                        for key in params.keys():
                            if type(params[key])==type("abc"):
                                param1 = [param, key, "=", params[key], "&"]

                                param = "".join(param1)
                            else:
                                param1 = [param, key, "=", str(params[key]), "&"]

                                param = "".join(param1)

                        param = param[:-1]
                        url = url + "&" + param
                        urls.append(url)
                        #print(112255, request_data, url)
                else:
                    sign = self.md51.newsign(i)
                    url += sign
                    urls = []
                    # print(223311,request_data)

                    if params != None:
                        param = ''
                        for key in params.keys():
                            if type(params[key])==type("abc"):
                                param1 = [param, key, "=", params[key], "&"]

                                param = "".join(param1)
                            else:
                                param1 = [param, key, "=", str(params[key]), "&"]

                                param = "".join(param1)
                            #param1 = [param, key, "=", params[key], "&"]
                            #param = "".join(param1)
                        param = param[:-1]
                        url = url + "&" + param
                        urls.append(url)
                    # print(depend_case)
                    # print(111,request_data)

                #print(112255, request_data, url)
                #print(333, request_data)
                if request_data!=None:
                    if "timestamp" in request_data.keys():
                        request_data.pop("timestamp")
                    else:
                        pass
                    if "nonce" in request_data.keys():
                        request_data.pop("nonce")
                    else:
                        pass
                    # 如果request_data有修改，需要传给md5重新计算
                #print(112233,request_data)

                #print(request_data)
                # 如果header字段值为write则将该接口的返回的token写入到token.json文件，如果为yes则读取token.json文件
                if header == "write":
                    herders={'content-type': 'application/json;charset=utf-8',
                    'Accept': 'application/json;charset=utf-8'
                    }
                    try:
                        res = self.run_method.run_main(method, url, request_data, herders)
                        #print(urls[0], url,type(json.loads(res)))
                        if "result" in res:
                            #print(123456,type(res),res,321)
                            token=dict(res)["result"]["token"]
                            #print("run",token)
                            op_header = OperationHeader(token)
                            op_header.write_token()
                        else:
                            pass
                            #print("no token")
                            #print(dict(res)["code"])

                        #token = dict(r.json())["result"]["token"]

                    except:
                        res = str({"error code":404})

                    if method=="POST":
                        try:
                            r = requests.post(url, data=json.dumps(request_data), headers=herders)
                            #JSESSIONID在headers中
                            #JSESSIONID = dict(r.cookies)['JSESSIONID']
                            #token在body中
                            #print("post",r.json())
                            token=dict(r.json())["result"]["token"]
                            op_header = OperationHeader(token)
                            op_header.write_token()
                        except:
                            pass
                            # res = str({"error code":404})


                    else:
                        try:
                            r = requests.get(url, request_data)
                            token = dict(r.json())["result"]["token"]
                            op_header = OperationHeader(token)
                            #op_header = OperationHeader(dict(r.cookies))
                            op_header.write_token()
                        except:
                            pass
                            #res = str({"error code":404})




                elif header == 'yes':
                    #有依赖时，MD5验证码需要重新计算
                    op_json = OperationJson("./dataconfig/token.json")
                    jsession2 = op_json.get_data('X-Access-Token')
                    #request_data = dict(request_data, **token)  # 把请求数据与登录token合并，并作为请求数据
                    herders={'content-type':'application/json;charset=utf-8',
          'Accept':'application/json;charset=utf-8','X-Access-Token':jsession2}
                    #print(urls[0], url,herders)
                    #print("yes",request_data)
                    try:
                        res = self.run_method.run_main(method, url, request_data,herders)
                    except:
                        res = str({"error code":404})
                else:
                    try:
                        herders = {'content-type': 'application/json;charset=utf-8',
                                   'Accept': 'application/json;charset=utf-8'}
                        res = self.run_method.run_main(method, url, request_data,herders)
                    except:
                        res=str({"error code":404})
                #检查点判断，判断预期结果是否在响应结果中，使用字符串是否在另一个字符串中进行判断，未采用key和值进行判断

                if expect != None:
                    #判断res是否为字符串，为字符串则直接比较；否则先转换为字符串再比较
                    if type("123") == type("abc"):
                    #if type(res) == type("abc"):
                        testcase=unittest.TestCase

                        #print(expect,type(expect),len(expect))
                        exp_dic=eval(expect)
                        #print(exp_dic,123)
                        ticks = time.time()
                        new_ticks = str(ticks).replace('.', '')
                        #print('当前时间戳： ', new_ticks[:13])
                        if type(res)==type({"key":123}):
                            res = str(res)
                            res = res.replace("true", "True").replace("false", "False").replace("null","None")
                        else:
                            res = res.replace("true", "True").replace("false", "False").replace("null","None")
                        exp_dic["timestamp"] = new_ticks[:13]
                        result =eval(res)
                        #timestamp处理时间判断

                        t1 = int(int(result["timestamp"]) - int(exp_dic["timestamp"]))
                        result_exc=[]
                        count=0
                        if len(str(t1)) <6:
                            pass
                            #print("timestamp pass")
                        else:
                            #print("timestamp:%s"%t1)
                            list1={"timestamp":t1}
                            result_exc.append(list1)
                        #code为200时公共key值判断:
                        fail_dict={}
                        for keys in exp_dic.keys():
                            if keys=="code" and exp_dic["code"] == 200:
                                if result["code"] == 200:
                                    pass
                                    #print("code pass")
                                else:
                                    #print("code fail")
                                    list1 = {"code": result["code"]}
                                    result_exc.append(list1)
                                if result["message"] == "成功":
                                    pass
                                    print("message pass")
                                else:
                                    #print("message fail")
                                    list1 = {"message": result["message"]}
                                    result_exc.append(list1)
                                if result["success"] == True:
                                    pass
                                    #print("success pass")
                                else:
                                    #print("success fail")
                                    list1 = {"success": result["success"]}
                                    result_exc.append(list1)
                            elif keys=="timestamp":
                                pass
                            #key对应value值为字典，以及字典判断
                            elif type(exp_dic.get(keys))==type({"abc":123}) and keys in result.keys():
                                for keys1 in exp_dic.get(keys).keys():

                                    #print("result",type(exp_dic.get(keys).get(keys1)),type(["abc",123]))
                                    if "_length" in keys1:
                                        key2=keys1[:-7]
                                        #print(key2,keys,result.get(keys))
                                        if result.get(keys).get(key2)!=None:
                                            if len(result.get(keys).get(key2)) == exp_dic.get(keys).get(keys1):
                                                pass
                                                #print("%s pass" % key2)
                                            else:
                                                print("%s:%s" % (keys1, result.get(keys).get(key2)))
                                                list1 = {"%s.%s" % (keys, keys1): result.get(keys).get(key2)}
                                                result_exc.append(list1)
                                        else:
                                            print("%s:%s" % (keys1, result.get(keys).get(key2)))
                                            list1 = {"%s.%s" % (keys, keys1): result.get(keys).get(key2)}
                                            result_exc.append(list1)


                                    # 第2层值为列表以及第3层列表判断exp_dic.get(keys).get(keys1)
                                    elif type(exp_dic.get(keys).get(keys1)) == type(["abc",123]) and "_list" not in keys1:
                                        for keys2 in exp_dic.get(keys).get(keys1)[0].keys():
                                            if "_length" in keys2:
                                                key_1 = keys2[:-7]
                                                #print(keys2,keys,result.get(keys))
                                                if result.get(keys).get(keys1)[0].get(key_1) != None:
                                                    if len(result.get(keys).get(keys1)[0].get(key_1)) == \
                                                            exp_dic.get(keys).get(keys1)[0].get(keys2):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % ( keys, keys1, keys2, result.get(keys).get(keys1)[0].get(key_1)))
                                                        list1 = {"%s.%s.%s" % (keys, keys1,keys2): result.get(keys).get(keys1)[0].get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (keys, keys1, keys2, result.get(keys).get(keys1)[0].get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2): result.get(keys).get(keys1)[
                                                            0].get(key_1)}
                                                    result_exc.append(list1)


                                            elif "_include" in keys2:
                                                key_1 = keys2[:-8]
                                                # print(keys, exp_dic.get(keys), key1)
                                                if result.get(keys).get(keys1)[0].get(key_1) != None:
                                                    if exp_dic.get(keys).get(keys1)[0].get(key_1) in \
                                                            result.get(keys).get(keys1)[0].get(keys2):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                            keys, keys1, keys2,
                                                            result.get(keys).get(keys1)[0].get(key_1)))
                                                        list1 = {"%s.%s.%s" % (keys, keys1, keys2):
                                                                     result.get(keys).get(keys1)[0].get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys).get(keys1)[0].get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2): result.get(keys).get(keys1)[
                                                            0].get(key_1)}
                                                    result_exc.append(list1)

                                            elif "_type" in keys2:
                                                key_1 = keys2[:-5]
                                                # print(keys, exp_dic.get(keys), key1)
                                                # print("key3",type(exp_dic.get(keys).get(keys1)),type(result.get(keys).get(key3)))
                                                if result.get(keys).get(keys1)[0].get(key_1) != None:
                                                    if type(exp_dic.get(keys).get(keys1)[0].get(keys2)) == type(
                                                            result.get(keys).get(keys1)[0].get(key_1)):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                            keys, keys1, keys2,
                                                            result.get(keys).get(keys1)[0].get(key_1)))
                                                        list1 = {"%s.%s.%s" % (keys, keys1, keys2):
                                                                     result.get(keys).get(keys1)[0].get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys).get(keys1)[0].get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2): result.get(keys).get(keys1)[
                                                            0].get(key_1)}
                                                    result_exc.append(list1)

                                            elif "_list" in keys2:
                                                key_1 = keys2[:-5]
                                                # print(key2,keys,result.get(keys))
                                                if result.get(keys).get(keys1)[0].get(key_1) != None:
                                                    if result.get(keys).get(keys1)[0].get(key_1) in \
                                                            exp_dic.get(keys).get(keys1)[0].get(keys2):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                            keys, keys1, keys2,
                                                            result.get(keys).get(keys1)[0].get(key_1)))
                                                        list1 = {"%s.%s.%s" % (keys, keys1, keys2):
                                                                     result.get(keys).get(keys1)[0].get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys).get(keys1)[0].get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2): result.get(keys).get(keys1)[
                                                            0].get(key_1)}
                                                    result_exc.append(list1)

                                            elif "_range" in keys2:
                                                key_1 = keys2[:-6]
                                                # print(key2,keys,result.get(keys))
                                                # print("range",exp_dic.get(keys))
                                                if result.get(keys).get(keys1)[0].get(key_1)!=None:
                                                    if result.get(keys).get(keys1)[0].get(key_1) in \
                                                            exp_dic.get(keys).get(keys1)[0].get(keys2):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                            keys, keys1, keys2,
                                                            result.get(keys).get(keys1)[0].get(key_1)))
                                                        list1 = {"%s.%s.%s" % (keys, keys1, keys2):
                                                                     result.get(keys).get(keys1)[0].get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys).get(keys1)[0].get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2): result.get(keys).get(keys1)[
                                                            0].get(key_1)}
                                                    result_exc.append(list1)
                                            #keys2值为字典判断
                                            elif type(exp_dic.get(keys).get(keys1)[0].get(keys2))==type(["abc",123]) and "_list" not in keys1:
                                                for keys3 in exp_dic.get(keys).get(keys1)[0].get(keys2).keys():
                                                    if "_length" in keys3:
                                                        key_1 = keys3[:-7]
                                                        # print(key2,keys,result.get(keys))
                                                        if result.get(keys).get(keys1)[0].get(keys2).get(key_1) != None:
                                                            if len(result.get(keys).get(keys1)[0].get(keys2).get(key_1)) == \
                                                                    exp_dic.get(keys).get(keys1)[0].get(keys2).get(
                                                                        keys3):
                                                                pass
                                                                #print("%s pass" % keys3)
                                                            else:
                                                                print("%s.%s.%s.%s:%s" % (
                                                                    keys, keys1, keys2,keys3,
                                                                    result.get(keys).get(keys1)[0].get(keys2).get(key_1)))
                                                                list1 = {
                                                                    "%s.%s.%s.%s" % (keys, keys1, keys2,keys3):
                                                                        result.get(keys).get(keys1)[0].get(keys2).get(
                                                                            key_1)}
                                                                result_exc.append(list1)
                                                        else:
                                                            print("%s.%s.%s.%s:%s" % (
                                                                keys, keys1, keys2, keys3,
                                                                result.get(keys).get(keys1)[0].get(keys2).get(key_1)))
                                                            list1 = {
                                                                "%s.%s.%s.%s" % (keys, keys1, keys2, keys3):
                                                                    result.get(keys).get(keys1)[0].get(keys2).get(
                                                                        key_1)}
                                                            result_exc.append(list1)


                                                    elif "_include" in keys2:
                                                        key_1 = keys3[:-8]
                                                        # print(keys, exp_dic.get(keys), key1)
                                                        if result.get(keys).get(keys1)[0].get(keys2).get(key_1) != None:
                                                            if exp_dic.get(keys).get(keys1)[0].get(keys2).get(
                                                                        keys3) in \
                                                                    result.get(keys).get(keys1)[0].get(keys2).get(key_1):
                                                                pass
                                                                #print("%s pass" % keys3)
                                                            else:
                                                                print("%s.%s.%s.%s:%s" % (
                                                                    keys, keys1, keys2, keys3,
                                                                    result.get(keys).get(keys1)[0].get(keys2).get(
                                                                        key_1)))
                                                                list1 = {
                                                                    "%s.%s.%s.%s" % (keys, keys1, keys2, keys3):
                                                                        result.get(keys).get(keys1)[0].get(keys2).get(
                                                                            key_1)}
                                                                result_exc.append(list1)
                                                        else:
                                                            print("%s.%s.%s.%s:%s" % (
                                                                keys, keys1, keys2, keys3,
                                                                result.get(keys).get(keys1)[0].get(keys2).get(key_1)))
                                                            list1 = {
                                                                "%s.%s.%s.%s" % (keys, keys1, keys2, keys3):
                                                                    result.get(keys).get(keys1)[0].get(keys2).get(
                                                                        key_1)}
                                                            result_exc.append(list1)

                                                    elif "_type" in keys2:
                                                        key_1 = keys3[:-5]
                                                        # print(keys, exp_dic.get(keys), key1)
                                                        # print("key3",type(exp_dic.get(keys).get(keys1)),type(result.get(keys).get(key3)))
                                                        if result.get(keys).get(keys1)[0].get(keys2).get(key_1) != None:
                                                            if type(exp_dic.get(keys).get(keys1)[0].get(keys2).get(
                                                                        keys3)) == type(result.get(keys).get(keys1)[0].get(keys2).get(key_1)):
                                                                pass
                                                                #print("%s pass" % keys3)
                                                            else:
                                                                print("%s.%s.%s.%s:%s" % (
                                                                    keys, keys1, keys2, keys3,
                                                                    result.get(keys).get(keys1)[0].get(keys2).get(
                                                                        key_1)))
                                                                list1 = {
                                                                    "%s.%s.%s.%s" % (keys, keys1, keys2, keys3):
                                                                        result.get(keys).get(keys1)[0].get(keys2).get(
                                                                            key_1)}
                                                                result_exc.append(list1)
                                                        else:
                                                            print("%s.%s.%s.%s:%s" % (
                                                                keys, keys1, keys2, keys3,
                                                                result.get(keys).get(keys1)[0].get(keys2).get(key_1)))
                                                            list1 = {
                                                                "%s.%s.%s.%s" % (keys, keys1, keys2, keys3):
                                                                    result.get(keys).get(keys1)[0].get(keys2).get(
                                                                        key_1)}
                                                            result_exc.append(list1)

                                                    elif "_list" in keys2:
                                                        key_1 = keys3[:-5]
                                                        # print(key2,keys,result.get(keys))
                                                        if result.get(keys).get(keys1)[0].get(keys2).get(key_1) != None:
                                                            if result.get(keys).get(keys1)[0].get(keys2).get(key_1) in \
                                                                    exp_dic.get(keys).get(keys1)[0].get(keys2).get(
                                                                        keys3):
                                                                pass
                                                                #print("%s pass" % keys3)
                                                            else:
                                                                print("%s.%s.%s.%s:%s" % (
                                                                    keys, keys1, keys2, keys3,
                                                                    result.get(keys).get(keys1)[0].get(keys2).get(
                                                                        key_1)))
                                                                list1 = {
                                                                    "%s.%s.%s.%s" % (keys, keys1, keys2, keys3):
                                                                        result.get(keys).get(keys1)[0].get(keys2).get(
                                                                            key_1)}
                                                                result_exc.append(list1)
                                                        else:
                                                            print("%s.%s.%s.%s:%s" % (
                                                                keys, keys1, keys2, keys3,
                                                                result.get(keys).get(keys1)[0].get(keys2).get(key_1)))
                                                            list1 = {
                                                                "%s.%s.%s.%s" % (keys, keys1, keys2, keys3):
                                                                    result.get(keys).get(keys1)[0].get(keys2).get(
                                                                        key_1)}
                                                            result_exc.append(list1)

                                                    elif "_range" in keys2:
                                                        key_1 = keys3[:-6]
                                                        # print(key2,keys,result.get(keys))
                                                        # print("range",exp_dic.get(keys))
                                                        if result.get(keys).get(keys1)[0].get(keys2).get(key_1) != None:
                                                            if result.get(keys).get(keys1)[0].get(key_1) in \
                                                                    exp_dic.get(keys).get(keys1)[0].get(keys2).get(
                                                                        keys3):
                                                                pass
                                                                #print("%s pass" % keys3)
                                                            else:
                                                                print("%s.%s.%s.%s:%s" % (
                                                                    keys, keys1, keys2, keys3,
                                                                    result.get(keys).get(keys1)[0].get(keys2).get(
                                                                        key_1)))
                                                                list1 = {
                                                                    "%s.%s.%s.%s" % (keys, keys1, keys2, keys3):
                                                                        result.get(keys).get(keys1)[0].get(keys2).get(
                                                                            key_1)}
                                                                result_exc.append(list1)
                                                        else:
                                                            print("%s.%s.%s.%s:%s" % (
                                                                keys, keys1, keys2, keys3,
                                                                result.get(keys).get(keys1)[0].get(keys2).get(key_1)))
                                                    else:
                                                        print(keys, keys1, keys2)
                                                        if result.get(keys).get(keys1)[0].get(keys2).get(keys3) == \
                                                                exp_dic.get(keys).get(keys1)[0].get(keys2).get(
                                                                    keys3):
                                                            print("%s pass" % keys3)
                                                        else:
                                                            print("%s.%s.%s.%s:%s" % (
                                                                keys, keys1, keys2, keys3,
                                                                result.get(keys).get(keys1)[0].get(keys2).get(keys3)))
                                                            list1 = {
                                                                "%s.%s.%s.%s" % (keys, keys1, keys2, keys3):
                                                                    result.get(keys).get(keys1)[0].get(keys2).get(
                                                                        keys3)}
                                                            result_exc.append(list1)

                                            else:
                                                print(keys,keys1,keys2)
                                                if result.get(keys).get(keys1)[0].get(keys2) == exp_dic.get(keys).get(keys1)[0].get(keys2):
                                                    pass
                                                    #print("%s pass" % keys2)
                                                else:
                                                    print("%s.%s.%s:%s" % (keys,keys1,keys2, result.get(keys).get(keys1)[0].get(keys2)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys).get(keys1)[0].get(keys2)}
                                                    result_exc.append(list1)
                                    elif "_include" in keys1:
                                        key1 = keys1[:-8]
                                        # print(keys, exp_dic.get(keys), key1)
                                        if result.get(keys).get(key1)!=None:
                                            if exp_dic.get(keys).get(keys1) in result.get(keys).get(key1):
                                                pass
                                                #print("%s pass" % key1)
                                            else:
                                                print("%s:%s" % (keys1, result.get(keys).get(key1)))
                                                list1 = {
                                                    "%s.%s" % (keys, keys1):
                                                        result.get(keys).get(key1)}
                                                result_exc.append(list1)
                                        else:
                                            print("%s:%s" % (keys1, result.get(keys).get(key1)))
                                            list1 = {
                                                "%s.%s" % (keys, keys1):
                                                    result.get(keys).get(key1)}
                                            result_exc.append(list1)

                                    elif "_type" in keys1:
                                        key3 = keys1[:-5]
                                        #print(12521,keys,result,result.get(keys))
                                        # print(keys, exp_dic.get(keys), key1)
                                        #print("key3",type(exp_dic.get(keys).get(keys1)),type(result.get(keys).get(key3)))
                                        if result.get(keys).get(key3) != None:
                                            if type(exp_dic.get(keys).get(keys1)) == type(result.get(keys).get(key3)):
                                                pass
                                                #print("%s pass" % key3)
                                            else:
                                                print("%s:%s" % (keys1, result.get(keys).get(key3)))
                                                list1 = {
                                                    "%s.%s" % (keys, keys1):
                                                        result.get(keys).get(key3)}
                                                result_exc.append(list1)
                                        else:
                                            print("%s:%s" % (keys1, result.get(keys).get(key3)))
                                            list1 = {
                                                "%s.%s" % (keys, keys1):
                                                    result.get(keys).get(key3)}
                                            result_exc.append(list1)

                                    elif "_list" in keys1:
                                        key4 = keys1[:-5]
                                        # print(key2,keys,result.get(keys))
                                        if result.get(keys).get(key4) != None:
                                            if result.get(keys).get(key4) in exp_dic.get(keys).get(keys1):
                                                pass
                                                #print("%s pass" % key4)
                                            else:
                                                print("%s.%s:%s" % (keys, keys1, result.get(keys).get(key4)))
                                                list1 = {
                                                    "%s.%s" % (keys, keys1):
                                                        result.get(keys).get(key4)}
                                                result_exc.append(list1)
                                        else:
                                            print("%s.%s:%s" % (keys, keys1, result.get(keys).get(key4)))
                                            list1 = {
                                                "%s.%s" % (keys, keys1):
                                                    result.get(keys).get(key4)}
                                            result_exc.append(list1)

                                    elif "_range" in keys1:
                                        key5 = keys1[:-6]
                                        # print(key2,keys,result.get(keys))
                                        # print("range",exp_dic.get(keys))
                                        if result.get(keys).get(key5) != None:
                                            if result.get(keys).get(key5) in exp_dic.get(keys).get(keys1):
                                                pass
                                                #print("%s pass" % key5)
                                            else:
                                                print("%s.%s:%s" % (keys, keys1, result.get(keys).get(key5)))
                                                list1 = {
                                                    "%s.%s" % (keys, keys1):
                                                        result.get(keys).get(key5)}
                                                result_exc.append(list1)
                                        else:
                                            print("%s.%s:%s" % (keys, keys1, result.get(keys).get(key5)))
                                            list1 = {
                                                "%s.%s" % (keys, keys1):
                                                    result.get(keys).get(key5)}
                                            result_exc.append(list1)

                                    # 第2层为字典以及对应第3层判断
                                    elif type(exp_dic.get(keys).get(keys1))==type({"abc":123}):
                                        for keys2 in exp_dic.get(keys).get(keys1).keys():
                                            if "_length" in keys2:
                                                key_1 = keys2[:-7]
                                                # print(key2,keys,result.get(keys))
                                                if result.get(keys).get(keys1).get(key_1)!=None:
                                                    if len(result.get(keys).get(keys1).get(key_1)) == exp_dic.get(
                                                            keys).get(keys1).get(keys2):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys).get(keys1).get(key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1,keys2):
                                                                result.get(keys).get(keys1).get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys).get(keys1).get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys).get(keys1).get(key_1)}
                                                    result_exc.append(list1)


                                            elif "_include" in keys2:
                                                key_1 = keys2[:-8]
                                                # print(keys, exp_dic.get(keys), key1)
                                                if result.get(keys).get(keys1).get(key_1)!=None:
                                                    if exp_dic.get(keys).get(keys1).get(keys2) in result.get(keys).get(
                                                            keys1).get(key_1):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys).get(keys1).get(key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys).get(keys1).get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys).get(keys1).get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys).get(keys1).get(key_1)}
                                                    result_exc.append(list1)

                                            elif "_type" in keys2:
                                                key_1 = keys2[:-5]
                                                # print(keys, exp_dic.get(keys), key1)
                                                # print("key3",type(exp_dic.get(keys).get(keys1)),type(result.get(keys).get(key3)))
                                                if result.get(keys).get(keys1).get(key_1) != None:
                                                    if type(exp_dic.get(keys).get(keys1).get(keys2)) == type(
                                                            result.get(keys).get(keys1).get(key_1)):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys).get(keys1).get(key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys).get(keys1).get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys).get(keys1).get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys).get(keys1).get(key_1)}
                                                    result_exc.append(list1)

                                            elif "_list" in keys2:
                                                key_1 = keys2[:-5]
                                                # print(key2,keys,result.get(keys))
                                                if result.get(keys).get(keys1).get(key_1) != None:
                                                    if result.get(keys).get(keys1).get(key_1) in exp_dic.get(keys).get(
                                                            keys1).get(keys2):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys).get(keys1).get(key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys).get(keys1).get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys).get(keys1).get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys).get(keys1).get(key_1)}
                                                    result_exc.append(list1)


                                            elif "_range" in keys2:
                                                key_1 = keys2[:-6]
                                                # print(key2,keys,result.get(keys))
                                                # print("range",exp_dic.get(keys))
                                                if result.get(keys).get(keys1).get(key_1) != None:
                                                    if result.get(keys).get(keys1).get(key_1) in exp_dic.get(keys).get(
                                                            keys1).get(keys2):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys).get(keys1).get(key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys).get(keys1).get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys).get(keys1).get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys).get(keys1).get(key_1)}
                                                    result_exc.append(list1)

                                            else:

                                                if result.get(keys).get(keys1).get(keys2) == exp_dic.get(keys).get(keys1).get(keys2):
                                                    pass
                                                    #print("%s pass" % keys2)
                                                else:
                                                    print("%s.%s.%s:%s" % (keys,keys1,keys2, result.get(keys).get(keys1).get(keys2)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys).get(keys1).get(keys2)}
                                                    result_exc.append(list1)

                                    else:
                                        if result.get(keys).get(keys1) == exp_dic.get(keys).get(keys1):
                                            pass
                                            #print("%s pass" % keys)
                                        else:
                                            print("%s:%s"%(keys, result.get(keys)))
                                            list1 = {
                                                "%s.%s" % (keys, keys1):
                                                    result.get(keys).get(keys1)}
                                            result_exc.append(list1)
                            # 第一层key对应value值为列表以及2层列表中字典判断
                            elif type(exp_dic.get(keys))==type(["abc",123]) and "_list" not in keys and keys in result.keys():
                                for keys1 in exp_dic.get(keys)[0].keys():
                                    if "_length" in keys1:
                                        key2=keys1[:-7]
                                        #print(key2,keys,result.get(keys))
                                        if result.get(keys)[0].get(key2)!=None:
                                            if len(result.get(keys)[0].get(key2)) == exp_dic.get(keys)[0].get(keys1):
                                                pass
                                                #print("%s pass" % key2)
                                            else:
                                                print("%s:%s" % (keys1, result.get(keys)[0].get(key2)))
                                                list1 = {
                                                    "%s.%s" % (keys, keys1):
                                                        result.get(keys)[0].get(key2)}
                                                result_exc.append(list1)
                                        else:
                                            print("%s:%s" % (keys1, result.get(keys)[0].get(key2)))
                                            list1 = {
                                                "%s.%s" % (keys, keys1):
                                                    result.get(keys)[0].get(key2)}
                                            result_exc.append(list1)



                                    elif "_include" in keys1:
                                        key1 = keys1[:-8]
                                        # print(keys, exp_dic.get(keys), key1)
                                        if result.get(keys).get(key1) != None:
                                            if exp_dic.get(keys).get(keys1) in result.get(keys)[0].get(key1):
                                                pass
                                                #print("%s pass" % key1)
                                            else:
                                                print("%s:%s" % (keys1, result.get(keys)[0].get(key1)))
                                                list1 = {
                                                    "%s.%s" % (keys, keys1):
                                                        result.get(keys)[0].get(key1)}
                                                result_exc.append(list1)
                                        else:
                                            print("%s:%s" % (keys1, result.get(keys)[0].get(key1)))
                                            list1 = {
                                                "%s.%s" % (keys, keys1):
                                                    result.get(keys)[0].get(key1)}
                                            result_exc.append(list1)

                                    elif "_type" in keys1:
                                        key3 = keys1[:-5]
                                        # print(keys, exp_dic.get(keys), key1)
                                        #print("key3",type(exp_dic.get(keys).get(keys1)),type(result.get(keys).get(key3)))
                                        if result.get(keys)[0].get(key3) != None:
                                            if type(exp_dic.get(keys)[0].get(keys1)) == type(
                                                    result.get(keys)[0].get(key3)):
                                                pass
                                                #print("%s pass" % key3)
                                            else:
                                                print("%s:%s" % (keys1, result.get(keys)[0].get(key3)))
                                                list1 = {
                                                    "%s.%s" % (keys, keys1):
                                                        result.get(keys)[0].get(key3)}
                                                result_exc.append(list1)
                                        else:
                                            print("%s:%s" % (keys1, result.get(keys)[0].get(key3)))
                                            list1 = {
                                                "%s.%s" % (keys, keys1):
                                                    result.get(keys)[0].get(key3)}
                                            result_exc.append(list1)

                                    elif "_list" in keys1:
                                        key4 = keys1[:-5]
                                        # print(key2,keys,result.get(keys))
                                        if result.get(keys)[0].get(key4) != None:
                                            if result.get(keys)[0].get(key4) in exp_dic.get(keys)[0].get(keys1):
                                                pass
                                                #print("%s pass" % key4)
                                            else:
                                                print("%s.%s:%s" % (keys, keys1, result.get(keys)[0].get(key4)))
                                                list1 = {
                                                    "%s.%s" % (keys, keys1):
                                                        result.get(keys)[0].get(key4)}
                                                result_exc.append(list1)
                                        else:
                                            print("%s.%s:%s" % (keys, keys1, result.get(keys)[0].get(key4)))
                                            list1 = {
                                                "%s.%s" % (keys, keys1):
                                                    result.get(keys)[0].get(key4)}
                                            result_exc.append(list1)

                                    elif "_range" in keys1:
                                        key5 = keys1[:-6]
                                        # print(key2,keys,result.get(keys))
                                        # print("range",exp_dic.get(keys))
                                        if result.get(keys).get(key5) != None:
                                            if result.get(keys)[0].get(key5) in exp_dic.get(keys)[0].get(keys1):
                                                pass
                                                #print("%s pass" % key5)
                                            else:
                                                print("%s.%s:%s" % (keys, keys1, result.get(keys)[0].get(key5)))
                                                list1 = {
                                                    "%s.%s" % (keys, keys1):
                                                        result.get(keys)[0].get(key5)}
                                                result_exc.append(list1)
                                        else:
                                            print("%s.%s:%s" % (keys, keys1, result.get(keys)[0].get(key5)))
                                            list1 = {
                                                "%s.%s" % (keys, keys1):
                                                    result.get(keys)[0].get(key5)}
                                            result_exc.append(list1)

                                    #第2层为字典以及对应第3层判断
                                    elif type(exp_dic.get(keys)[0].get(keys1))==type({"abc":123}):
                                        for keys2 in exp_dic.get(keys)[0].get(keys1).keys():
                                            if "_length" in keys2:
                                                key_1 = keys2[:-7]
                                                print(result.get(keys)[0].get(keys1).get(key_1))
                                                if result.get(keys)[0].get(keys1).get(key_1)!=None:
                                                    if len(result.get(keys)[0].get(keys1).get(key_1)) ==exp_dic.get(keys)[0].get(keys1).get(keys2):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys)[0].get(keys1).get(key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1,keys2):
                                                                result.get(keys)[0].get(keys1).get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys)[0].get(keys1).get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys)[0].get(keys1).get(key_1)}
                                                    result_exc.append(list1)


                                            elif "_include" in keys2:
                                                key_1 = keys2[:-8]
                                                # print(keys, exp_dic.get(keys), key1)
                                                if result.get(keys)[0].get(keys1).get(key_1)!=None:
                                                    if exp_dic.get(keys)[0].get(keys1).get(keys2) in result.get(keys)[
                                                        0].get(keys1).get(key_1):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys)[0].get(keys1).get(key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys)[0].get(keys1).get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys)[0].get(keys1).get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys)[0].get(keys1).get(key_1)}
                                                    result_exc.append(list1)

                                            elif "_type" in keys2:
                                                key_1 = keys2[:-5]
                                                # print(keys, exp_dic.get(keys), key1)
                                                # print("key3",type(exp_dic.get(keys).get(keys1)),type(result.get(keys).get(key3)))
                                                if result.get(keys)[0].get(keys1).get(key_1) != None:
                                                    if type(exp_dic.get(keys)[0].get(keys1).get(keys2)) == type(
                                                            result.get(keys)[0].get(keys1).get(key_1)):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys)[0].get(keys1).get(key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys)[0].get(keys1).get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys)[0].get(keys1).get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys)[0].get(keys1).get(key_1)}
                                                    result_exc.append(list1)



                                            elif "_list" in keys2:
                                                key_1 = keys2[:-5]
                                                # print(key2,keys,result.get(keys))
                                                if result.get(keys)[0].get(keys1).get(key_1) != None:
                                                    if result.get(keys)[0].get(keys1).get(key_1) in exp_dic.get(keys)[
                                                        0].get(keys1).get(keys2):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys)[0].get(keys1).get(key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys)[0].get(keys1).get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys)[0].get(keys1).get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys)[0].get(keys1).get(key_1)}
                                                    result_exc.append(list1)

                                            elif "_range" in keys2:
                                                key_1 = keys2[:-6]
                                                # print(key2,keys,result.get(keys))
                                                # print("range",exp_dic.get(keys))
                                                if result.get(keys)[0].get(keys1).get(key_1) != None:
                                                    if result.get(keys)[0].get(keys1).get(key_1) in exp_dic.get(keys)[
                                                        0].get(keys1).get(keys2):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys)[0].get(keys1).get(key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys)[0].get(keys1).get(key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys)[0].get(keys1).get(key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys)[0].get(keys1).get(key_1)}
                                                    result_exc.append(list1)

                                            else:
                                                #print("%s.%s.%s" % (keys, keys1, keys2))
                                                if result.get(keys)[0].get(keys1).get(keys2) != None:
                                                    if result.get(keys)[0].get(keys1).get(keys2) == exp_dic.get(keys)[
                                                        0].get(keys1).get(keys2):
                                                        pass
                                                        #print("%s pass" % keys2)
                                                    else:
                                                        print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys)[0].get(keys1).get(keys2)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys)[0].get(keys1).get(keys2)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (
                                                        keys, keys1, keys2, result.get(keys)[0].get(keys1).get(keys2)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys)[0].get(keys1).get(keys2)}
                                                    result_exc.append(list1)

                                    #第2层值为列表以及第3层列表判断
                                    elif type(exp_dic.get(keys)[0].get(keys1))==type(["abc",123]):
                                        for keys2 in exp_dic.get(keys)[0].get(keys1)[0].keys():
                                            if "_length" in keys2:
                                                key_1 = keys2[:-7]
                                                # print(key2,keys,result.get(keys))
                                                if result.get(keys)[0].get(keys1)[0].get(key_1)!=None:
                                                    if len(result.get(keys)[0].get(keys1)[0].get(key_1)) == \
                                                            exp_dic.get(keys)[0].get(keys1)[0].get(keys2):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (keys, keys1, keys2,
                                                                               result.get(keys)[0].get(keys1)[0].get(
                                                                                   key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys)[0].get(keys1)[0].get(
                                                                    key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (keys, keys1, keys2,
                                                                           result.get(keys)[0].get(keys1)[0].get(
                                                                               key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys)[0].get(keys1)[0].get(
                                                                key_1)}
                                                    result_exc.append(list1)


                                            elif "_include" in keys2:
                                                key_1 = keys2[:-8]
                                                # print(keys, exp_dic.get(keys), key1)
                                                if result.get(keys)[0].get(keys1)[0].get(key_1) != None:
                                                    if exp_dic.get(keys)[0].get(keys1)[0].get(key_1) in \
                                                            result.get(keys)[0].get(keys1)[0].get(keys2):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (keys, keys1, keys2,
                                                                               result.get(keys)[0].get(keys1)[0].get(
                                                                                   key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys)[0].get(keys1)[0].get(
                                                                    key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (keys, keys1, keys2,
                                                                           result.get(keys)[0].get(keys1)[0].get(
                                                                               key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys)[0].get(keys1)[0].get(
                                                                key_1)}
                                                    result_exc.append(list1)

                                            elif "_type" in keys2:
                                                key_1 = keys2[:-5]
                                                # print(keys, exp_dic.get(keys), key1)
                                                # print("key3",type(exp_dic.get(keys).get(keys1)),type(result.get(keys).get(key3)))
                                                if result.get(keys)[0].get(keys1)[0].get(key_1) != None:
                                                    if type(exp_dic.get(keys)[0].get(keys1)[0].get(keys2)) == type(
                                                            result.get(keys)[0].get(keys1)[0].get(key_1)):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (keys, keys1, keys2,
                                                                               result.get(keys)[0].get(keys1)[0].get(
                                                                                   key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys)[0].get(keys1)[0].get(
                                                                    key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (keys, keys1, keys2,
                                                                           result.get(keys)[0].get(keys1)[0].get(
                                                                               key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys)[0].get(keys1)[0].get(
                                                                key_1)}
                                                    result_exc.append(list1)

                                            elif "_list" in keys2:
                                                key_1 = keys2[:-5]
                                                # print(key2,keys,result.get(keys))
                                                if result.get(keys)[0].get(keys1)[0].get(key_1) != None:
                                                    if result.get(keys)[0].get(keys1)[0].get(key_1) in \
                                                            exp_dic.get(keys)[0].get(keys1)[0].get(keys2):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (keys, keys1, keys2,
                                                                               result.get(keys)[0].get(keys1)[0].get(
                                                                                   key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys)[0].get(keys1)[0].get(
                                                                    key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (keys, keys1, keys2,
                                                                           result.get(keys)[0].get(keys1)[0].get(
                                                                               key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys)[0].get(keys1)[0].get(
                                                                key_1)}
                                                    result_exc.append(list1)

                                            elif "_range" in keys2:
                                                key_1 = keys2[:-6]
                                                # print(key2,keys,result.get(keys))
                                                # print("range",exp_dic.get(keys))
                                                if result.get(keys)[0].get(keys1)[0].get(key_1) != None:
                                                    if result.get(keys)[0].get(keys1)[0].get(key_1) in \
                                                            exp_dic.get(keys)[0].get(keys1)[0].get(keys2):
                                                        pass
                                                        #print("%s pass" % key_1)
                                                    else:
                                                        print("%s.%s.%s:%s" % (keys, keys1, keys2,
                                                                               result.get(keys)[0].get(keys1)[0].get(
                                                                                   key_1)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys)[0].get(keys1)[0].get(
                                                                    key_1)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (keys, keys1, keys2,
                                                                           result.get(keys)[0].get(keys1)[0].get(
                                                                               key_1)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys)[0].get(keys1)[0].get(
                                                                key_1)}
                                                    result_exc.append(list1)

                                            else:
                                                if result.get(keys)[0].get(keys1)[0].get(keys2) != None:
                                                    if result.get(keys)[0].get(keys1)[0].get(keys2) == \
                                                            exp_dic.get(keys)[0].get(keys1)[0].get(keys2):
                                                        pass
                                                        #print("%s pass" % keys2)
                                                    else:
                                                        print("%s.%s.%s:%s" % (keys, keys1, keys2,
                                                                               result.get(keys)[0].get(keys1)[0].get(
                                                                                   keys2)))
                                                        list1 = {
                                                            "%s.%s.%s" % (keys, keys1, keys2):
                                                                result.get(keys)[0].get(keys1)[0].get(
                                                                    keys2)}
                                                        result_exc.append(list1)
                                                else:
                                                    print("%s.%s.%s:%s" % (keys, keys1, keys2,
                                                                           result.get(keys)[0].get(keys1)[0].get(
                                                                               keys2)))
                                                    list1 = {
                                                        "%s.%s.%s" % (keys, keys1, keys2):
                                                            result.get(keys)[0].get(keys1)[0].get(
                                                                keys2)}
                                                    result_exc.append(list1)


                                    else:
                                        if result.get(keys)[0].get(keys1) != None:
                                            if result.get(keys)[0].get(keys1) == exp_dic.get(keys)[0].get(keys1):
                                                pass
                                                #print("%s pass" % keys)
                                            else:
                                                print("%s.%s:%s" % (keys, keys1, result.get(keys)[0].get(keys1)))
                                                list1 = {
                                                    "%s.%s" % (keys, keys1):
                                                        result.get(keys)[0].get(keys1)}
                                                result_exc.append(list1)
                                        else:
                                            print("%s.%s:%s" % (keys, keys1, result.get(keys)[0].get(keys1)))
                                            list1 = {
                                                "%s.%s" % (keys, keys1):
                                                    result.get(keys)[0].get(keys1)}
                                            result_exc.append(list1)

                            elif "_include" in keys:
                                key1=keys[:-8]
                                #print(keys, exp_dic.get(keys), key1)
                                if result.get(key1) != None:
                                    if exp_dic.get(keys) in result.get(key1):
                                        pass
                                        #print("%s pass" % key1)
                                    else:
                                        print("%s:%s" % (keys, result.get(key1)))
                                        list1 = {
                                            "%s" % (keys):
                                                result.get(key1)}
                                        result_exc.append(list1)
                                else:
                                    print("%s:%s" % (keys, result.get(key1)))
                                    list1 = {
                                        "%s" % (keys):
                                            result.get(key1)}
                                    result_exc.append(list1)

                            elif "_type" in keys:
                                key3 = keys[:-5]
                                # print(keys, exp_dic.get(keys), key1)
                                if result.get(key3) != None:
                                    if type(exp_dic.get(keys)) == type(result.get(key3)):
                                        pass
                                        #print("%s pass" % key3)
                                    else:
                                        print("%s:%s" % (keys, result.get(key3)))
                                        list1 = {
                                            "%s" % (keys):
                                                result.get(key3)}
                                        result_exc.append(list1)
                                else:
                                    print("%s:%s" % (keys, result.get(key3)))
                                    list1 = {
                                        "%s" % (keys):
                                            result.get(key3)}
                                    result_exc.append(list1)

                            elif "_length" in keys:
                                key2 = keys[:-7]
                                # print(key2,keys,result.get(keys))
                                if result.get(key2) != None:
                                    if len(result.get(key2)) == exp_dic.get(keys):
                                        pass
                                        #print("%s pass" % key2)
                                    else:
                                        print("%s:%s" % (keys, result.get(key2)))
                                        list1 = {
                                            "%s" % (keys):
                                                result.get(key2)}
                                        result_exc.append(list1)
                                else:
                                    print("%s:%s" % (keys, result.get(key2)))
                                    list1 = {
                                        "%s" % (keys):
                                            result.get(key2)}
                                    result_exc.append(list1)

                            elif "_list" in keys:
                                key4 = keys[:-5]
                                # print(key2,keys,result.get(keys))
                                if result.get(key4) != None:
                                    if result.get(key4) in exp_dic.get(keys):
                                        pass
                                        #print("%s pass" % key4)
                                    else:
                                        print("%s:%s" % (keys, result.get(key4)))
                                        list1 = {
                                            "%s" % (keys):
                                                result.get(key4)}
                                        result_exc.append(list1)
                                else:
                                    print("%s:%s" % (keys, result.get(key4)))
                                    list1 = {
                                        "%s" % (keys):
                                            result.get(key4)}
                                    result_exc.append(list1)

                            elif "_range" in keys:
                                key5 = keys[:-6]
                                # print(key2,keys,result.get(keys))
                                #print("range",exp_dic.get(keys))
                                if result.get(key5) != None:
                                    if result.get(key5) in exp_dic.get(keys):
                                        pass
                                        #print("%s pass" % key5)
                                    else:
                                        print("%s:%s" % (keys, result.get(key5)))
                                        list1 = {
                                            "%s" % (keys):
                                                result.get(key5)}
                                        result_exc.append(list1)
                                else:
                                    print("%s:%s" % (keys, result.get(key5)))
                                    list1 = {
                                        "%s" % (keys):
                                            result.get(key5)}
                                    result_exc.append(list1)

                            else:
                                if result.get(keys) != None:
                                    if result.get(keys) == exp_dic.get(keys):
                                        pass
                                        #print("%s pass" % keys)
                                    else:
                                        print("%s:%s" % (keys, result.get(keys)))
                                        list1 = {
                                            "%s" % (keys):
                                                result.get(keys)}
                                        result_exc.append(list1)
                                else:
                                    print("%s:%s" % (keys, result.get(keys)))
                                    list1 = {
                                        "%s" % (keys):
                                            result.get(keys)}
                                    result_exc.append(list1)






                        if len(result_exc)==0:
                            self.data.write_result(i, "Pass")
                            pass_count.append(i)
                            with self.subTest(data="case_"+str(i)):
                                self.assertEqual(len(result_exc),0,"pass" )
                        else:
                            self.data.write_result(i, str(result_exc))
                            fail_count.append(i)
                            with self.subTest(data="case_"+str(i)):
                                self.assertEqual(result_exc,exp_dic,"fail" )


                    else:
                        print(len(expect))
                        res=str(res)
                        if self.com_util.is_contain(expect, res):
                            pass
                            #self.data.write_result(i, "Pass")
                            #pass_count.append(i)
                        else:
                            pass
                            #self.data.write_result(i, res)
                            #fail_count.append(i)

                else:
                    print(f"用例ID：case-{i}，预期结果不能为空")



        print(f"通过用例数：{len(pass_count)}")
        print(f"失败用例数：{len(fail_count)}")
        #s2 = data_delete_ota()
        #s2.itri_ota_delete()
    def tearDown(self):
        '''清除数据'''
        s2 = data_delete_ota()
        s2.depart_delete()
        s2.user_delete()
        s2.version_delete()
        db127.itri_ota.close()





if __name__ == '__main__':
    run = RunTest()
    run.test_01()