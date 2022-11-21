#!/usr/bin/python3
from base.runmethon import runmethon
#from data.get_data import GetData
from data.data_web import GetData
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
from selenium import webdriver
class RunTest(unittest.TestCase):

    def setUp(self):
        self.run_method = runmethon()
        self.data = GetData()
        self.com_util = CommonUtil()
        self.md51 = sing_md5()
        self.md5_depend = md5_depend()
        #s1=data_create_ota()
        #s1.depart_create()
        #s1.user_create()
        #s1.oss_file_create()
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
                action_type=self.data.get_depend_key(i)
                action_value=self.data.get_depend_field(i)
                #params=self.data.get_params(i)
                print(method,url)
                driver = webdriver.Chrome()
                if method=="打开":

                    driver.maximize_window()
                    driver.get(url)

                else:
                    pass
                if depend_case=="xpath":
                    if method == "点击":
                        if action_type!=0:
                            text=driver.find_elements_by_xpath(action_value)
                            #driver.find_elements_by_xpath("%s"%action_value)[0].click()

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