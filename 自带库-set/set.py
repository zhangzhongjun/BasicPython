# coding=utf-8
#!usr/bin/python

s = set([])
s.add(1)
s.add(1)
s.add(2)
s.add(3)
print(s)

s = "{'804a28df-dc8b-43d5-b7f9-51fd8e1549c7.txt', '4b571a62-130a-495e-96e4-b4eff466fde8.txt'}"
s = eval(s)
print (len(s))
print (s)
print (type(s))


# 如何生成一个set：set()传入一个List
s = set(["Adam","Lisa","Bart","Paul"])
print (s)
print (len(s))
#使用join
print ("".join(s))
s = set(["Adam","Lisa","Bart","Paul","adam","bart"])
print ("adam" in s)
print ("bart" in s)

# set的迭代
s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s:
    print (x[0]+':',x[1])

s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for i in L:
    if i in s:
        s.remove(i)
    else:
        s.add(i)
print (s)

# 使用set生成式来解析set
from random import randint
data = [randint(-10,10) for _ in range(20)]
print (data)
s = set(data)
print (s)
print (set([x for x in s if x>0]))

s1 = set([1,2,3,4])
s2 = set([2,3,4,5])
#并集
print(s1.union(s2))
print(s1|s2)
#交集
print(s1.intersection(s2))
print(s1&s2)
#差集
print(s1-s2)
#返回一个新的 set 包含 s 和 t 中不重复的元素
print(s1.symmetric_difference(s2))  
print(s1 ^ s2)
#测试是否 s 中的每一个元素都在 t 中  
s1.issubset(s2)  
s1 <= s2  
#测试是否 t 中的每一个元素都在 s 中
s1.issuperset(s2)  
s1 >= s2
