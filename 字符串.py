# coding=utf-8
#!/usr/bin/python

spam = bytes([104, 101, 108, 108, 111])
s = spam.decode('ascii')
print s,type(s)

s = r'http://music.baidu.com/artist/707709'
print s.split('/')
print s.split('/')[4]
print "I'm John"
print 'learn "python" in imooc'
print 'Bob Saib:\"I\'am a student\"'
print "Bob \n Alice \n John \n Mike"
print "Bob \t Alice \t John \t Mike"
print "Bob \\ Alice \\ John \\ Mike"

s = 'Python was started in 1989 by "Guido"\nPython is free and easy to learn.'
print s

# 在字符串前面加上r表示这是一个raw字符串
s = r'\(~_~)/ \(~_~)/'
print s

s = '''python is created by "Guido".
It is free and easy to learn.
Let's start learn Python in imooc!'''
print s

s = r'''"to be or not to be":that's the question.Whether it's nobler in the mind to suffer.'''
print s

s = u'我是中文，我前面加u'
print s
print "=============================================================="
s = ur'我是中文，我前面加"u"'
print s
print "=============================================================="
s = ur'''第一行
第二行
第三行
第四行
'''
print s
print "=============================================================="
s = ur'''
静月思
床前明月光
疑是地上霜
举头望明月
低头思故乡
'''
print s
print "=============================================================="
L = ["Hello","World",12]
for i in L:
    print isinstance(i,str)
    print isinstance(i,int)
    