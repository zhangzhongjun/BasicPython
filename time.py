# coding=utf-8

import time

#精确到千分之一秒
print (time.time())

print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )

# 程序休眠10 s
time.sleep(10)
