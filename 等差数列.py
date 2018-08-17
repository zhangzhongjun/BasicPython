# coding=utf-8
#!/usr/bin/python

x1 = 0
d = 3
res = 0
# range(100)生成0-99的整数数列
for i in range(100):
    res += x1
    x1 += d
    print x1
print res

L = range(0,100,3)
print L
print sum(L)