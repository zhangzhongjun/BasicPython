# coding=utf-8
import codecs
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
        
    # data是dict格式维护的数据
    def collect_data(self,data):
        if data is None:
            return 
        self.datas.append(data)
        
    def collect_datas(self,datas):
        if datas is None or len(datas)==0:
            return 
        for data in datas:
            self.collect_data(data)
            
    def output_html(self):
        fout = codecs.open('f:\\output.html','w','utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write(r'<table border="1" bordercolor="red">')
        
        fout.write("<tr>")
        fout.write("<td>"+u"记录数"+"</td>")
        for key in self.datas[0]:
            print key
            fout.write("<td>"+key+"</td>")
        fout.write("</tr>")
        
        i = 1
        for d in self.datas:
            fout.write("<tr>")
            fout.write("<td>"+str(i)+"</td>")
            i = i+1
            for key in d:
                fout.write("<td>"+d[key] +"</td>")
            fout.write("</tr>")
        
        fout.write('</table>')
        fout.write("</body>")
        fout.write("</html>")
        
        fout = codecs.open('f:\\output.txt','w','utf-8')

        i = 1
        for d in self.datas:
            ress = str(i)+","+d[u"网站"] +","+d[u"姓名"]
            fout.write(ress)
            fout.write("\r\n")
            i = i+1
'''
ho = HtmlOutputer()
d = {u'姓名':u"张中俊",u'学位':u"硕士",u'工资':"200W"}
ho.collect_data(d)

d = {u'姓名':u"张三",u'学位':u"学士",u'工资':"100w"}
ho.collect_data(d)

d = {u'姓名':u"王五",u'学位':u"学士",u'工资':"20k"}
ho.collect_data(d)

ho.output_html()
'''