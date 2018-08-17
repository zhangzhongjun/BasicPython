import json
import base64


data = {20: [['张三', '20', '男'], ['赵六', '20', '女']], 21: [['李四', '21', '女']], 22: [['王五', '22', '女']]}
data_temp ={}
for key in data:
    items = data[key]
    items_temp = []
    for item in items:
        item_temp = []
        for attr in item:
            item_temp.append(base64.b64encode(attr.encode()))
    items_temp.append(item_temp)
    
    data_temp[key] = items_temp
    
print(data_temp)

for key in data_temp:
    items = data_temp[key]
    for item in items:
        for attr in item:
            print(base64.b64decode(attr).decode('utf-8'))
