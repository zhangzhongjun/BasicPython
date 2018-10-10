# python2和python3的区别

```python
#coding=utf-8

#2.X中的字符串默认为byte，而3.X中的字符串默认为unicode
#在字符串前面加上b，表示这是ascii编码；加上u，表示这是unicode编码
#2.X中/将得到整数，//将得到浮点数
#3.X中/将得到浮点数,//将得到整数

from __future__ import division
from __future__ import unicode_literals
print 10/3
print 10//3
```


# 导包

3种不同的导包方式
```python
from numpy import *
直接使用numpy中定义的函数，如mat，T等
```
```python
import numpy
必需使用numpy.mat()才可以
```
```python
import numpy as np
可以使用缩写，如np.mat()
```

# range和xrange

```python
for i in range(1000):
	pass
```
会导致生成一个 1000 个元素的 List，而代码：
```python
for i in xrange(1000):
	pass
```
则不会生成一个 1000 个元素的 List，而是在每次迭代中返回下一个数值，内存空间占用很小。因为 xrange 不返回 List，而是返回一个 iterable 对象。


# 路径问题

```python
# 获取当前文件__file__的路径
print ("os.path.realpath(__file__)=%s" % os.path.realpath(__file__))
# 获取当前文件__file__的所在目录
print ("os.path.dirname(os.path.realpath(__file__))=%s" % os.path.dirname(os.path.realpath(__file__)))
# 获取当前文件__file__的所在目录
print ("os.path.split(os.path.realpath(__file__))=%s" % os.path.split(os.path.realpath(__file__))[0])
# 获取父亲目录
print (os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir)))

# 文件或文件夹是否存在
os.path.exists(savedir)

# 创建多级别目录
os.makedirs(savedir) 

#获得当前py文件的路径
os.path.dirname(__file__)

#对路径进行分隔，分隔为两部分，第一部分是路径，第二部分是文件名
p = os.path.split(os.path.realpath(__file__))
p = str(p[0])
print(p)

#对路径进行连接，第一个参数是路径，第二个参数是文件名
path = path.join(d, "alice_mask.png")

```

# 下载小文件 图片等

```python
import requests
response = requests.get(url)
response.encoding='utf-8'
with open(p,'wb') as ft:
  ft.write(response.content)
  ft.close
```

# 清洗掉Windows系统非法文件夹名字

```python
def strip(path):
    """
    :param path: 需要清洗的文件夹名字
    :return: 清洗掉Windows系统非法文件夹名字的字符串
    """
    path = re.sub(r'[？\\*|“<>:/]', '', str(path))
    return path
```

# 判断平台

```python
#换行符：都使用\n就可以了，windows平台会自动的进行转化
my_os = platform.system()
if my_os=="Windows":
    dbFilePath = "F://睿云实验室//王剑锋//关键词检索//第3阶段工作-搞数据//弄好的数据库//zhengli.db"
    outputPath = "F://睿云实验室//王剑锋//关键词检索//第3阶段工作-搞数据//弄好的数据库//ciPing.txt"
    inputPath = "F://睿云实验室//王剑锋//关键词检索//第3阶段工作-搞数据//弄好的数据库//ciPing"
    print("you are in windows")
else:
    dbFilePath = "/home/controller/ZhengLiEDRM/database_26.db";
    dbFilePath2 = "/home/controller/ZhengLiEDRM/zhengli.db"
    print("you are in linux")
```

# 画图工具

```python
#先加载画图需要用的包
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.style.use('ggplot')
plt.figure(figsize=(12,6))
plt.plot(x,yHat2,'r')
plt.scatter(x,y)
# 保存图片到指定路径  
plt.savefig("../data/HeightAndWeight.png")
# 展示
plt.show()

```

# 换行符问题
直接使用`\n`，windows会帮你替换为`\r\n`

# 依赖

1. 安装pipreqs
  `pip install pipreqs`
2. 进入项目所在的目录，生成requirements.txt文件
  `pipreqs --encoding utf-8 --force  ./`
3. 使用requirements.txt文件
  `pip install -r requirements.txt`

# pip源
```cmd
pip install web.py -i https://pypi.tuna.tsinghua.edu.cn/simple
-i https://linux.xidian.edu.cn/mirrors/pypi/web/simple/
```

# scrapy

> 参考我的另外一个仓库：https://github.com/zhangzhongjun/Crawler-ScrapyLearn

文档：https://docs.scrapy.org/en/latest/topics/commands.html

创建项目
```cmd
scrapy startproject tutorial
```
创建spider
```cmd
cd tutorial
scrapy genspider example example.com
```
运行spider
```cmd
scrapy crawl quotes
```
保存结果
```cmd
保存为json格式：scrapy crawl quotes -o quotes.json
保存成json line格式：scrapy crawl quotes -o quotes.jl
```
