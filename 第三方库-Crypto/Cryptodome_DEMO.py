from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

import json
def AES_File(data):
    key = get_random_bytes(16)
    print (key)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)


    file_out = open("f:\\key.bin", "wb")
    file_out.write(key)
    file_out.close()


    file_out = open("f:\\encrypted.bin", "wb")
    [ file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()
    
if __name__ == "__main__":
    f = open("f:\\test.csv",'rb')
    AES_File(f.read())
    f.close()
