# encoding=utf-8
import os
import codecs
def getPath(i):
    index = chr(i+ord('A'))
    return 'f:\\bdyy\\old\\'+index
#打印出所有的有重复的文件的路径
count = 0
count2 = 0
for i in range(0,26,1):
    dir = getPath(i)
    filenames = os.listdir(dir)
    for filename in filenames:
        filepath = dir+"\\"+filename
        try:
            fp = codecs.open(filepath,'r','utf-8')
        except:
            count = count+1
            print filepath
        else:
            lines = fp.readlines()
            L = []
            for line in lines:
                line = line.strip()
                if line in L:
                    print filepath
                    count2 = count2 + 1
                    break
                L.append(line)
print count
print count2