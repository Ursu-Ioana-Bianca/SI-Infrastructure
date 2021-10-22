import os
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES

# def _unpad(s):
#     return s[:-ord(s[len(s)-1:])]    

class Client2:
    BLOCKSIZE=16
    encrypt_key = " "
    file = " "
    mod = " "
    is_ready=False
    kc2_decr = " "

    def __init__(self,name, iv, key2):
        self.name=name
        self.iv=iv
        self.key2=key2


    def decrypt_key(self):
      cipher2 = AES.new(self.key2, AES.MODE_CBC, self.iv) 
      key1 = unpad(cipher2.decrypt(self.encrypt_key), self.BLOCKSIZE)
      return key1

    def decrypt_file(self, cipher_file):
        cipher = AES.new(self.kc2_decr, AES.MODE_CBC, self.iv) 
        plaintext = cipher.decrypt(cipher_file[AES.block_size:])
        return plaintext.rstrip(b"\0")

    # def decrypt_file1(self, cipher_file):
    #   decrypted_blocks = []

    #   nb_blocks = (int)(len(cipher_file) / 16) 
    #   cipher = AES.new(self.kc1_decr, AES.MODE_ECB)
    #   for i in range(nb_blocks):
    #         plain = cipher.decrypt(enc2, c2.encrypt_key) # set the the IV based on the encryption of the xored text
    #         decrypted_blocks.append(str(plain))
    #   return decrypted_blocks    

    

