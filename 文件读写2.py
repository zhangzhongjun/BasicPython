# coding=utf-8

#
# year 1 bits
# month date hour 5 bits
# minute second 6 bits
#

import codecs
path = 'F:\\notexits.txt'
f = codecs.open(path,'a','utf-8')
f.writelines(["aa","bb","cc","dd"])
f.close


#在文件的开头插入数据
with open(path, "r+") as f:
     old = f.read()
     
     
     f.seek(0)
     f.write("hello world\n")
     f.write(old)
     
for str in ["aa","bb","cc"]:
    print(str)