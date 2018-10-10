# windows下

pycrypto，pycrytodome和crypto是一个东西，在很久以前，crypto在python上面的名字是pycrypto它是一个第三方库，但是已经停止更新三年了，所以不建议安装这个库；

windows下python3.6安装也不会成功！
这个时候pycryptodome就来了，它是pycrypto的延伸版本，用法和pycrypto 是一模一样的；

重点：
直接pip install pycryptodome
successfully.........................................................................................................
但是，在使用的时候导包是有问题的，这个时候只要修改一个文件夹的名称就可以完美解决这个问题，beautiful !!!!!
C:\Users\Administrator\AppData\Local\Programs\Python\Python36\Lib\site-packages
找到这个路径，下面有一个文件夹叫做crypto,将c改成C，对就是改成大写就ok了！！！

网上有很多教程都是扯犊子的，就这种最简单，最靠谱

# centos下

```bash
pip install pycrypto
```

但是由于pycrypto年久失修，所以会出问题，列如AES的某种加密模式不存在

还是建议使用pycryptodome库

```bash
pip install pycryptodome
```