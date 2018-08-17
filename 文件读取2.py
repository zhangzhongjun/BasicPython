# coding=utf-8

f = open("f:\\Gowalla_totalCheckins.txt","r")
f2 = open("f:\\Gowalla_100050.txt",'w')
i=0
for i in range(0,1000100):
    line = f.readline(i)
    f2.write(line)
f.close()
f2.close()