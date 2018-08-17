# coding=utf-8
import codecs
import sys
import json
fin = codecs.open("F:\\t1.json",'r','utf-8')
try:
    d = json.load(fin)
except:
    info=sys.exc_info()  
    print info[0],":",info[1]
else:
    info = d[u"data"][u"info"]
    print type(info)
    print len(info)
    i =1
    while i<28:
        theInfo = info[i]
        print theInfo[u'title']
        i = i+1
        singers = theInfo[u'singer']
        print len(singers)
        
finally:
    fin.close()