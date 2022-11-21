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
import unittest
class RunTest:

    def __init__(self):
        self.run_method = runmethon()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.md51=sing_md5()
        # self.send_email = SendEmail()

    def go_on_run(self):
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
                sign=self.md51.newsign(i)
                url+=sign
                urls=[]
                print(params)
                if params!= None:
                    param=''

                    for key in params.keys():
                        param1 = [param,key,"=",params[key],"&"]
                        param="".join(param1)
                    param=param[:-1]
                    url=url+"&"+param
                    urls.append(url)
                else:
                    urls.append(url)


                print(depend_case)
                if depend_case != None:
                    self.depend_data = DependentData(depend_case)
                    # 获取依赖的响应数据
                    #print(self.depend_data.run_dependent())
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    print(depend_response_data)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    """
                    
                    """
                    # 更新请求字段
                    print(depend_key)
                    depend_data_1 = depend_key.split("-")
                    request_data_1=request_data

                    if len(depend_data_1) == 1:
                        request_data[depend_key] = depend_response_data
                    elif len(depend_data_1) == 2:
                        try:
                            #第一个为数字（列表）
                            one_num=int(depend_data_1[0])
                            try:
                                #第二个为数字（列表）
                                two_num = int(depend_data_1[1])
                                request_data[one_num][two_num]=depend_response_data
                            except:
                                #第一个为数字（列表），第二个为字符串
                                request_data[one_num][depend_data_1[1]] = depend_response_data

                        except:
                            try:
                                #第一个为字符串，第二个为数字（列表）
                                two_num = int(depend_data_1[1])
                                request_data[depend_data_1[0]][two_num] = depend_response_data
                            except:
                                #2个都为字符串
                                request_data[depend_data_1[0]][depend_data_1[1]] = depend_response_data
                    elif len(depend_data_1) == 3:
                        try:
                            #第一个为数字（列表）
                            one_num=int(depend_data_1[0])
                            try:
                                #第二个为数字（列表）
                                two_num = int(depend_data_1[1])
                                try:
                                    #第三个为数字（列表）

                                    three_num = int(depend_data_1[2])
                                    print(1)
                                    request_data[one_num][two_num][three_num] = depend_response_data
                                except:

                                    #第三个为字符串，前2个都为数字
                                    request_data[one_num][two_num][depend_data_1[2]] = depend_response_data
                                    print(2)
                                    print(request_data[one_num][two_num][depend_data_1[2]])

                            except:
                                #第一个为数字（列表），第二个为字符串
                                try:
                                    #第3个为数字
                                    three_num = int(depend_data_1[2])
                                    print(3)
                                    request_data[one_num][depend_data_1[1]][three_num] = depend_response_data
                                except:
                                    #第3个为字符串
                                    print(4)
                                    request_data[one_num][depend_data_1[1]][depend_data_1[2]] = depend_response_data
                        except:
                            try:
                                #第一个为字符串，第二个为数字（列表）
                                two_num = int(depend_data_1[1])
                                try:
                                    #第三个为数字
                                    three_num = int(depend_data_1[2])
                                    print(5)
                                    request_data[depend_data_1[0]][two_num][three_num] = depend_response_data
                                except:
                                    #第三个为字符串
                                    print(6)
                                    request_data[depend_data_1[0]][two_num][depend_data_1[2]] = depend_response_data
                            except:

                                try:
                                    #第三个为数字
                                    three_num = int(depend_data_1[2])
                                    print(7)
                                    request_data[depend_data_1[0]][depend_data_1[1]][three_num] = depend_response_data
                                except:
                                    #3个都为字符
                                    print(8)
                                    request_data[depend_data_1[0]][depend_data_1[1]][depend_data_1[2]] = depend_response_data
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
                            print(123456,type(res),res,321)
                            token=dict(res)["result"]["token"]
                            print("run",token)
                            op_header = OperationHeader(token)
                            op_header.write_token()
                        else:
                            print("no token")
                            print(dict(res)["code"])

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
                    op_json = OperationJson("./dataconfig/token.json")
                    jsession2 = op_json.get_data('X-Access-Token')
                    #request_data = dict(request_data, **token)  # 把请求数据与登录token合并，并作为请求数据
                    herders={'content-type':'application/json;charset=utf-8',
          'Accept':'application/json;charset=utf-8','X-Access-Token':jsession2}
                    #print(urls[0], url,herders)
                    try:
                        res = self.run_method.run_main(method, url, request_data,herders)
                    except:
                        res = str({"error code":404})
                else:
                    try:
                        res = self.run_method.run_main(method, url, request_data)
                    except:
                        res=str({"error code":404})
                #检查点判断，判断预期结果是否在响应结果中，使用字符串是否在另一个字符串中进行判断，未采用key和值进行判断
                if expect != None:
                    #判断res是否为字符串，为字符串则直接比较；否则先转换为字符串再比较
                    if type(res) == type("abc"):
                        print(expect,type(expect),len(expect))
                        if self.com_util.is_contain(expect, res):

                            self.data.write_result(i, "Pass")
                            pass_count.append(i)
                        else:
                            self.data.write_result(i, res)
                            fail_count.append(i)
                    else:
                        print(len(expect))
                        res=str(res)
                        if self.com_util.is_contain(expect, res):
                            self.data.write_result(i, "Pass")
                            pass_count.append(i)
                        else:
                            self.data.write_result(i, res)
                            fail_count.append(i)

                else:
                    print(f"用例ID：case-{i}，预期结果不能为空")



        print(f"通过用例数：{len(pass_count)}")
        print(f"失败用例数：{len(fail_count)}")



if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()