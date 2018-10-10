import json


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


if __name__ == "__main__":
    #生成密钥
    miyao = get_random_bytes(16)
    f = open('f://key.data','wb')
    f.write(miyao)
    f.close()
    
    f = open('f://originData.data',"r")
    data = json.loads(f.read())
    f.close()
    
    print(miyao)
    print(data)
    
    f = open("f://encrypt.data",'wb')
    #data_temp = {}
    for key in data:
        items = data[key]
        #items_temp = []
        for item in items:
            #item_temp = []
            attr = " ".join(item)
            print(attr)
            cipher = AES.new(miyao, AES.MODE_EAX)
            ciphertext, tag = cipher.encrypt_and_digest(attr.encode())
            
            print(key,cipher.nonce,ciphertext,tag)
            f.write(cipher.nonce+b" "+ciphertext+b"\r\n")
            cipher = AES.new(miyao, AES.MODE_EAX, cipher.nonce)
            plainText = cipher.decrypt(ciphertext)
            print(plainText.decode("utf-8"))
    f.close()

