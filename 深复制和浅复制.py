# coding=utf-8
''''' 
一、深拷贝、浅拷贝 
Python中的对象之间赋值时是按引用传递的，如果需要拷贝对象，需要使用标准库中的copy模块。 
1. copy.copy 浅拷贝 只拷贝父对象，不会拷贝对象的内部的子对象。 
2. copy.deepcopy 深拷贝 拷贝对象及其子对象 
对于一般的浅拷贝,使用copy.copy就可以了 
 
如果要复制一个对象o,它属于内建的类型t,那么可以使用t(o)来获得一个拷贝:
    要复制列表L,使用list(L)
    要复制一个字典d,使用dict(d)
    要复制一个集合s,使用set(s)
    dict也提供了一个复制版本,dict.copy,这个和dict(d)是一样, 
二、is、== 
Python中的对象包含三要素：id、type、value 
其中id用来唯一标识一个对象，type标识对象的类型，value是对象的值 
is 判断的是a对象是否就是b对象，是通过id来判断的 
== 判断的是a对象的值是否和b对象的值相等，是通过value来判断的 
'''  
  
import copy  
a = [1, 2, 3, 4, ['a', 'b']]# 原始对象  
b = a                       # 赋值，传对象的引用，完全相等改变  
print a is b #True  
print a == b #True  
  
c = copy.copy(a)            # 对象拷贝 浅拷贝，子对象的值跟着变，父对象值不变  
d = list(a)  
e = a[:]  
print a is c #False  
print a == c #True  
  
f = copy.deepcopy(a)        # 对象拷贝，深拷贝，两个对象完全没关系  
print a is f #False  
print a == f #True  
  
a.append(5)                 # 修改父对象a  
a[4].append('c')            # 修改对象a中的子对象['a', 'b']  
  
print 'a = ', a             # a = [1, 2, 3, 4, ['a', 'b', 'c'], 5]  
print 'b = ', b             # b = [1, 2, 3, 4, ['a', 'b', 'c'], 5]  
print 'c = ', c             # c = [1, 2, 3, 4, ['a', 'b', 'c']]   
print 'd = ', d             # d = [1, 2, 3, 4, ['a', 'b', 'c']]  
print 'e = ', e             # e = [1, 2, 3, 4, ['a', 'b', 'c']]  
print 'f = ', f             # f = [1, 2, 3, 4, ['a', 'b']]