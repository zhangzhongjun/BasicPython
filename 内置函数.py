# coding=utf-8
#!/usr/bin/python

d=['1','2','2']
print isinstance(d[0],str)
d=[{"name":'asd',"age":12},{"name":'asd',"age":12},{"name":'asd',"age":12}]
print isinstance(d[0],dict)

print sorted(['cut','HelLo','add','blue'])

print cmp(1,2)

pass
# unicode str是两种不同的数据类型
s = b'am I an unicode?'
print isinstance(s, unicode)
print isinstance(s,str)
s = u"am I an Unicode?"
print isinstance(s,unicode)
print isinstance(s,str)

L = [1,2,3,4]
print isinstance(L,list)

print type(L)
print type(s)

from random import randint
data = [randint(-10,10) for _ in xrange(10)]
print data
data = filter(lambda x:x>0,data)
print data

print range(1,5)