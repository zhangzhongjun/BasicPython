#coding=utf-8
a,b = 123,'world'
print a,b

#利用多重赋值来实现交换
a,b = b,a
print a,b

def gcd(a,b):
    while a!=0:
        a,b = b%a,a
    return b
    
print gcd(24,30)
print gcd(409119243,87780243)
print gcd(30,24)
print gcd(87780243,409119243)