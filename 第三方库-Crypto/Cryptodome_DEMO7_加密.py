import json


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import codecs

if __name__ == "__main__":
    #生成密钥
    miyao = get_random_bytes(16)
    f = open('f://key.data','wb')
    f.write(miyao)
    f.close()
    
    f = codecs.open('f://年龄数据.csv',"r","utf-8")
    lines = f.readlines()
    f.close()
    
    print(miyao)
    
    f = open("f://encrypt.data",'wb')
    #data_temp = {}
    for line in lines:
        cipher = AES.new(miyao, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(line.encode())
        
        print(cipher.nonce,ciphertext,tag)
        print(len(cipher.nonce),len(ciphertext))
        f.write(cipher.nonce)
        f.write(ciphertext+b"\r\n")
        cipher = AES.new(miyao, AES.MODE_EAX, cipher.nonce)
        plainText = cipher.decrypt(ciphertext)
        print(plainText.decode("utf-8"))
    f.close()

