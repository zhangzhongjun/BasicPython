import json


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


if __name__ == "__main__":
    #生成密钥
    miyao = get_random_bytes(16)

    f = codecs.open('f://originData.data',"r",'utf-8')
    data = json.loads(f.read())
    f.close()
    
    print(miyao)
    print(data)
    
    f = open("f://encrypt.data",'wb')
    data_temp = {}
    for key in data:
        items = data[key]
        items_temp = []
        for item in items:
            item_temp = []
            
            for attr in item:
                cipher = AES.new(miyao, AES.MODE_EAX)
                ciphertext, tag = cipher.encrypt_and_digest(attr.encode())
                #print (cipher.nonce, tag, ciphertext)
                #print (cipher.nonce+" ".encode()+ciphertext+" ".encode()+tag)
                item_temp.append((cipher.nonce+" ".encode()+ciphertext+" ".encode()+tag))
            items_temp.append(item_temp)
            print (b"###".join(item_temp))
            f.write(str(key).encode()+b"###"+b"###".join(item_temp))
        data_temp[key] = items_temp
    #print (data_temp)

    
    f = open('f://encrypt.data','r')
    data_temp = json.loads(f.read())
    f.close()
    #开始解密
    for key in data_temp:
        items = data_temp[key]
        for item in items:
            for attr in item:
                nonce = attr.split(" ".encode())[0]
                miwen = attr.split(" ".encode())[1]
                tag = attr.split(" ".encode())[2]
                cipher = AES.new(miyao, AES.MODE_EAX, nonce)
                data = cipher.decrypt(miwen)
                print(data.decode('utf-8'))