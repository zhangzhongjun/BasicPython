# coding=utf-8
#!usr/bin/python
# Python的 decorator 本质上就是一个高阶函数，它接收一个函数作为参数，然后，返回一个新函数。
def log(f):
    def fn(*args,**kw):
        print 'call ' + f.__name__ + '()...'
        return f(*args,**kw)
    return fn

@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)

@log
def add(x, y):
    return x + y
print add(1, 2)


import time
def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print 'call %s() in %f s' % (f.__name__, (t2 - t1))
        return r
    return fn

@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)

# 带参数的log函数首先返回一个decorator函数，再让这个decorator函数接收my_func并返回新函数
def log(prefix):
    def log_decorator(f):
        def wrapper(*args,**kw):
            print '[%s] calling %s...' %(prefix,f.__name__)
            return f(*args,**kw)
        return wrapper
    return log_decorator

@log('DEBUG')
def test():
    pass
print test()

@log("INFO")
def test():
    pass
print test()

def performance(danwei):
    def log_decorator(f):
        def wrapper(*args,**kw):
            begin = time.time()
            res = f(*args,**kw)
            end = time.time()
            lishi = end - begin
            print "call %s() in %f%s" %(f.__name__,lishi,danwei)
            return res
        return wrapper
    return log_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)

# 使用functools.wrap来保证让调用者看不出一个函数经过了@decorator的“改造”，
import time, functools
def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit=='ms' else (t2 - t1)
            print 'call %s() in %f %s' % (f.__name__, t, unit)
            return r
        return wrapper
    return perf_decorator

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial.__name__

# 使用functools.partial来简化函数设计
import functools

sorted_ignore_case = functools.partial(sorted,cmp=lambda s1,s2:cmp(s1.upper(),s2.upper()))

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])

# 使用property来定义一个属性
# @score.setter是@property的附属品，当对score赋值时候，调用这个方法
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property
    def grade(self):
        if self.score>=80:
            return "A"
        elif self.score >=60:
            return "B"
        else self.score <60:
            return "C"

s = Student('Bob', 59)
print s.grade

s.score = 60
print s.grade

s.score = 99
print s.grade