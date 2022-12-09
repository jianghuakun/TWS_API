#!/usr/bin/python3
from base.runmethon import runmethon
from data.get_data import GetData
from util.common_util import CommonUtil
from util.operation_header import OperationHeader
from util.operation_json import OperationJson
import requests
import json
import unittest
import re
import time
import unittest
from base.log import log1
import health
#智能health项目。
#1、account相关后台接口：192.168.75.242:9001/
#2、business相关后台接口：192.168.75.242:9002/
#例如：health/account/public/api/login    只需要拼接/api/login后   其它同理
#请求数据格式：{"token":token,"params":params}，其中token为登录获取token;params为请求数据调用加密接口加密后字符串。
#token执行health.py获取

class RunTest(unittest.TestCase):

    def setUp(self):
        self.run_method = runmethon()
        self.data = GetData()
        self.com_util = CommonUtil()
        #s1.oss_file_create()
    #def __init__(self):



        # self.send_email = SendEmail()

    def test_01(self):
    #def go_on_run(self):
        """程序执行"""
        pass_count = []
        fail_count = []
        count1=0
        count2=0
        res = None


        # 获取用例数
        #rows_count = self.data.get_case_lines()
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
                api_name=self.data.get_api_name(i)
                request_name=self.data.get_request_name(i)
                caseID=self.data.get_ID(i)
                times=self.data.get_times(i)
                # token执行health.py获取
                token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2Njg3NTI4ODQsIm5iZiI6MTY2ODc1Mjg4NCwiZXhwIjoxNjY5MzU3Njg0LCJkYXRhIjp7InBsYXRmb3JtaWQiOiIyMDEyNSIsInVzZXJpZCI6IkhQMDAxYWViOWZhMSJ9fQ.gxCXDatxMPd4FSnVg9IqLZCYr0eTpiYArwVEaM-CaGM"
                if method=="POST":
                    params = health.code(request_data)
                else:
                    pass
                newrequest_data = {"token": token, "params": params}
                herders = {'content-type': 'application/json;charset=utf-8',
                           'Accept': 'application/json;charset=utf-8'}
                res0 = self.run_method.run_main(method, url, newrequest_data, herders)
                exp_dic = eval(expect)
                for j in exp_dic.keys():
                    if str(exp_dic[j]) in str(res0):
                        #self.data.write_result(i, "Pass")
                        self.data.write_result(i, str(res0))
                        pass_count.append(i)
                        count1 += 1
                        log1.info("测试用例执行成功:%s" % caseID + '\n')
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(0, 0, "pass")
                    else:
                        self.data.write_result(i, str(res0))
                        fail_count.append(i)
                        count2 += 1
                        log1.error("测试用例执行失败:%s" % caseID + api_name + request_name + '\n')
                        with self.subTest(data=caseID + '_' + api_name + '_' + request_name):
                            self.assertEqual(expect, res0, "fail")
                print(res0)






        print(f"通过用例数：{len(pass_count)}")
        print(f"失败用例数：{len(fail_count)}")

        #with self.subTest(data=str(count1)):
            #self.assertEqual(count1, count2, "fail")
        #s2 = data_delete_ota()
        #s2.depart_delete()
    def tearDown(self):
        '''清除数据'''
        print("teardown")
        #db127.itri_ota.close()





if __name__ == '__main__':
    run = RunTest()
    run.test_01()