# coding=utf-8
from bs4 import BeautifulSoup

html_doc=u'''
<html>
    <li>所在板块：<span>西青李七庄</span></li>
    <li class="li-b">总户数：<span>暂无数据</span></li>
    <li>绿化率：<span>20%（绿化率适中）</span></li>
    <li class="li-b">停车位：<span>暂无数据</span></li>
    <li>物业类型：<span>暂无数据</span></li>
    <li class="li-b">竣工时间：<span>2010年</span></li>
</html>  
'''
def bk(item):
    return item.find(u"所在")!=-1
import re
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
node = soup.find("li")
print node
print node.contents

html_doc = """
<html>
  <head>
    <title>The Dormouse's story</title>
  </head>
  <body>
    <p class="title">
      <b>The Dormouse's story</b>
    </p>
    <p class="story">Once upon a time there were three little sisters; and their names were 
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>, 
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; and they lived at the bottom of a well.</p>
    <p class="story">...</p>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
# 带一个或多个attrs
for link in soup.find_all('a',class_='sister'):
    print link.name,link['href'],link['class'],link['id'],link.text
for link in soup.find_all('a',class_='sister',id='link1'):
    print link.name,link['href'],link['class'],link['id'],link.text
# 不带attrs
print soup.find_all("title")
# [<title>The Dormouse's story</title>]
# 只带attr
print soup.find_all(class_='sister')


soup.find_all("p", "title")
# [<p class="title"><b>The Dormouse's story</b></p>]

# 不带attrs的
soup.find_all("a")
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
soup.find_all(id="link2")
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

# 使用正则表达式 可以自定义正则表达式
import re
soup.find(text=re.compile("sisters"))
# u'Once upon a time there were three little sisters; and their names were\n'
def has_six_characters(css_class):
    return css_class is not None and len(css_class) < 6
for node in soup.find_all(class_=has_six_characters):
    print node
    
html_doc = '''
<div class="lemma-summary" label-module="lemmaSummary">
<div class="para" label-module="para">Python<sup>[1]</sup><a class="sup-anchor" name="ref_[1]_21087">&nbsp;</a>
（英国发音：/ˈpaɪθən/ 美国发音：/ˈpaɪθɑːn/）, 是一种面向对象的解释型计算机程序设计语言，由荷兰人Guido van Rossum于1989年发明，第一个公开发行版发行于1991年。</div><div class="para" label-module="para">Python是纯粹的自由软件， 源代码和解释器CPython遵循 GPL(GNU General Public License)协议<sup>[2]</sup><a class="sup-anchor" name="ref_[2]_21087">&nbsp;</a>
。</div><div class="para" label-module="para">Python语法简洁清晰，特色之一是强制用空白符(white space)作为语句缩进。</div><div class="para" label-module="para">Python具有丰富和强大的库。它常被昵称为胶水语言，能够把用其他语言制作的各种模块（尤其是C/C++）很轻松地联结在一起。常见的一种应用情形是，使用Python快速生成程序的原型（有时甚至是程序的最终界面），然后对其中<sup>[3]</sup><a class="sup-anchor" name="ref_[3]_21087">&nbsp;</a>
有特别要求的部分，用更合适的语言改写，比如3D游戏中的图形渲染模块，性能要求特别高，就可以用C/C++重写，而后封装为Python可以调用的扩展类库。需要注意的是在您使用扩展类库时可能需要考虑平台问题，某些可能不提供跨平台的实现。</div>
</div>
'''
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
nodes = soup.find_all("div",class_='para')
print len(nodes)
    
html_doc = '''
<li data-songitem="{&quot;yyr_song_id&quot;:&quot;0&quot;,&quot;songItem&quot;:{&quot;sid&quot;:&quot;100575177&quot;,&quot;author&quot;:&quot;\u859b\u4e4b\u8c26&quot;,&quot;sname&quot;:&quot;\u4f60\u8fd8\u8981\u6211\u600e\u6837&quot;,&quot;pay_type&quot;:&quot;0&quot;}}" class="  bb-dotimg clearfix   song-item-hook   csong-item-hook   "><div class="song-item"><span class="index-num index-hook" style="width: 25px;">01</span><span class="song-info "></span><!-- 设置截断长度，考虑到有热门歌曲后会跟一个hot标签，需要做相应处理 --><span class="fun-icon">

    <span class="music-icon-hook" data-musicicon="{&quot;id&quot;:&quot;100575177&quot;,&quot;type&quot;:&quot;song&quot;,&quot;iconStr&quot;:&quot; play add download send collects&quot;,&quot;moduleName&quot;:&quot;songIcon&quot;,&quot;searchValue&quot;:null,&quot;yyr_song_id&quot;:&quot;0&quot;,&quot;pay_type&quot;:&quot;0&quot;,&quot;kr_top&quot;:0,&quot;is_jump&quot;:0,&quot;playFee&quot;:false,&quot;albumId&quot;:&quot;93104033&quot;,&quot;siPresaleFlag&quot;:&quot;0&quot;,&quot;downFee&quot;:false,&quot;songPic&quot;:&quot;http:\/\/musicdata.baidu.com\/data2\/pic\/246669444\/246669444.jpg@s_0,w_180&quot;,&quot;songTitle&quot;:&quot;\u4f60\u8fd8\u8981\u6211\u600e\u6837&quot;,&quot;songPublishTime&quot;:&quot;2013-11-11&quot;}">

        <a class="list-micon icon-play" data-action="play" title="播放你还要我怎样" href="javascript:;"></a>

        <a class="list-micon icon-add" data-action="add" title="添加你还要我怎样" href="javascript:;"></a>

        <a class="list-micon icon-download" data-action="download" title="下载你还要我怎样" href="javascript:;"></a>

        <a class="list-micon icon-send" data-action="send" title="下载到手机你还要我怎样" href="javascript:;"></a>
        </span>
    </span>
    <span class="song-title " style="width: 185px;">
        <a href="/song/100575177" target="_blank" title="薛之谦《意外》你还要我怎样" data-film="null">你还要我怎样</a><a title="歌曲MV" target="_blank" href="/mv/100575177" class="mv-icon"></a></span><span class="album-title" style="width: 130px;"><a target="_blank" href="/album/93104033" title="意外">意外</a></span><span class="hot-info" style="width:100px;"><span class="hot-num">19,692,053 </span><span class="hot-bar" style="width:100px;"><span class="hot-bar-inner" style="width:100px"></span></span></span></div></li>
'''
import re
soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8')
node = soup.find("li",class_=" bb-dotimg clearfix ")
print "======================"
print node
node = node.find('span',class_='song-title')
print "======================"
print node
node = node.find('a',href=re.compile(r'/song/\d+'))
print "======================"
print node

n = soup.find("li",class_=" bb-dotimg clearfix song-item-hook csong-item-hook ").find('span',class_='song-title').find('a',href=re.compile(r'/song/\d+'))
print "======================"
print n

n = soup.find("li",class_=" bb-dotimg clearfix song-item-hook csong-item-hook ").find('span',class_='song-title ').find('a',href=re.compile(r'/mv/\d+'))
print "======================"
print n

