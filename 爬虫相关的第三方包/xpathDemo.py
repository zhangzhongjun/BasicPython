# coding=utf-8

from lxml import etree

ss = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>建立测试网址文本</title>
    </head>
    <body>
        <div id="content" version="1.0">
        <ul id="useful">
            <li>数学建模方法</li>
            <li>数学建模数据</li>
            <li>数学建模软件</li>
        </ul>
        <ul id="useless">
            <li>不需要的信息１</li>
            <li>不需要的信息２</li>
            <li>不需要的信息３</li>
        </ul>
        <span name="data">
            <book>
                <title lang="eng">数学建模书籍1</title>
                <price>29.99</price>
            </book>
            <book>
                <title lang="eng">数学建模书籍2</title>
                <price>39.95</price>
            </book>
            <div id="url">
                <a href="http:nveyun.com">虐云建模网</a>
                <a href="http://nveyun.com/forum.php" title="虐云建模论坛">建模论坛</a>
            </div>
        </span>
    </body>
</html>
 """


selector = etree.HTML(ss)

#a.提取文本
content = selector.xpath('//ul[@id="useful"]/li/text()')
for each in content:
    print ('each:',each)

#b.提取属性
link = selector.xpath('//a/@href')
for href in link:
    print ('href:',href)


#c.提取title
title = selector.xpath('//a/@title')
print ('title[0]:',title[0])


#c.提取多层字符
data = selector.xpath('//span[@name="data"]')[0]
#二进制数'\r\n'
info = data.xpath('string(.)')
content=info.replace('\r\n', '').replace(' ', '')
print('content:',content)

#提取book对应的数据
book=selector.xpath('//title[@lang="eng"]/text()')
print('book:',book)

#仅提取所需的book数据
book1=selector.xpath('//book[1]/title[@lang="eng"]/text()')
print('book1:',book1)

#使用last函数，其表示最后一个book子元素。[last()-1]：表示选择的倒数第二个book子元素
book_last=selector.xpath('//book[last()]/title[@lang="eng"]/text()')
print('book_last:',book_last)

#[position()<3] ：表示选择前两个book子元素
book_p=selector.xpath('//book[position()<3]/title[@lang="eng"]/text()')
print('book_p:',book_p)

#//title[@lang] 表示选择所有具有lang属性的title节点。
lang=selector.xpath('//title[@lang]/text()')
print('lang',lang)

#select price>35 ,book下面的两个标签一个price一个title,如果为//span/book[price>35.00]则选择的是所有 book 元素，
#且其中的 price 元素的值须大于 35.00。
price_35=selector.xpath('//span/book[price>35.00]/title/text()')
print('price_35:',price_35)

#=符号要求属性完全匹配
#部分匹配可以用contains,如：<div id="content" version="1.0"> 版本1.0
denghao=selector.xpath('//*[@id="content"]/text()')[0].replace('\r\n','')
print('denghao:',denghao)
contains=selector.xpath('//*[contains(@id,"content")]/text()')[0].replace('\r\n','')
print('contains:',contains)

#运算符：and 和 or   【@class='a'  or @class='b'】
operators1=selector.xpath('//div[@id="content"]//*[self::ul[@id="useful"]/li or self::span]/text()')
print('operators1:',operators1)
operators2=selector.xpath('//div[@id="content"]//*[self::li or self::span]/text()')
print('operators2:',operators2)
