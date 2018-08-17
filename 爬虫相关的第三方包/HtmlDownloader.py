# coding=utf-8
import urllib2
class HtmlDownloader(object):
    def download(self,url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
        
import codecs
if __name__ == "__main__":
    hd = HtmlDownloader()
    res = hd.download("http://www.baidu.com")
    res = unicode(res,'utf-8')
    f = codecs.open("f:\\baidu.html","w","utf-8")
    f.write(res)
    f.close()