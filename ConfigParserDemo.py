# coding=utf-8
'''
    ConfigParser.ConfigParser()获得ConfigParser对象
    read() 加载配置文件
    sections() 以列表的格式返回Sections
    items(section) 以列表的格式返回指定Sections下的items [('name', 'John'), ('age', '12')]由map组成的list，每个map是一个item
    set(section,key,value) 添加或者修改一个item
    add_section(section) 添加一个section
    remove_option(section,key) 删除一个item
    remove_section(section) 删除一个section
    write(file) 将配置文件写入文件中

    [userinfo]
    name = John
    age = 12

    [study]
    os = 100
    ds = 93    
'''
import ConfigParser

class student_info(object):
    def __init__(self,recordfile):
        self.logfile = recordfile
        self.cfg = ConfigParser.ConfigParser()
    def cfg_load(self):
        self.cfg.read(self.logfile)
    def cfg_dump(self):
        se_list = self.cfg.sections()
        print '================================================='
        for se in se_list:
            print se
            print self.cfg.items(se)
        print '================================================='
    def delete_item(self,section,key):
        self.cfg.remove_option(section,key)
    def delete_section(self,section):
        self.cfg.remove_section(section)
    def add_section(self,section):
        self.cfg.add_section(section)
    def add_item(self,section,key,value):
        self.cfg.set(section,key,value)
    def save(self):
        fp = open(self.logfile,'a')
        self.cfg.write(fp)
        fp.close()

if __name__ == '__main__':        
    si = student_info('f:\\stuinfo.txt')
    si.add_section('userinfo')
    si.add_section('study')
    si.add_item('userinfo','name','John')
    si.add_item('userinfo','age','12')
    si.add_item('study','os','100')
    si.add_item('study','ds','93')
    si.save()
    si.cfg_dump()