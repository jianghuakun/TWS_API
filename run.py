#!/usr/bin/python3
import json
import unittest
from config.HTMLTestRunner import HTMLTestRunner
import time
# 相对路径
test_dir =r'./'
test_dir1 =r'./report'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_sta*.py')
if __name__ == '__main__':
    # 定义带有当前测试时间的报告，防止前一次报告被覆盖
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = now + ' OTA接口测试报告-系统账户.html'
    # 二进制打开，准备写入文件
    fp = open('./report/{0}'.format(filename), 'wb')
    # 定义测试报告
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况')
    runner = HTMLTestRunner(stream=fp, title=u'OTA接口测试报告-系统账户', description=u'统计情况')
    runner.run(discover)
    fp.close()
