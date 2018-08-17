from Crypto.Cipher import AES

file_in = open("f:\\key.bin",'rb')
key = file_in.read()
file_in.close()

file_in = open("f:\\encrypted.bin", "rb")
nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]
file_in.close()


# let's assume that the key is somehow available again
cipher = AES.new(key, AES.MODE_EAX, nonce)
data = cipher.decrypt_and_verify(ciphertext, tag)

print(data.decode("utf8"))