#coding=utf-8
'''
用户名
18835109707
密码
/*zhong*/
应用名称
应用01
APP ID
8a216da85da6adf7015ddfa456641411
APP TOKEN
ef1a382ff33283a2452196fa41544a16

ACCOUNT SID：
8a216da85da6adf7015ddfa4535f140a
AUTH TOKEN：
1fda47acb47549b0b63b96c9de20ba16（APP TOKEN 请到应用管理中获取）
Rest URL(生产)：
https://app.cloopen.com:8883
AppID(默认)：
8a216da85da6adf7015ddfa456641411未上线
鉴权IP：
尚未开启（开启后可有效提升账户安全）
'''

import md5
import base64
import datetime
import urllib2
import json
from xmltojson import xmltojson
from xml.dom import minidom 

accountSid= '8a216da85da6adf7015ddfa4535f140a'; 
#说明：主账号，登陆云通讯网站后，可在控制台首页中看到开发者主账号ACCOUNT SID。

accountToken= '1fda47acb47549b0b63b96c9de20ba16'; 
#说明：主账号Token，登陆云通讯网站后，可在控制台首页中看到开发者主账号AUTH TOKEN。

appId='8a216da85da6adf7015ddfa456641411'; 
#请使用管理控制台中已创建应用的APPID。

serverIP='app.cloopen.com';
#说明：请求地址，生产环境配置成app.cloopen.com。

serverPort='8883'; 
#说明：请求端口 ，生产环境为8883.

softVersion='2013-12-26'; #说明：REST API版本号保持不变。 


class REST:
    AccountSid=''
    AccountToken=''
    AppId=''
    SubAccountSid=''
    SubAccountToken=''
    ServerIP=''
    ServerPort=''
    SoftVersion=''
    Iflog=True #是否打印日志
    Batch=''  #时间戳
    BodyType = 'xml'#包体格式，可填值：json 、xml
    
     # 初始化
     # @param serverIP       必选参数    服务器地址
     # @param serverPort     必选参数    服务器端口
     # @param softVersion    必选参数    REST版本号
    def __init__(self,ServerIP,ServerPort,SoftVersion):
        self.ServerIP = ServerIP;
        self.ServerPort = ServerPort;
        self.SoftVersion = SoftVersion;
    
    
    # 设置主帐号
    # @param AccountSid  必选参数    主帐号
    # @param AccountToken  必选参数    主帐号Token
    def setAccount(self,AccountSid,AccountToken):
      self.AccountSid = AccountSid;
      self.AccountToken = AccountToken;   
    
    # 设置应用ID
    # 
    # @param AppId  必选参数    应用ID
    def setAppId(self,AppId):
       self.AppId = AppId; 
    
    def log(self,url,body,data):
        print(u'这是请求的URL：')
        print (url);
        print(u'这是请求包体:')
        print (body);
        print(u'这是响应包体:')
        print (data);
        print('********************************')
    
    
    #主帐号鉴权
    def accAuth(self):
        if(self.ServerIP==""):
            print('172004');
            print(u'IP为空');
        
        if(self.ServerPort<=0):
            print('172005');
            print(u'端口错误（小于等于0）');
        
        if(self.SoftVersion==""):
            print('172013');
            print(u'版本号为空');
        
        if(self.AccountSid==""):
            print('172006');
            print(u'主帐号为空');
        
        if(self.AccountToken==""):
            print('172007');
            print(u'主帐号令牌为空');
        
        if(self.AppId==""):
            print('172012');
            print(u'应用ID为空');


    #设置包头
    def setHttpHeader(self,req):
        if self.BodyType == 'json':
            req.add_header("Accept", "application/json")
            req.add_header("Content-Type", "application/json;charset=utf-8")
            
        else:
            req.add_header("Accept", "application/xml")
            req.add_header("Content-Type", "application/xml;charset=utf-8")
    
    
    # 发送模板短信
    # @param to  必选参数     短信接收彿手机号码集合,用英文逗号分开
    # @param datas 可选参数    内容数据
    # @param tempId 必选参数    模板Id
    def sendTemplateSMS(self, to,datas,tempId):
        self.accAuth()
        nowdate = datetime.datetime.now()
        self.Batch = nowdate.strftime("%Y%m%d%H%M%S")
        #生成sig
        signature = self.AccountSid + self.AccountToken + self.Batch;
        sig = md5.new(signature).hexdigest().upper()
        #拼接URL
        url = "https://"+self.ServerIP + ":" + self.ServerPort + "/" + self.SoftVersion + "/Accounts/" + self.AccountSid + "/SMS/TemplateSMS?sig=" + sig
        #生成auth
        src = self.AccountSid + ":" + self.Batch;
        auth = base64.encodestring(src).strip()
        
        req = urllib2.Request(url)
        self.setHttpHeader(req)
        req.add_header("Authorization", auth)
        #创建包体
        b=''
        for a in datas:
            b+='<data>%s</data>'%(a)
        
        body ='<?xml version="1.0" encoding="utf-8"?><SubAccount><datas>'+b+'</datas><to>%s</to><templateId>%s</templateId><appId>%s</appId>\
            </SubAccount>\
            '%(to, tempId,self.AppId)
        if self.BodyType == 'json':   
            # if this model is Json ..then do next code
            b='['
            for a in datas:
                b+='"%s",'%(a) 
            b+=']'
            body = '''{"to": "%s", "datas": %s, "templateId": "%s", "appId": "%s"}'''%(to,b,tempId,self.AppId)
        req.add_data(body)
        data=''
        try:
            res = urllib2.urlopen(req);
            data = res.read()
            res.close()
            
            if self.BodyType=='json':
                #json格式
                locations = json.loads(data)
            else:
                #xml格式
                xtj=xmltojson()
                locations=xtj.main(data)
            if self.Iflog:
                self.log(url,body,data)
            return locations
        except Exception, error:
            print error
            if self.Iflog:
                self.log(url,body,data)
            return {u'172001':u'网络错误'}
            
            

def sendTemplateSMS(to,datas,tempId): 
    #初始化REST SDK
    rest = REST(serverIP,serverPort,softVersion) 
    rest.setAccount(accountSid,accountToken) 
    rest.setAppId(appId)

    result = rest.sendTemplateSMS(to,datas,tempId) 
    for k,v in result.iteritems():
        if k=='templateSMS' : 
                for k,s in v.iteritems():
                    print '%s:%s' % (k, s) 
        else: 
            print '%s:%s' % (k, v)
            
if __name__=="__main__":
    sendTemplateSMS("18835109707",['aaa',u'中文'],1)
 

