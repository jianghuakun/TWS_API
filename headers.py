#!/usr/bin/python3
import requests
import json
from config.excel_write import excel1

import time
import xlwt


'''终上所述，json与eval区别有两点：

1、json.loads与eval都能将s转成python中的对象，json.loads将json中的字符串转成unicode(types.UnicodeType)，eval转成了str(types.StringType)。

2、json不认单引号，json中的字符串需要用双引号包起来'''
data=["a","b","a"]
for x in data:
    if x=="a":
        data1 = excel1.sheet_read.cell(1, 0).value
        data2 = eval(data1)
        print(data2, "a")
        headers = {'content-type': 'application/json;charset=utf-8',
                   'Accept': 'application/json;charset=utf-8'
            , 'X-Access-Token': x}
        excel1.sheet_copy.write(1, 0, str(headers))
        excel1.excel2.save(r'dataconfig/header_write.xls')
    else:
        from config.excel_yes import excel2
        data1 = excel2.sheet_read.cell(1, 0).value
        data2 = eval(data1)
        print(data2,"no b")










