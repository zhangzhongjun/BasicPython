# coding=utf-8

'''
    1.字符串在Python内部的表示是unicode编码
    2.在做编码转换时，通常需要以unicode作为中间编码，即先将其他编码的字符串解码（decode）成unicode，再从unicode编码（encode）成另一种编码
    3.decode的作用是将其他编码的字符串转换成unicode编码，如str1.decode('gb2312')，表示将gb2312编码的字符串str1转换成unicode编码
    4.encode的作用是将unicode编码转换成其他编码的字符串，如str2.encode('gb2312')，表示将unicode编码的字符串str2转换成gb2312编码
    5.代码中字符串的默认编码与代码文件本身的编码一致
    6.不能对unicode进行解码
    7.不能对非unicode的字符串进行编码
    8.
'''
str1  = '㑂彿'
str2 = '㑂佛'
print repr(str1),repr(str2)

str3="中国"
str4 = unicode(str3,'utf8')
print type(str3),type(str4)

'''
    实现对s进行gb2312编码
    1.如果s是unicode编码，直接encode
    2.如果s是非unicode编码，先decode，在encode
'''
s="中文"

if isinstance(s, unicode):
    print s.encode('gb2312')
else:
    print s.decode('utf-8').encode('gb2312')

b = b"example"
  
# str object
s = "example"    
  
# str to bytes    
bytes(s, encoding = "utf8")    
  
# bytes to str    
str(b, encoding = "utf-8")    
  
# an alternative method    
# str to bytes    
str.encode(s)    
  
# bytes to str    
bytes.decode(b) 

