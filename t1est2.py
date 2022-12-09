#!/usr/bin/python3
#第一个注释
import health
from base.runmethon import runmethon
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
data = GetData()
com_util = CommonUtil()
rows_count = data.get_case_lines()
run_method = runmethon()
for i in range(1, rows_count):
    is_run = data.get_is_run(i)
    if is_run:
        url = data.get_request_url(i)
        method = data.get_request_method(i)
        # request_data = data.get_data_for_json(i)
        request_data = data.get_request_data(i)
        expect = data.get_expcet_data(i)
        header = data.is_header(i)
        depend_case = data.is_depend(i)
        params = data.get_params(i)
        api_name = data.get_api_name(i)
        request_name = data.get_request_name(i)
        caseID = data.get_ID(i)
        times = data.get_times(i)
        # token执行health.py获取
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2Njg3NTI4ODQsIm5iZiI6MTY2ODc1Mjg4NCwiZXhwIjoxNjY5MzU3Njg0LCJkYXRhIjp7InBsYXRmb3JtaWQiOiIyMDEyNSIsInVzZXJpZCI6IkhQMDAxYWViOWZhMSJ9fQ.gxCXDatxMPd4FSnVg9IqLZCYr0eTpiYArwVEaM-CaGM"
        params1 = health.code(request_data)
        newrequest_data = {"token": token, "params": params1}
        herders = {'content-type': 'application/json;charset=utf-8',
                   'Accept': 'application/json;charset=utf-8'}
        res0 = run_method.run_main(method, url, newrequest_data, herders)
        print(res0)
        exp_dic = eval(expect)
        print(exp_dic)
        for i in exp_dic.keys():
            print(exp_dic[i])
    

