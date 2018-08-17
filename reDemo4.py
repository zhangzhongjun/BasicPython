# coding=utf-8
s = "[[382287,90,-1,'2010-04-10 23:59',20,24,'0-3','0-0','英超7','英超1',-0.75,-0.25,'2.5/3','1',1,1,1,1,0,0,'先开球(车路士)<br>角球数(6) | 角球数(7)','kick-off (Chelsea),Aston Villa corner(6),Chelsea corner(7)',''],[382288,90,-1,'2010-04-11 23:00',33,36,'0-0','0-0','英超5','英超20',1.5,0.75,'3','1/1.5',1,1,1,1,0,0,'先开球(热刺)<br>角球数(17) | 角球数(5)<br>90分钟[0-0],120分钟[0-2],朴茨茅夫胜出','kick-off (Tottenham Hotspur),Tottenham Hotspur corner(17),Portsmouth corner(5)<br>90Min[0-0],,120Min[0-2],Portsmouth Win','']]"
import re

house_price = u'40753元/㎡'
print re.sub('\D','',house_price)
s = 'http://tj.sofang.com/saleesb/area/aa20'
print s+'-bl'

message = 'HOW ARE&&YOU'
print re.sub('[^A-Z]','',message)