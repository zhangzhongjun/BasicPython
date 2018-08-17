# coding=utf-8
"""-----------------------------------------------------------------------------
    使用HTTPS调用飞信接口:
    https://quanapi.sinaapp.com/fetion.php?
    u=飞信登录手机号&p=飞信登录密码&to=接收飞信的手机号&m=飞信内容
    返回结果为Json格式，result=0时表示发送成功
    {“result”:0,”message”:”\u53d1\u9001\u6210\u529f”}
-----------------------------------------------------------------------------"""
import requests

url = "https://quanapi.sinaapp.com/fetion.php"
parameter = {
    'u':'18835109707',
    'p':'zhang1968311',
    'to':'18835109707',
    'm':'张中俊发送，由飞信代发。。。'
}
r = requests.get(url,params=parameter)
r.encoding='utf-8'
print r.content
print r.url