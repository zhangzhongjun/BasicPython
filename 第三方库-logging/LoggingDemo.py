# coding=utf-8
import logging

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='f:\\myapp.log',
                filemode='w')
s = u'张三'
logging.debug(u'This is debug message 张中俊')
logging.info('This is info message')
logging.info(s)
logging.warning('This is warning message')