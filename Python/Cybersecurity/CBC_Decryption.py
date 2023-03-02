from Crypto.Cipher import AES
import binascii
from binascii import hexlify, unhexlify

# Define the key, initialization vector, and ciphertext
key = 'usetheforce!!!!!'
iv = 'encryptionIntVec'
ciphertext = 'c17baad5ff4c2ce25f10d5a1040df92d'


key_bytes = key.encode()
iv_bytes = iv.encode()
ciphertext_bytes = binascii.unhexlify(ciphertext)
# ciphertext_bytes = bytes.fromhex(ciphertext)
# ciphertext = ciphertext.decode()()



# Create an AES cipher object with CBC mode and the given key and IV
cipher = AES.new(key_bytes, AES.MODE_CBC, iv_bytes)

# Decrypt the ciphertext and remove the padding
plaintext = cipher.decrypt(ciphertext)
plaintext = plaintext[:-plaintext[-1]]

# Print the decrypted plaintext as a string
print(plaintext.decode())


