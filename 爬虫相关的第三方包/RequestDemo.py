# coding=utf-8
import requests
value={
    "p":1,
    'q':'牛子裤',
    'version':'2017071708'
}
headers={
    "a":"a",
    "b":"b"
}
url = 'http://info.goaloo.com/jsData/matchResult/2014/c109.js'
res = requests.get(url,params=value,headers=headers)
res.encoding='utf-8'
print res.url
print res.status_code
print res.text

proxies = {'https':'socks5://92.223.72.173:1080'}
res = requests.get('https://www.facebook.com',proxies=proxies)
print res.url
print res.status_code
print res.text

res = requests.post(url,data=value,headers=headers)