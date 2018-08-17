# coding=utf-8
import os
import codecs
# 去掉重复的
def quChong(filepath1,filepath2):
    fp = codecs.open(filepath1,'r','utf-8')
    lines = fp.readlines()
    L = []
    for line in lines:
        line = line.strip()
        L.append(line)
    S = set(L)
    if len(S)==len(L):
        return 
    else:
        print filepath1
        fp2 = codecs.open(filepath2,'w','utf-8')
        for s in S:
            fp2.write(s+"\r\n")
        fp2.close()
    fp.close()    

def getDirName(i,str):
    index = chr(i+ord('A'))
    return 'f:\\bdyy\\'+str+'\\'+index

if __name__ == "__main__":
    for i in range(0,26,1):
        filenames = os.listdir(getDirName(i,"old"))
        for filename in filenames:
            filepath1 = getDirName(i,"old")+"\\"+filename
            filepath2 = getDirName(i,"new")+"\\"+filename
            quChong(filepath1,filepath2)
                