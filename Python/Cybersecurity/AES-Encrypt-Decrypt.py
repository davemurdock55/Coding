from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad, unpad

# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#cbc-mode
# https://pycryptodome.readthedocs.io/en/latest/src/util/util.html#module-Crypto.Util.Padding
# pip install pycryptodome

def AESEncryptFile(fileBytes, key):
   AEScipher = AES.new(key, AES.MODE_CBC) # Create our AES Cipher Object; Using CBC for consistency with C#, but better are available
   paddedData = pad(fileBytes, 16, 'pkcs7') # We have to do the padding manually. Here using 16 byte blocks (used by CBC) and standard PKCS7 padding
   iv = AEScipher.iv # with CBC, we need an initialization vector. The AES cipher can randomly create one for us.
   ciphertext = AEScipher.encrypt(paddedData) # Performs the encryption
   return ciphertext, iv # in bytes

def AESDecryptFile(fileBytes, key, iv):
   AEScipher = AES.new(key, AES.MODE_CBC, iv) # Create our AES Cipher Object. We need to include our IV. Using CBC for consistency with C#, but better are available
   decryptedData = unpad(AEScipher.decrypt(fileBytes), 16, 'pkcs7') # Performs the encryption and also unpads the data using PKCS7
   return decryptedData # in bytes

# This isn't a great way to convert the key into something that AES can handle, but I'm adding here to be consistent with the C# limitations
# This method of computing SHA-256 is using the pycryptodome library. Typically, the standard 'hashlib' library is used
def deriveKeyHash(password):
   h = SHA256.new()
   h.update(password.encode())
   return h.digest()

def encryptMe():
   password = 'password123' # <------ ENTER YOUR PASSWORD HERE

   with open('/path/to/PO.pdf', 'rb') as poFile: # Open the file to be encrypted. We're opening as a binary file because PDFs are binary files.
      pdfBytes = poFile.read()

   ciphertext, iv = AESEncryptFile(pdfBytes, deriveKeyHash(password)) # encrypts the file using the password. The password is hashed using SHA256 (not a good option instead of a standard KDF but used here for consistency)

   with open('/path/to/PO-Encrypted-Python.pdf', 'wb') as outFile:
      outFile.write(iv) # We write the IV first (first 16 bytes)
      outFile.write(ciphertext) # Then write out everything else

def decryptMe():
   password = 'password123' # <------ ENTER YOUR PASSWORD HERE

   with open('/path/to/PO-Encrypted-Python.pdf', 'rb') as poFile:
      fileBytes = poFile.read() # Reads the file as binary bytes
      iv = fileBytes[0:16] # Gets the IV (initialization vector) out of the first 16 bytes
      pdfBytes = fileBytes[16:] # gets the rest of the file (the PDF content)

   decryptedBytes = AESDecryptFile(pdfBytes, deriveKeyHash(password), iv) # decrypts the encrypted file using the password and IV. The password is hashed using SHA256 (not a great option, but used for consistency here).

   with open('/path/to/PO-Decrypted-Python.pdf', 'wb') as outFile:
      outFile.write(decryptedBytes)



#encryptMe()
decryptMe()