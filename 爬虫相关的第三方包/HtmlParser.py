# coding=utf-8
import re
from bs4 import BeautifulSoup
class HtmlParser(object):

    def __getNewUrls__(self,page_url,soup):
        new_urls = set()
        # /artist/4840
        nodes = soup.find_all("a",href=re.compile(r"/artist/\d+"))
        for node in nodes:
            new_url = node['href']
            new_completeUrl = "http://music.baidu.com"+new_url
            #new_urls.add(new_completeUrl)
        return new_urls

    def __getNewDatas__(self,page_url,soup):
        new_datas = []
        # /artist/4840
        nodes = soup.find_all("a",href=re.compile(r"/artist/\d+"))
        for node in nodes:
            name = node.text
            new_url = node['href']
            new_completeUrl = "http://music.baidu.com"+new_url
            new_datas.append({u"姓名":name,u"网站":new_completeUrl})
        return new_datas
       
    '''
        page_url:当前正在解析的网页
        html_cont:正在解析的网页上的内容
    '''    
    def parse(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls = self.__getNewUrls__(page_url,soup)
        new_datas = self.__getNewDatas__(page_url,soup)
        return new_urls,new_datas
        
