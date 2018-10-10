# coding=utf-8
#!usr/bin/python

#高阶函数是指，可以接收函数作为参数的函数 可以返回一个函数的函数
import math
def add(x, y, f):
    return f(x) + f(y)
print add(25, 9, math.sqrt)

# map函数接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
def format_name(s):
    return s[0:1:1].upper()+s[1::1].lower()
print map(format_name, ['adam', 'LISA', 'barT'])

# reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
def prod(x, y):
    return x*y
print reduce(prod, [2, 4, 5, 7, 12],0)

# filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
def is_sqr(x):
    r = int(math.sqrt(x))
    return r*r==x
print filter(is_sqr, range(1, 101,1))

# sort()函数，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。
def cmp_ignore_case(s1, s2):
    t1 = s1.lower()
    t2 = s2.lower()
    if t1<t2:
        return -1;
    elif t1>t2:
        return 1;
    return 0;
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)