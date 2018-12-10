# coding=utf-8
#!/usr/bin/python


# 定义一个新的list

```python
L=['']
print (L,len(L),type(L))

L=['']*10
print (L,len(L),type(L))

#使用extend来扩展list
L1=[1,2,3]
L2=[12,23,23]
L1.extend(L2)
print L1


#使用加法扩展
print L1+L2

#使用shuffle来打乱list
import random
random.shuffle(L1)
print L1
```

# 格式化输出

```python
import pprint
a = [[1,2,3],[2,2],[12,1212],['hejji']]
pprint.pprint(a)
```

# 列表转字符串

```python
arr=["1","2","3"]
print(",".join(arr))
```

# 字符串转列表

```python
str3 = "www.google.com"  
list3 = str3.split(".")  
print list3 
```

# 排序

```python
str = "ad"
L=['a','l','o','u','d','e','r']
print L
#排序方法 py3中已被弃用
L.sort(key = str.find,reverse=True)
print L
```

# 生成排列组合

```python
import itertools
print len(list(itertools.product(L,repeat=2))),list(itertools.product(L,repeat=2))
```

# 列表是按照地址引用的，reference

```python
L=[1,23,23,213,2434,1234,23,23,42,55465,8768,34,123]
L1 = L
L1[1]='hello world'
print(L1,L)
```


# 使用deepcopy完成真正的赋值

```python
import copy
L2 = copy.deepcopy(L1)
L2[0]='bad world'
print L2,L1
```

# 字符串的len函数

```python
str='\r\n'
print len(str)
```

# list的__str__()函数

```python
print L.__str__()
```

# 相当于contains

```python
print ('Adam' in L)
print ('aa' in L)

```


# pop,remove,del

```python
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
```

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

```python
L = range(1,100,2)
a = [x*(x+1) for x in L]
print (a)
```


# 列表生成式中还可以加上if语句

```python
L = [x * x for x in range(1, 11) if x % 2 == 0]
print L
# 列表生成式中使用双重循环
L = [a*100+b*10+c for a in range(1,9,1) for b in range(0,9,1) for c in range(0,9,1) if a == c]
print L
print [a*100+b*10+c for a in range(1,9,1) for b in range(0,9,1) for c in range(0,9,1) if a==c]
```

# 使用列表生成式生成随机的list
```python
from random import randint
data = [randint(-10,10) for _ in xrange(10)]
print data
print filter(lambda x:x>0,data)
```

# 使用列表生成式完成filter的功能

```python
print [x for x in data if x>0]
print [x if x>0 else -x for x in data]
```
