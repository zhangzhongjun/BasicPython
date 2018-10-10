# coding=gb2312
import pyttsx
engine = pyttsx.init()
#控制语速
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.say(u'你好啊 The quick brown fox jumped over the lazy dog.')
engine.say(u'我最近喜欢听Life is a strugle')
engine.runAndWait()