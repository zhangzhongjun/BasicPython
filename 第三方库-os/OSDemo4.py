# coding=utf-8
import os
import codecs
# 去掉重复的 直接覆盖
def quChong(filepath1):
    fp = codecs.open(filepath1,'r','utf-8')
    lines = fp.readlines()
    L = []
    for line in lines:
        line = line.strip()
        L.append(line)
    S = set(L)
    if len(S)==len(L):
        fp.close()
        return 
    else:
        fp.close() 
        print filepath1
        fp = codecs.open(filepath1,'w','utf-8')
        for s in S:
            fp.write(s+"\r\n")
        fp.close()
       

def getDirName(i,str):
    index = chr(i+ord('A'))
    return 'f:\\bdyy\\'+str+'\\'+index

if __name__ == "__main__":
    for i in range(0,26,1):
        filenames = os.listdir(getDirName(i,"old"))
        for filename in filenames:
            filepath = getDirName(i,"old")+"\\"+filename
            quChong(filepath)
                