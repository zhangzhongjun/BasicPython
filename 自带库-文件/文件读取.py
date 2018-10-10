# coding=utf-8
try:
    f = open("f:\\tr.arff","r")
    print f.read(4)
    print f.readline(4)
    print f.readline(100)
    print f.readline(100)
    print f.readlines()
    
    f = open("f:\\test.txt","r")
    i=0
    for line in f:
        print u"第"+str(i)+u"行:"+Unicode.encode(line,'utf-8')        i += 1
finally:
    if f:
        f.close()
count=0
try:
    f = open("f:\\test.txt","r")
    print len(f.readlines())
    f = open("f:\\test.txt","r")
    print len(f.readlines(1))
    f = open("f:\\test.txt","r")
    print len(f.readlines(2))
    f = open("f:\\test.txt","r")
    print len(f.readlines(3))
    f = open("f:\\test.txt","r")
    print len(f.readlines(4))
finally:
    if f:
        f.close()
# io.DEFAULT_BUFFER_SIZE的大小决定了writelines()写入的行数
import io
print io.DEFAULT_BUFFER_SIZE

try:
    f = open("f:\\t1.txt","w")
    f.write("hello world")
    f.writelines(['1','2','3','4'])
finally:
    if f:
        f.close()

import os
try:
    fd = os.open("f:\\ttt.txt",os.O_CREAT)
    f = open("f:\\ttt.txt",'a')
    print fd
    print f
    print os.read(fd,4)
finally:
    os.close(fd)
    if f:
        f.close()
        
try:
    fd = os.open("f:\\mq.txt",os.O_CREAT | os.O_RDWR)
    os.write(fd,'hello world')
    str = u'张中俊'
    #os.write(fd,str.encode('utf-8'))
finally:
    os.close(fd)
    
import codecs
try:
    f = codecs.open('F:\\test.txt','w','utf-8')
    f.write(u'张中俊')
finally:
    if f:
        f.close