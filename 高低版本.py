#coding=utf-8

#2.X中的字符串默认为byte，而3.X中的字符串默认为unicode
#在字符串前面加上b，表示这是ascii编码；加上u，表示这是unicode编码
#2.X中/将得到整数，//将得到浮点数
#3.X中/将得到浮点数,//将得到整数

from __future__ import division
from __future__ import unicode_literals
print 10/3
print 10//3

