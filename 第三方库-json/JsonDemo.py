# coding=utf-8
import json
import codecs
import sys
class JsonInputer:
    def readFile(self,filePath):
        fin = codecs.open(filePath,'r','utf-8')
        try:
            d = json.load(fin)
        except:
            info=sys.exc_info()  
            print info[0],":",info[1]
            return None 
        else:
            return d
        finally:
            fin.close()
    
    def readStr(self,str):
        try:    
            res = json.loads(str)
        except:
            info=sys.exc_info()  
            print info[0],":",info[1]
            return None
        else:
            return res
    
    def writeJson2Str(self,j):
        return json.dumps(j)
        
    def writeJson2File(self,j,filePath):
        str = self.writeJson2Str(j)
        fin = codecs.open(filePath,'w','utf-8')
        res = fin.write(str)
        fin.close()
        
str='''
{
	"status": 1,
	"error": "",
	"data": {
		"timestamp": 1498870559,
		"info": [{
			"title": "热门",
			"singer": [{
				"heatoffset": 1,
				"sortoffset": -9,
				"singername": "Alan Walker",
				"intro": "",
				"songcount": 0,
				"imgurl": "http:\/\/singerimg.kugou.com\/uploadpic\/softhead\/{size}\/20170316\/20170316182005449.jpg",
				"albumcount": 0,
				"mvcount": 0,
				"singerid": 178240,
				"heat": 2857285,
				"fanscount": 638423,
				"is_settled": 0
			},
			{
				"heatoffset": 2,
				"sortoffset": -6,
				"singername": "Justin Bieber",
				"intro": "",
				"songcount": 0,
				"imgurl": "http:\/\/singerimg.kugou.com\/uploadpic\/softhead\/{size}\/20161109\/20161109155400970766.jpg",
				"albumcount": 0,
				"mvcount": 0,
				"singerid": 27108,
				"heat": 1829159,
				"fanscount": 646173,
				"is_settled": 0
			}]
		}]
	},
	"errcode": 0}
'''            
if __name__=="__main__":
    ji = JsonInputer()
    #从python数据类型到json dumps
    d={"status":1,"error":"","data":{"timestamp":1498870559,"info":[{"title":"a"},{"中文":"a"}]}}
    print type(d)
    print json.dumps(d)
    print ji.writeJson2Str(d)
    ji.writeJson2File(d,"F:\\t1.json")
    print ji.writeJson2Str([1,2,3])
    ji.writeJson2File([1,2,3],"F:\\t.json")
    #从json到python数据类型 loads
    o = ji.readStr("[1,2,3]")
    print type(o)
    o = ji.readStr('{"type":"1","data":"good"}')
    print type(o)
    o=ji.readStr('{"status":1,"error":"","data":{"timestamp":1498870559,"info":[{"title":"a"},{"title":"a"}]}}')
    print type(o)
    print o
    o=ji.readStr(str)
    print type(o)
    print o
    
    o = ji.readFile("F:\\t1.json")
    print type(o)
