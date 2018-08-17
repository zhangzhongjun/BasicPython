# coding=utf-8
import re
s='''
 [[603,383,1,4,[1136068,103,-1,"2015-07-14 23:30",603,383,"1-3","0-0","拉脱超2","芬超1",-0.5,-0.25,"2/2.5","0.5/1",1,1,1,1,0,0,"","","","0","LAT D1-2","FIN D1-1"],[1136055,103,-1,"2015-07-21 23:59",383,603,"1-0","0-0","芬超1","拉脱超2",1.25,0.5,"2.5","1",1,1,1,1,0,0,"","","","0","FIN D1-1","LAT D1-2"]],[703,940,1,1,[1136061,103,-1,"2015-07-15 01:00",703,940,"0-0","0-0","塞浦甲1","马其甲1",1.75,0.75,"3","1/1.5",1,1,1,1,0,0,"","","","0","CYP D1-1","MKD D1-1"],[1136074,103,-1,"2015-07-22 02:00",940,703,"1-1","0-0","马其甲1","塞浦甲1",-0.25,0,"2/2.5","0.5/1",1,1,1,1,0,0,"","","","0","MKD D1-1","CYP D1-1"]],[238,23131,3,0,[1144859,103,-1,"2015-07-15 01:30",238,23131,"1-0","1-0","丹麦超7","",3,,"4/4.5","",1,1,1,1,0,0,"","","","0","DEN SASL-7",""],[1144860,103,-1,"2015-07-22 02:00",23131,238,"0-2","0-1","","丹麦超2",-1.75,-0.75,"3","1/1.5",1,1,1,1,0,0,"","","","0","","DEN SASL-2"]],[505,2555,5,1,[1144861,103,-1,"2015-07-15 02:00",505,2555,"5-0","2-0","挪超5","阿美超1",1.25,0.5,"2.5/3","1/1.5",1,1,1,1,0,0,"","","","0","NOR D1-5","ARM D1-1"],[1144862,103,-1,"2015-07-21 22:00",2555,505,"1-0","0-0","阿美超1","挪超6",-0.75,-0.25,"2.5/3","1/1.5",1,1,1,1,0,0,"","","","1","ARM D1-1","NOR D1-6"]],[3573,1650,6,4,[1144863,103,-1,"2015-07-15 02:00",3573,1650,"4-1","2-0","阿尔巴1","北爱超1",0.75,0.25,"2.5","1",1,1,1,1,0,0,"","","","0","ALB D1-1","NIR D1-1"],[1144864,103,-1,"2015-07-22 02:45",1650,3573,"3-2","0-0","北爱超1","阿尔巴1",-0.25,0,"2.5","1",1,1,1,1,0,1,"","","","0","NIR D1-1","ALB D1-1"]],[1261,1225,1,1,[1144865,103,-1,"2015-07-15 02:00",1261,1225,"0-1","0-0","威超1","匈甲1",-0.5,-0.25,"2.5","1",1,1,1,1,0,0,"","","","0","WAL PR-1","HUN D1-1"],[1144866,103,-1,"2015-07-23 02:30",1225,1261,"0-1","0-0","匈甲11","威超1",1.25,0.5,"2.5","1",1,1,1,1,0,1,"","",";|;|;|90,0-1;1-1;1,1-1;;1","0","HUN D1-11","WAL PR-1"]],[722,953,3,0,[1136058,103,-1,"2015-07-15 02:45",722,953,"1-0","0-0","塞尔超1","格鲁甲1",1.25,0.5,"2.5","1",1,1,1,1,0,1,"","","","0","SER D1-1","GEO D1-1"],[1136071,103,-1,"2015-07-21 20:30",953,722,"0-2","0-1","格鲁甲1","塞尔超2",-0.75,-0.25,"2/2.5","0.5/1",1,1,1,1,0,0,"","","","0","GEO D1-1","SER D1-2"]],[666,1142,0,3,[1136052,103,-1,"2015-07-15 03:00",666,1142,"0-2","0-1","波斯甲1","波兰超8",-0.25,-0.25,"2/2.5","0.5/1",1,1,1,1,0,0,"","","","0","BOS PL-1","POL D1-8"],[1136065,103,-1,"2015-07-23 02:45",1142,666,"1-0","1-0","波兰超12","波斯甲1",1,0.5,"2.5","1",1,1,1,1,0,0,"","","","0","POL D1-12","BOS PL-1"]],[408,2389,1,0,[1136056,103,-1,"2015-07-16 01:00",408,2389,"0-0","0-0","瑞典超6","立陶甲1",1.75,0.75,"3","1/1.5",1,1,1,1,0,0,"","","","0","SWE D1-6","LIT D1-1"],[1136069,103,-1,"2015-07-22 02:10",2389,408,"0-1","0-0","立陶甲1","瑞典超5",-0.5,-0.25,"2/2.5","0.5/1",1,1,1,1,1,0,"","","","0","LIT D1-1","SWE D1-5"]],[70,4383,6,1,[1136063,103,-1,"2015-07-16 02:45",70,4383,"2-0","1-0","苏超1","冰岛超6",2.25,1,"3.5","1.5",1,1,1,1,0,0,"","","","0","SCO PR-1","ICE PR-6"],[1136076,103,-1,"2015-07-23 03:15",4383,70,"1-4","1-1","冰岛超7","苏超1",-1,-0.5,"2/2.5","1",1,1,1,1,0,0,"","","","0","ICE PR-7","SCO PR-1"]],[15474,15175,3,1,[1136072,103,-1,"2015-07-21 23:00",15474,15175,"2-1","1-1","摩尔甲2","保超9",-0.75,-0.25,"2/2.5","1",1,1,1,1,1,0,"","","","0","MOL D1-2","BUL D1-9"],[1136059,103,-1,"2015-07-15 01:45",15175,15474,"0-1","0-1","保超1","摩尔甲2",2,0.75,"3/3.5","1/1.5",1,1,1,1,0,0,"","","","0","BUL D1-1","MOL D1-2"]],[714,957,6,3,[1136064,103,-1,"2015-07-22 01:30",714,957,"5-1","1-0","以超2","马尔甲1",2.5,1,"3.5/4","1/1.5",1,1,1,1,0,0,"","","","0","ISR D1-2","MAL D1 PO-1"],[1136051,103,-1,"2015-07-15 02:00",957,714,"2-1","0-1","马尔甲1","以超2",-1.5,-0.5,"3","1/1.5",1,1,1,1,0,0,"","","","0","MAL D1 PO-1","ISR D1-2"]],[683,725,3,2,[1136066,103,-1,"2015-07-22 22:00",683,725,"3-1","2-1","哈萨超3","斯亚甲6",0.25,0.25,"2/2.5","0.5/1",1,1,1,1,1,0,"","","","0","KAZ PR-3","SLO D1-6"],[1136053,103,-1,"2015-07-15 02:30",725,683,"1-0","1-0","斯亚甲1","哈萨超3",0.5,0.25,"2/2.5","0.5/1",1,1,1,1,0,0,"","","","0","SLO D1-1","KAZ PR-3"]],[8441,653,1,4,[1136060,103,-1,"2015-07-23 02:00",8441,653,"0-3","0-2","卢森甲1","克亚甲6",-1.5,-0.5,"2.5/3","1/1.5",1,1,1,1,0,0,"","","","1","LUX D1-1","CRO D1-6"],[1136073,103,-1,"2015-07-16 03:00",653,8441,"1-1","1-1","克亚甲4","卢森甲1",2.5,1,"3.5","1.5",1,1,1,1,0,1,"","","","0","CRO D1-4","LUX D1-1"]],[626,1232,4,3,[1136070,103,-1,"2015-07-23 02:30",626,1232,"2-3","0-2","罗甲2","斯伐超1",0.75,0.25,"2/2.5","1",1,1,1,1,0,1,"","","","0","ROM D1-2","SVK D1-1"],[1136057,103,-1,"2015-07-15 02:30",1232,626,"0-2","0-0","斯伐超1","罗甲1",0,0,"2/2.5","1",1,1,1,1,0,0,"","","","1","SVK D1-1","ROM D1-1"]],[1345,2435,1,2,[1136067,103,-1,"2015-07-23 02:45",1345,2435,"0-0","0-0","爱超1","白俄超1",-0.25,0,"2/2.5","1",1,1,1,1,0,0,"","","","0","IRE PR-1","BLR D1-1"],[1136054,103,-1,"2015-07-16 01:30",2435,1345,"2-1","2-1","白俄超1","爱超1",1.25,0.5,"2.5","1",1,1,1,1,0,0,"","","","0","BLR D1-1","IRE PR-1"]],[5912,4395,0,1,[1136075,103,-1,"2015-07-23 02:45",5912,4395,"0-1","0-0","黑山甲1","阿塞超1",-0.25,-0.25,"2/2.5","0.5/1",1,1,1,1,0,0,"","","","1","MNE D1-1","AZE D1-1"],[1136062,103,-1,"2015-07-16 00:30",4395,5912,"0-0","0-0","阿塞超1","黑山甲1",1.5,0.5,"2.5","1",1,1,1,1,0,0,"","","","0","AZE D1-1","MNE D1-1"]]]
'''
s = s.replace(';','')
s = s.replace('|','')
print s
import json
json.loads(s)