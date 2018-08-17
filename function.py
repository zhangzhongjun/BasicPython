# coding=utf-8
#!/usr/bin/python
import math

def quadratic_equation(a,b,c):
    delta = b*b-4*a*c
    res1 = (-b + math.sqrt(delta))/(2*a)
    res2 = (-b - math.sqrt(delta))/(2*a)
    return (res1,res2)
print quadratic_equation(2, 3, 0)
print quadratic_equation(1, -6, 5)

i = 1
L=[]
while i<=100:
    L.append(i*i)
    i = i + 1
print L
print sum(L)

def square_of_sum(L):
    res = 0
    for i in L:
        res = res + (i*i)
    return res
print square_of_sum([1, 2, 3, 4, 5])
print square_of_sum([-5, 0, 5, 15, 25])

# 多个变量可以接收同一个tuple，然后按照位置赋值
a,b=('aaa','bbb')
print a
print b

def move(n, a, b, c):
    if n ==1:
        print a, '-->', c
        return
    move(n-1,a,c,b)
    print a, '-->', c
    move(n-1,b,a,c)
move(4, 'A', 'B', 'C')

def greet(a='world'):
    print "Hello, "+a+"."
greet()
greet("john")

def average(*args):
    if(len(args)==0):
        return 0
    sum = 0.0
    for i in args:
        sum = sum + i
    return sum/len(args)

print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)