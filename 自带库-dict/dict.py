# coding=utf-8
#!usr/bin/python

#dict中存放的是引用 而不是数值
spam = {'hello':42}
eggs = spam
eggs['hello']=99
print spam
print eggs
#字符串和dict之间的相互转化
import json
data1 = {'b': 789, 'c': 456, 'a': 123}
encode_json = json.dumps(data1)
print type(encode_json), encode_json
decode_json = json.loads(encode_json)
print type(decode_json)
print decode_json['a']
print decode_json

#dict里面的数据是可以改变的
d={1:[1,2,3],2:[11,22,33]}
d[1].append(4)
print d
'''
	dict是无顺序的
'''
d={
    'Adam':95,
    'Lisa':85,
    'Bart':59
}
print len(d)
print d
# 判断某key是否包含在dict中
if 'Adam' in d:
    print d['Adam']
# 对key进行遍历
for key in d:
    print key,':',d.get(key)
# 对value进行遍历 values()获得dict中的所有值
for value in d.values():
    print value
print "-----------------------------------------------------------"
# itervalues()依次从dict中取出values，而values()则会将dict转化为包含value的list
for value in d.itervalues():
    print value
print "-----------------------------------------------------------"
# 使用get方法，如果存在key，则返回需要的值；否则返回none
print d.get('Adam')
print d.get('ge')
print "-----------------------------------------------------------"
# 遍历key和value
for key,value in d.items():
    print key,":",value
print "-----------------------------------------------------------"
# 使用iterItems()方法，不转化，只是单纯的取出来
for key,value in d.iteritems():
    print key,":",value
print "-----------------------------------------------------------"
print "Adam:",d.get('Adam')
print "Lisa:",d.get('Lisa')
print 'Bart:',d.get('Bart')
print "-----------------------------------------------------------"
d={
    95:'Adam',
    85:'Lisa',
    59:'Bart'
}
print "95:",d.get(95)
d[72]="Paul"
print d
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum = 0.0
for score in d.values():
    sum = sum + score
print sum/(len(d.values()))

d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
#打印出 name : score，最后再打印出平均分 average : score。
sum = 0.0
for name,score in d.items():
    print name,",",score
    sum += score
print "average",":",sum/len(d)
print "-----------------------------------------------------------"
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
tds = ['<tr><td>%s</td><td>%s</td></tr>' % (name, score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
print "-----------------------------------------------------------"
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score>=60:
        return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
    else: 
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
tds = [generate_tr(name,score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
print '\n'.join(tds)
print '</table>'
# dict生成式
from random import randint
d= {x: randint(60,100) for x in xrange(1,21,1)}
print d
print {k:v for k,v in d.iteritems() if v>90}
# 将10个老师随机地分配到3个办公室中
offices = {0:[],1:[],2:[]}
print offices
teachers = ["Wang","Li","Zhang","Lv","Hao","Cang","Zhang","Wang","Lv","Liu"]
from random import randint
for name in teachers:
    index  = randint(0,2)
    L = offices.get(index)
    L.append(name)
print offices
# 将10个老师随机地分配到3个办公室中，每个办公室的老师不少于3个
from random import randint
bol = False
while not bol:
    offices = {0:[],1:[],2:[]}
    print offices
    teachers = ["Wang","Li","Zhang","Lv","Hao","Cang","Zhang","Wang","Lv","Liu"]
    for name in teachers:
        index  = randint(0,2)
        L = offices.get(index)
        L.append(name)
    bol = True
    for v in offices.itervalues():
        if len(v)<3:
            bol = False
print offices