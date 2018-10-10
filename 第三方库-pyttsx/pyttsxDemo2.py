#-*- coding: UTF-8 -*-
import sys
import pyttsx

reload(sys)
sys.setdefaultencoding("utf-8")

text = u'你好，中文测试'
engine = pyttsx.init()
engine.say(text)
engine.runAndWait()