# coding=utf-8
#!/usr/bin/python
'''
	请牢记如下的网站：
	www.python.org()	官方网站，可能已经被墙 
	https://docs.python.org/2/ python2.7的帮助文档
'''
lines=['123','1','3','2','222','222222','123123']
print type(lines)
print str(type(lines))=="<type 'list'>"
print type(1)
for line in lines:
    #不含a
    if line.find('a')==-1:
        #包含2
        if line.find('2')!=-1:
            continue
        print line
print '========='
courses={'1','23'}
for i in range(0,5,1):
    print i
    i = i+2
i = 0
while i<5:
    print i
    i = i+2

a = 1
for i in range(1,20):
    a = 2
print a
print 1/25+1
print 50/25+1
print range(1,2,1)
print 0==0
print 21%20==1
import random
print random.random()

print 100/30
print 25/30
print 0/30

def getUrls(num):
    return num/30 if num%30==0 else num/30+1
print getUrls(100)
print getUrls(31)

import sys
#sys.setdefaultencoding("utf8")
# 输入和输出
print "hello world"
i= raw_input(u"请输入")
a = 45678
b = 0x12fd2
# 逗号会输出一个空格
print "45678 + 0x12fd2 =",a+b
print "learn python in imooc"
b1 = (100 < 99)
b2 = (0xff == 255)
print b1
print b2
print 'the quick brown fox','jump over','the lazy dog'

a = 'abc'
b = a
a = 'AXY'
print b

a = 1
b = a
a = 2
print b

print 2.5 + 10/4
print 2.5 + 10.0/4

# 在计算a or b时候，如果a是True，则返回a；否则返回b
# 短路计算
a = 'python'
print 'hello,',a or 'world'
b = ''
print 'hello,',b or 'world'

# python的缩进规则 ：四个空格
score = 75
if score>=60:
    print 'passed'

score = 55
if score>=60:
    print 'passed'
else:
    print 'failed'

score = 85
if score>= 90:
    print 'excellent'
elif score>=80:
    print 'good'
elif score>=60:
    print 'passed'
else:
    print 'failed'

L = ['Adam','Lisa','Bart']
for name in L:
    print name

L = [75,92,59,68]
sum = 0.0
for score in L:
    sum += score
print sum/4

N = 10
x = 0
while x<N:
    print x
    x = x + 1

sum = 0
x = 1
while x<100:
    sum += x
    x+=2
print sum

sum = 0
x = 1
n = 1
while True:
    sum += x
    x = x * 2
    n = n + 1
    if(n>20):
        break;
print sum

sum = 0
x = 0
while True:
    x = x + 1
    if x > 100:
        break;
    if x % 2 == 0:
        continue;
    sum = sum + x
print sum

for a in [1,2,3,4,5,6,7,8,9]:
    for b in [0,1,2,3,4,5,6,7,8,9]:
        if a < b:
            print a*10+b
			
# int函数,取整函数
print int(8.9)
print int(8.5)
print int(8.3)

name = 'John'
age = 23
salary = 3.512
print "my name is %s,i am %d years old,i earn %f K every year" %(name,age,salary)


