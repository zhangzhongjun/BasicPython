#!/usr/bin/python

import os
import sys
#import commands
import json


'''get json'''
def get_new_json(filepath,key,value):
	key_ = key.split(".")
	key_length = len(key_)
	with open(filepath, 'rb') as f:
		json_data = json.load(f)
		i = 0
		a = json_data
		while i < key_length :
			if i+1 == key_length :
				a[key_[i]] = value
				i = i + 1
			else :
				a = a[key_[i]]
				i = i + 1
	f.close()
	return json_data

'''write json'''	
def rewrite_json_file(filepath,json_data):
	with open(filepath, 'w') as f:
	    json.dump(json_data,f)
	f.close()
 
'''main function'''
if __name__ == '__main__':
    key = sys.argv[1]
    value = sys.argv[2]
    json_path = 'config.json'

    #os.system('cp ./dependencies/tpl_dir/config.json.tpl ./config.json')
    	
    m_json_data = get_new_json(json_path,key,value)	
    rewrite_json_file(json_path,m_json_data)







# with open('config.json.test') as conf:
#     for line in conf():
#         if re.search('${CONFIG_JSON_SYSTEM_CONTRACT_ADDRESS_TPL}',line):
#             line = re.sub('${CONFIG_JSON_SYSTEM_CONTRACT_ADDRESS_TPL}','test_var_1',line)
#             w_str+=line
#         else:
#             w_str+=line
# print w_str
# conf.close


    # line = conf.readline()
# with open(filename, 'r+') as conf:
#     # for line in conf:
#     #     _json = json.loads(line)
#     pop_data = json.load(conf)
#     print(type(pop_data))
#     #data = "cryptomod" + ":" + "12"
#     _json = json.dumps(pop_data['cryptomod'])
#     print(type(pop_data['cryptomod']))
#     print(type(_json))
#     print(_json)
#     json.dump(['cryptomod':'123'],conf)
#     print(pop_data['cryptomod'])

   

# conf.close()


