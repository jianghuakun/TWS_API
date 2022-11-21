#!/usr/bin/python3
import xlrd
import xlwt
import requests
import json
from xlutils.copy import copy
#xlrd只适合xls表格。xlsx表格需要使用其他函数
class excel1():
    path = r'D:\PyCharm2022.1.3\project\TWS_API.git\dataconfig\1.xls'
    excel1 = xlrd.open_workbook(path)
    sheet_read = excel1.sheets()[1]
    nrows = sheet_read.nrows
    excel2 = copy(excel1)
    sheet_copy = excel2.get_sheet(1)
    #print(sheet_read.cell(1, 1).value)




