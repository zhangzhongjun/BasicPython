# coding=utf-8
#!/usr/bin/python
def f():
    print 'call f()...'
    # 定义函数g:
    def g():
        print 'call g()...'
    # 返回函数g:
    return g
x = f()
x()

# 利用返回函数的函数来延迟计算
def calc_prod(lst):
    def mul(x,y):
        return x * y;
    def prod():
        return reduce(mul,lst,1)
    return prod

f = calc_prod([1, 2, 3, 4])
print f()


# 像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）。

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print f1()
print f2()
print f3()
# 要正确使用闭包，就要确保引用的局部变量在函数返回后不能变
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

# 匿名函数有个限制，就是只能有一个表达式，不写return，返回值就是该表达式的结果。
print sorted([1, 3, 9, 5, 0], lambda x,y: -cmp(x,y))
# 返回函数的时候，也可以返回匿名函数
myabs = lambda x: -x if x < 0 else x 
print myabs(-1)
print myabs(1)

def is_not_empty(s):
    return s and len(s.strip()) > 0
print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])

print filter(lambda s:s and len(s.strip())>0,['test', None, '', 'str', '  ', 'END'])