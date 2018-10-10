# coding=utf-8
import threading
from time import ctime,sleep
'''
    前台线程：主线程运行完毕，前台线程不会结束
    后台线程：主线程运行完毕，后台线程随机结束
    join：阻塞父亲线程，儿子死后，父亲才能死
'''
def music(func):
    for i in range(10):
        print u"%s I was listening to %s. %s \r\n" %(threading.current_thread().name,func,ctime())
        sleep(5)
        
def move(func):
    for i in range(10):
        print u"%s I was at the %s! %s\r\n" %(threading.current_thread().name,func,ctime())
        sleep(5)
        

threads = []
# 注意参数里的逗号不能省略
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=move,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    print "start:",ctime()
    for t in threads:
        #如果不设置为守护线程程序会被无限挂起。子线程启动后，父线程也继续执行下去
        t.setDaemon(False)
        t.start()
    for t in threads:
        pass
        #t.join()
    print "all over %s\r\n" %ctime()
    print "end:",ctime()
    