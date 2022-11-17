#!/usr/bin/python3
import xlrd
import xlwt
import requests
import json
from xlutils.copy import copy
#xlrd只适合xls表格。xlsx表格需要使用其他函数
class excel1:
    path = r'./dataconfig/header.xls'
    excel1 = xlrd.open_workbook(path)
    sheet_read = excel1.sheets()[0]
    nrows = sheet_read.nrows
    excel2 = copy(excel1)
    sheet_copy = excel2.get_sheet(0)
    #print(sheet_read.cell(1, 1).value)
