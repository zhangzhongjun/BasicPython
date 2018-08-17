# coding=utf-8
#!/usr/bin/python
for i in range(101):
    if(i%7==0):
        print i

L = ['Adam', 'Lisa', 'Bart', 'Paul']
s = range(1,len(L)+1,1)
a = zip(L,s)
for name,index in a:
    print index,"-",name