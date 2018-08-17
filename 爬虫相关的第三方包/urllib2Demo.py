# coding=utf-8
import urllib2,cookielib

url = 'http://www.baidu.com'
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36'
response = urllib2.urlopen(url)
print response.getcode()
print len(response.read())

request = urllib2.Request(url)
request.add_header('User-Agent',User_Agent)
response = urllib2.urlopen(request)
print response.getcode()
print len(response.read())

cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response = urllib2.urlopen(url)
print response.getcode()
print len(response.read())
print cj

url = "http://music.baidu.com/artist"
response = urllib2.urlopen(url)
print response.getcode()
print len(response.read())


url = 'http://www.baidu.com'
request = urllib2.Request(url)
request.add_data({"a",1})
request.add_data({"param",urllib2.quote('中文')})
print request.getUrl()