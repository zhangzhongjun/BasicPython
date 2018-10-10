from Crypto.Cipher import AES
from binascii import a2b_hex,b2a_hex
import json


from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import codecs

# 补全字符
def align(str, isKey=False):
    # 如果接受的字符串是密码，需要确保其长度为16
    if isKey:
        if len(str) > 16:
            return str[0:16]
        else:
            return align(str)
    # 如果接受的字符串是明文或长度不足的密码，则确保其长度为16的整数倍
    else:
        zerocount = 16-len(str) % 16
        for i in range(0, zerocount):
            str = str + '\0'
        return str


# CBC模式加密
def encrypt_CBC(str, key):
    # 补全字符串
    str = align(str)
    key = align(key, True)
    # 初始化AES，引入初始向量
    AESCipher = AES.new(key, AES.MODE_CBC, '1234567890123456')
    # 加密
    cipher = AESCipher.encrypt(str)
    return b2a_hex(cipher)




# CBC模式解密
def decrypt_CBC(str, key):
    # 补全字符串
    key = align(key, True)
    # 初始化AES
    AESCipher = AES.new(key, AES.MODE_CBC, '1234567890123456')
    # 解密
    paint = AESCipher.decrypt(a2b_hex(str))
    return paint
  
if __name__ == "__main__":
    #生成密钥
    miyao = get_random_bytes(16)
    temp = encrypt_CBC("test".encode(),miyao)
    print(temp,type(temp))