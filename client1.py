from __future__ import print_function
import os
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
import codecs
import sys


BITS = ('0', '1')
ASCII_BITS = 8

def pad_bits_append(seq, size):
     diff = max(0, size - len(seq))
     print(seq, diff)
     return seq + [0] * diff

def bits_to_char(b):
    assert len(b) == ASCII_BITS
    value = 0
    for e in b:
        print(e)
        value = (value * 2) + e
    return chr(value)     

def bits_to_string(b):
    return ''.join([bits_to_char(b[i:i + ASCII_BITS]) 
         for i in range(0, len(b), ASCII_BITS)])     


def string_to_bits(s):
    def chr_to_bit(c):
        return pad_bits(convert_to_bits(ord(c)), ASCII_BITS)
    return [b for group in 
            map(chr_to_bit, s)
                for b in group]

def aes_encoder(block, key):
    block = pad_bits_append(block, len(key))
    # the pycrypto library expects the key and block in 8 bit ascii encoded strings so we convert from the bit string
    block = bits_to_string(block)
    key = bits_to_string(key)
    ecb = AES.new(key, AES.MODE_ECB)
    return string_to_bits(ecb.encrypt(block))

# the electronic cookbook cipher
# illustrating manipulating the plaintext,
# key, and init_vec 
def electronic_cookbook(plaintext, key, block_size, block_enc):
    """Return the ecb encoding of `plaintext"""
    cipher = []
    # break the plaintext into blocks
    # and encode each one
    for i in range(len(plaintext) / block_size + 1):
        start = i * block_size
        if start >= len(plaintext):
            break
        end = min(len(plaintext), (i+1) * block_size)
        block = plaintext[start:end]
        cipher.extend(block_enc(block, key))
    return cipher


def cipher_block_chaining(plaintext, key, init_vec, block_size, block_enc):
    """Return the cbc encoding of `plaintext`
    
    Args:
        plaintext: bits to be encoded
        key: bits used as key for the block encoder
        init_vec: bits used as the initalization vector for 
                  the block encoder
        block_size: size of the block used by `block_enc`
        block_enc: function that encodes a block using `key`
    """
    # Assume `block_enc` takes care of the necessary padding if `plaintext` is not a full block
    
    # return a bit array, something of the form: [0, 1, 1, 1, 0]

    cipher = []
    # break the plaintext into blocks
    # and encode each one
    cipher.extend(init_vec)
    for i in range(len(plaintext) / block_size + 1):
        start = i * block_size
        if start >= len(plaintext):
            break
        end = min(len(plaintext), (i+1) * block_size)
        block = plaintext[start:end]
        pre = cipher[start:end]
        m = [int(block[j] != pre[j]) for j in range(len(pre))]
        
        cipher.extend(block_enc(m, key))
    return cipher[block_size:]



def pad(plaintext):
    padding_len = 16 - (len(plaintext) % 16)
    print(padding_len)
    if padding_len == 16:
         return plaintext
    padding = bytes([padding_len] * padding_len)
    return plaintext + padding


def xor_for_char(input_bytes, key_input):
    index = 0
    output_bytes = b''
    for byte in input_bytes:
        if index >= len(key_input):
            index = 0
        output_bytes += bytes(bool((byte) != bool(key_input[index])))
        index += 1
    return output_bytes


def padding(block_to_pad, block_length):
    smaller_size = len(block_to_pad)
    padding_size=block_length-smaller_size
    for i in range(padding_size):
        block_to_pad = block_to_pad +" "
    return block_to_pad   

    


class Client1:
    BLOCKSIZE=16
    # key2 = " "
    encrypt_key = " "
    file = " "
    mod=" "
    is_ready = False
    kc1_decr = " "
    cipher = " "


    def __init__(self,name, iv, key2):
        self.name=name
        self.iv=iv
        self.key2=key2



    def decrypt_key(self):
      cipher2 = AES.new(self.key2, AES.MODE_CBC, self.iv) 
      key1 = unpad(cipher2.decrypt(self.encrypt_key), self.BLOCKSIZE)
      return key1


    def encrypt_file_cbc(self):
        #  self.cipher = cipher_block_chaining(file, self.kc1_decr, self.iv, 128, aes_encoder)

      enc = pad(self.file) # here I pad the text (PCKS#7 way)
      nb_blocks = (int)(len(enc) / 16) #calculate the number of blocks I've to iter through
      cipher = AES.new(self.kc1_decr, AES.MODE_ECB)
      for i in range(nb_blocks):
            enc2 = xor_for_char(enc[i * 16:(i + 1) * 16], self.iv) #xor a block with IV
            self.iv = cipher.encrypt(enc2) # set the the IV based on the encryption of the xored text
            print(codecs.decode(codecs.encode(self.iv, 'base64')).replace("\n", ""), end='') #print the encrypted text in base 64


    def read_file():
      f = open(self.file, "r")
      if f.mode == 'r':
          content = f.readlines()
          for line_content in content:
              self.ecncrypy_file_cbc()
      f.close()   

    def encrypt_file_ecb(self): 
        self.cipher = electronic_cookbook(self.file, self.kc1_decr, 128, aes_encoder)    





