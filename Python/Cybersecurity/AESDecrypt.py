from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes
from binascii import hexlify, unhexlify

# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
# https://pycryptodome.readthedocs.io/en/latest/src/protocol/kdf.html#Crypto.Protocol.KDF.scrypt
# pip install pycryptodome

def AESDecrypt(data, key, iv):
   AEScipher = AES.new(key, AES.MODE_GCM, iv) # Create our AES Cipher Object; many modes are available and GCM is a good one for many things (e.g., used in TLS)
   # byteData = bytes.fromhex(data)  # encodes our message back from hex format to bytes
   plaintext = AEScipher.decrypt(data) # Performs the decryption; note: does not do verification with a MAC
   return plaintext.decode('latin-1') # returns the decoded message in latin format so we can read it


# def deriveKey(password, salt):
#    salt = bytes.fromhex(salt) # encode our hex salt into bytes
#    password = password.encode() # encode our string into bytes
#    return scrypt(password, salt, 16, N=2**14, r=8, p=1)


# ciphertext = '3a026284f1bdeb' # <----- Add your partner's encrypted message here
# senderNonce = '8a789a3ce90a4093be4f4b56e422a4ba' # <----- Add the nonce received from your partner here
# salt = '2f5d80ec9deb4582b9405a99a9276248' # <----- Add the salt received from your partner here
# senderPassword = 'thisistheway1234' # <----- Add your partner's key here
# 
# 
# key = deriveKey(senderPassword, salt) # derive the key based on our shared password and public salt

plaintext = AESDecrypt(unhexlify('c17baad5ff4c2ce25f10d5a1040df92d'), 'usetheforce!!!!!'.encode(), 'encryptionIntVec'.encode())
print('\n~~~DECRYPTED MESSAGE~~~')
print(plaintext + '\n')

