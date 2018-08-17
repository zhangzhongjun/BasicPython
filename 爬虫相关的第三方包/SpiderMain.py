# coding=utf-8
import UrlManager,HtmlDownloader,HtmlParser,HtmlOutputer

class SpiderMain(object):
    def __init__(self):
        self.urls = UrlManager.UrlManager()
        self.downloader = HtmlDownloader.HtmlDownloader()
        self.parser = HtmlParser.HtmlParser()
        self.outputer = HtmlOutputer.HtmlOutputer()
    
    def craw(self,root_url):
        self.urls.add_new_url(root_url)
        i = 0
        while self.urls.has_new_url():
            new_url = self.urls.get_new_url()
            html_con = unicode(self.downloader.download(new_url),"utf-8")
            new_urls,new_datas = self.parser.parse(new_url,html_con)
            self.urls.add_new_urls(new_urls)
            self.outputer.collect_datas(new_datas)
            
            print "craw"+str(i)+": "+new_url
        self.outputer.output_html()
        

if __name__ == "__main__":
    root_url = "http://music.baidu.com/artist"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
    
    