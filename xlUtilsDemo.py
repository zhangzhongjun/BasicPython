#coding=utf-8
from xlrd import open_workbook
from xlutils.copy import copy

rb = open_workbook('f:\\1.xls')
 
#通过sheet_by_index()获取的sheet没有write()方法
rs = rb.sheet_by_index(0)

wb = copy(rb)

#通过get_sheet()获取的sheet有write()方法
ws = wb.get_sheet(0)
ws.write(0, 0, 'changed!')
 
wb.save('f:\\2.xls')

rb = open_workbook(u'C:\\Users\\zhang\\Desktop\\密码竞赛\\工作簿1.xlsm')
wb = copy(rb)
ws = wb.get_sheet(1)
ws.write(0,0,'Changed?')
wb.save(u"C:\\Users\\zhang\\Desktop\\密码竞赛\\多选题.xlsm")