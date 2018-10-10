# coding=utf-8
#!/usr/bin/python
#格式化输出
import pprint
a = [[1,2,3],[2,2],[12,1212],['hejji']]
pprint.pprint(a)
#排序
str = "ad"
L=['a','l','o','u','d','e','r']
print L
#排序方法 py3中已被弃用
L.sort(key = str.find,reverse=True)
print L
#itertools.product()方法来生成
print u'==============生成排列组合=============='
import itertools
print len(list(itertools.product(L,repeat=2))),list(itertools.product(L,repeat=2))
#定义一个string的list
print u'==============如何定义list=============='
L=['']
print L,len(L),type(L)
L=['']*10
print L,len(L),type(L)
#使用extend来扩展list
print u"==========================list的扩展================="
L1=[1,2,3]
L2=[12,23,23]
L1.extend(L2)
print L1
#使用加法扩展
print L1+L2
#使用shuffle来打乱list
print u"=======================打乱List==============="
print u'使用shuffle来打乱list'
import random
random.shuffle(L1)
print L1
#数组是按照地址引用的，reference
L=[1,23,23,213,2434,1234,23,23,42,55465,8768,34,123]
L1 = L
L1[1]='hello world'
print L1,L
#使用deepcopy完成真正的赋值
import copy
L2 = copy.deepcopy(L1)
L2[0]='bad world'
print L2,L1
#字符串的len函数
str='\r\n'
print len(str)
#list的__str__()函数
print L.__str__()
index = 0
ll = L[index:index+3]
while len(ll)!=0:
    ll = L[index:index+3]
    index = index+3
    print ll

L = ['Adam',95.5,'Lisa',85,'Bart',59]
print L
#extend()方法添加另一个list的全部元素
for i in L:
	print i,

print "\n"

for i in range(6):
	print L[i],
print "\n"
print L[-1]
print L[-2]
print L[-3]
print L[-4]
print L[-5]
print L[-6]

L.append('Paul')
L.append(50)
L.insert(0,'John')
L.insert(1,100)
for i in L:
	print i,

print "\n"
L = ['Adam','Lisa','Bert']
L.insert(2,'Paul')
print L
#相当于contains
print 'Adam' in L
print 'aa' in L
'''
	pop删除指定位置
	remove按照值删除
	del删除指定位置
'''
print ("-"*40)
# pop()方法总是去除最后一个元素，并且返回这个元素
theLast = L.pop()
print theLast
# pop(int index)方法可以去除指定位置的元素
theFirst = L.pop(0)
print theFirst
L=[1,2,3,4]
print L
del L[0]
print L
print ("-"*40)
L = ['Adam','Lisa','Bert','John']
L.join()
L.pop(-1)
L.pop(-1)
print L


# 如何交换List中的两个位置
print ("-"*40)
L = ['Adam','Lisa','Bart']
print L
temp = L[0]
L[0] = L[2]
L[2] = temp
print L
print ("-"*40)

# 列表生成式
L = range(1,100,2)
a = [x*(x+1) for x in L]
print a
# 列表生成式中还可以加上if语句
L = [x * x for x in range(1, 11) if x % 2 == 0]
print L
# 列表生成式中使用双重循环
L = [a*100+b*10+c for a in range(1,9,1) for b in range(0,9,1) for c in range(0,9,1) if a == c]
print L
print [a*100+b*10+c for a in range(1,9,1) for b in range(0,9,1) for c in range(0,9,1) if a==c]

# 使用列表生成式生成随机的list
from random import randint
data = [randint(-10,10) for _ in xrange(10)]
print data
print filter(lambda x:x>0,data)
# 使用列表生成式完成filter的功能
print [x for x in data if x>0]
print [x if x>0 else -x for x in data]