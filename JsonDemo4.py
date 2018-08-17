# coding=utf-8
import json

s='''
[1,2,3,"",3]
'''
import re
s = s.replace('\'','\"  ')
s = re.sub('<a .*?</a>', '',s)
print s
data = json.loads(s)