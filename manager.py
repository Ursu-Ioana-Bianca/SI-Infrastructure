import os
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES
from os import urandom
from base64 import b64encode
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# -*- coding: utf-8 -*-




class Manager:
    BLOCKSIZE=16
    key2 = " "

    def __init__(self,name, iv, key2):
        self.name=name
        self.iv = iv
        self.key2=key2
  
    def generateKey(self):
       random_bytes = urandom(16)
       key = b64encode(random_bytes).decode('utf-8')
       return key


  

    def encryptKey(self):
        self.key1 = self.generateKey()
        cipher1 = AES.new(self.key2, AES.MODE_CBC, self.iv)
        encr_key = cipher1.encrypt(pad(self.key1.encode('utf-8'),self.BLOCKSIZE))
        return encr_key
