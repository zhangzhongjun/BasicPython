# coding=utf-8
import json
s = '[13588, 0, u"\u7b2c\u4e00\u5708", u"\u7b2c\u4e00\u5708", u"Round 1", 0, 0, 1]'
s = s[s.find('[')+1:s.rfind(']'):1]
print s
#s = '[1,2,3,"1"]'
data = s.split(',')
for d in data:
    print d,type(d)
s = '''
[13588, 0, u'\u7b2c\u4e00\u5708', u'\u7b2c\u4e00\u5708', u'Round 1', 0, 0, 1]
'''
s = s[s.find('[')+1:s.rfind(']'):1]
print s
data = s.split(',')
for d in data:
    print d,type(d),unicode(d,'unicode-escape')