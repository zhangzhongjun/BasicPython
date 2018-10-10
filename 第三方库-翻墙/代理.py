# encoding=utf-8
import requests

url='http://www.youtube.com'
r = requests.get(url,timeout=10,proxies = {"http" : 'http://127.0.0.1:1080'})
print r