# coding=utf-8
#!/usr/bin/python
'''
	tuple是有顺序的
'''
#相当于是一个不能变化的list
T = ('Adam','John','Bart')
print T
T = (1,2,3,4,5,6,7,8,9,10)
print T

#单元素tuple需要加一个额外的逗号
T = (1,)
print T
T = ('Adam',)
print T
#元组中的元素是不能变化的
T = ('a','b',['A','B'])
L = T[2]
L[0] = 'X'
L[1] = 'Y'
print T
T = ('a','b',('A','B'))
print T
