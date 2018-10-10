# coding=utf-8
import time
a = '2017-07-24 11:49:05'
b = time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))
print b