import os
import os.path 
if __name__ == '__main__':
    print os.path.exists(u"F:\\tr.arffs")
    fd = os.open('f:\\ttt.txt',os.O_CREAT|os.O_WRONLY)
    print fd
    os.write(fd,'hello world')
    os.close(fd)
    fd = os.open('f:\\ttt.txt',os.O_RDONLY)
    print fd
    str = os.read(fd,7)
    print str
    os.close(fd)
    os.remove("f:\\ttt.txt")
    
    fp = open('f:\\bdyy\\old\\A\\A Great Big World_15.txt','r')
    lines = fp.readlines()
    print len(lines)
    for line in lines:
        print line
    files = os.listdir('f:\\bdyy\\old\\A')
    print len(files)
    for file in files:
        print file
        
    for i in xrange(26):
        print chr(i+ord('A'))
    
    
