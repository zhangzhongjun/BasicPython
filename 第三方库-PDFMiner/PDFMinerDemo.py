#!/usr/bin/python
# -*- encoding:utf-8 -*-


from urllib2 import urlopen
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

def convert_pdf_to_txt(fp):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    fp.close()
    device.close()
    textstr = retstr.getvalue()
    retstr.close()
    return textstr

url='http://pythonscraping.com/pages/warandpeace/chapter1.pdf'
fp = StringIO(urlopen(url).read())  # for url

path=u"F:\\100.pdf"
fp = file(path, 'rb')               # for path

text=convert_pdf_to_txt(fp)
text = unicode(text,'utf-8')
print text
import codecs
b = codecs.open('F:\\b.txt','w','utf-8')
b.write(text)
lines = text.split('\n')
print len(lines)
#print unicode(text,'utf-8')