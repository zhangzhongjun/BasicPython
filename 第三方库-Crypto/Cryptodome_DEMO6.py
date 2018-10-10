import json


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


if __name__ == "__main__":
    #生成密钥
    f = open('f://key.key','rb')
    miyao = f.read()
    f.close()
    
    
    print(miyao)
    
    f = open("f://query_result.csv",'rb')
    for line in f.readlines():
        line = line.strip(b'\r\n')
        nonce = line.split(b" ")[0]
        ciphertext = line.split(b" ")[1]
        cipher = AES.new(miyao, AES.MODE_EAX, nonce)
        plainText = cipher.decrypt(ciphertext)
        print(plainText.decode('utf-8'))
    f.close()

