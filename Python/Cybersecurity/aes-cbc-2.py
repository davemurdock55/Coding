# from Crypto.Cipher import AES
# import Crypto.Cipher.AES
# from binascii import hexlify, unhexlify
#
# key = unhexlify('2b7e151628aed2a6abf7158809cf4f3c')
# IV = unhexlify('000102030405060708090a0b0c0d0e0f')
#
# plaintext1 = unhexlify('6bc1bee22e409f96e93d7e117393172a')
# plaintext2 = unhexlify('ae2d8a571e03ac9c9eb76fac45af8e51')
# plaintext3 = unhexlify('30c81c46a35ce411e5fbc1191a0a52ef')
#
# cipher = AES.new(key,AES.MODE_CBC,IV)
# ciphertext = cipher.encrypt(plaintext1 + plaintext2 + plaintext3)
# hexlify(ciphertext)
#
# decipher = AES.new(key,AES.MODE_CBC,IV)
# plaintext = decipher.decrypt(ciphertext)
# plaintext == plaintext1 + plaintext2 + plaintext3  # test if decryption was successful
#
# print(hexlify(plaintext))



from Crypto.Cipher import AES
import Crypto.Cipher.AES
from binascii import hexlify, unhexlify


def encryptDecryptCBC(message, key, IV) :
   key = unhexlify(key)
   IV = unhexlify(IV)

   plaintext1 = unhexlify(message)


   cipher = AES.new(key,AES.MODE_CBC,IV)
   ciphertext = cipher.encrypt(plaintext1)

   decipher = AES.new(key,AES.MODE_CBC,IV)
   plaintext = decipher.decrypt(ciphertext)
   plaintext == plaintext1 # test if decryption was successful

   return hexlify(plaintext)


print(encryptDecryptCBC('6bc1bee22e409f96e93d7e117393172a', '2b7e151628aed2a6abf7158809cf4f3c', '000102030405060708090a0b0c0d0e0f'))

def encryptCBC(message, key, IV) :
   key = unhexlify(key)
   IV = unhexlify(IV)

   plaintext1 = unhexlify(message)


   cipher = AES.new(key,AES.MODE_CBC,IV)
   ciphertext = cipher.encrypt(plaintext1)

   return hexlify(ciphertext)



def decryptCBC(message, key, IV) :
   # key = unhexlify(key)
   # IV = unhexlify(IV)

   # m = unhexlify(message)


   decipher = AES.new(key,AES.MODE_CBC,IV)
   plaintext = decipher.decrypt(message)

   return hexlify(plaintext)





key = 'usetheforce!!!!!'.encode()
iv = 'encryptionIntVec'.encode()
message = 'c17baad5ff4c2ce25f10d5a1040df92d'
ciphertext = unhexlify(message)
print('message: ', message)
print('key: ', key)
print('iv: ', iv)
print('ciphertext: ', ciphertext)

plaintext = decryptCBC(ciphertext, key, iv)

plaintext = plaintext.decode()

print("plaintext: ", plaintext)
