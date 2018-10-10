# coding=utf-8
import codecs
import re
import IOUtils
#现
io = IOUtils.IOUtils()
f = codecs.open('f:\\333\\b.txt','r','utf-16')
L=f.readlines()
d={}
for i in range(len(L)):
    line = L[i]
    if re.match("@@@LINK=\d+", line, flags=0):
        k = line[line.find('=')+1::1]
        v = L[i-1]
        if k in d:
            d[k].append(v)
        else:
            d[k]=[v]
#print d
f.close()
f = codecs.open('f:\\333\\output_xian.txt','w','utf-16')
for key in d:
    str=key
    str = str
    for item in d[key]:
        str = str+item
    f.write(str+u"\r\n")
f.close()

#汗
io = IOUtils.IOUtils()
f = codecs.open('f:\\333\\a.txt','r','utf-8')
L=f.readlines()
d={}
for i in range(len(L)):
    line = L[i]
    if re.match("@@@LINK=DCD\d+", line, flags=0):
        k = line[line.find('=')+1::1]
        v = L[i-1]
        if k in d:
            d[k].append(v)
        else:
            d[k]=[v]
#print d
f.close()
f = codecs.open('f:\\333\\output_han.txt','w','utf-8')
for key in d:
    str=key
    str = str
    for item in d[key]:
        str = str+item
    f.write(str+u"\r\n")
f.close()