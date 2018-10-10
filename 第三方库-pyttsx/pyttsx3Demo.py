# coding=utf-8
import pyttsx3;

print (pyttsx3.voice.Voice.languages)
engine = pyttsx3.init()
#控制语速
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.say("I will speak this text 哈哈哈哈哈");
engine.say("我最近喜欢听红色高跟鞋")
engine.runAndWait() ;