# coding=utf-8
#isupper islower
#将字符串2个2个的切割
ss = 'helloworldaaa'
print [ss[i:i+2] for i in range(0,len(ss),2)]
#切片
print ss[-1::1]
'''
The isupper() string method returns True if:
    1. The string has at least one uppercase letter.
    且2. The string does not have any lowercase letters in it.
The islower() string method returns True if:
    1. The string has at least one lowercase letter.
    且2. The string does not have any uppercase letters in it.
'''
print 'HELLO'.isupper()
print 'hEllo'.isupper()
print  'HELLO WORLD 123'.isupper()
print 'hello'.islower()
#title()方法 每一个单词的首字母都大写 其余字母都小写
print u'============title()==========='
print 'HELLO WORLD'.title()
print 'heLLO world'.title()
print 'Hello world'.title()
#replace方法
print u"==============replace()=========="
s = u'风景名胜;风景名 胜;国家级景点'
print s.replace(';','|')
#startswith endswith方法
print 'hello world'.startswith('he')
print 'hello world'.startswith('AA')
print 'hello world'.endswith('asd')
#切片
print u"===========切片功能============="
str = u"470671242"
print str[:len(str)-2:1]+u"."+str[len(str)-2::1]
#替代换行符
print u"===========替代换行符========="
str='''
as

asd
asd
asd
'''
print str.replace('\n','')
#去掉首尾的\r\n
str = "hello world\r\n"
print str,1
print str.strip('\r\n'),1
#替换
str = u"搞笑另类喊麦 - <em>DJ</em>版"
print str.replace(u"<em>","")
# 获取文件后缀
filenames = ["01.py","hehe.py","002.c","003.cpp","04.java","05.php","06.doc","09.css","index.html","10.js"]
# 使用for循环
for tempname in filenames:
    index = tempname.rfind(".")
    print(tempname[index+1::1])
# 使用列表生成式
print [tempname[tempname.rfind(".")+1::1] for tempname in filenames]
# 使用while循环
i = 0
while i<len(filenames):
    index = filenames[i].rfind(".")
    print(filenames[i][index+1::1])
    i+=1

L = [tempname[tempname.rfind(".")+1::1] for tempname in filenames]
S = set(L)
print S
# 字符串的截取功能
s = "hello world"
print u"截取： ",s[1:len(s)-1:1]
s = u"黄龄,薛之谦《来日方长》来日方长"
print s[s.rfind(u'》')+1::1]
name = u"Late Night (feat. Philthy Rich & The Hoodstarz)"
print name.find(u"(")
print name[:name.find(u"("):1]
title = u'Aaron Carter《Most Requested Hits》she wants me'
name = title[title.rfind(u'》')+1::1]
print name
print len(name)
print name[:name.find(u"("):1]
# 相当于trim
s = "  str  "
print s.strip()
print len(s.strip())
#转化成字符串
print str(1)
L=[1,2,3]
print str(L)