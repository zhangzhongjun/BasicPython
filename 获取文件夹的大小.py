import os, re 
"""
查看文件夹下的所有文件及文件夹 join为拼接函数
"""
def Look_File(path):
  for root , dirs, files in os.walk(path, True):
    print( root)     #主目录
    for item in files: #主目录下的文件夹
      print (os.path.join(root, item))
"""
计算文件夹 大小
"""   
def FileSize(path):
  size = 0
  for root , dirs, files in os.walk(path, True):
    size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    #目录下文件大小累加
    return size
if __name__ == '__main__':
  Look_File("f:\\vba")
  print (FileSize("f:\\vba"))