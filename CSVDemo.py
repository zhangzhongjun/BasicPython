# coding=utf-8
import csv
import codecs
#支持的CSV格式
print  csv.list_dialects()

f = codecs.open('f:\\cc.csv','rb','utf-8')
csv_reader = csv.reader(f,dialect='excel')
for row in csv_reader:
    print row,type(row),len(row)

f = codecs.open('f:\\ca.csv','wb','utf-8')
csv_writer = csv.writer(f,dialect='excel')
list=[1,2,3,4]
list2=["hello","world"]
csv_writer.writerow(list)
csv_writer.writerow(list2)


import CSVClass
if __name__=="__main__":
    f = codecs.open('f:\\caw.csv','wb','utf-8')
    uw = CSVClass.UnicodeWriter(f)
    list=['1','2','3','4']
    list2=["hello","world"]
    uw.writerow(list)
    uw.writerow(list2)
    L=[list,list2]
    uw.writerows(L)
    