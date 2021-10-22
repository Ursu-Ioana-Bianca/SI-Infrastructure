#!/usr/bin/env python3
import manager
from client1 import Client1
from client2 import Client2
from manager import Manager
from Crypto import Random
from Crypto.Cipher import AES
from os import urandom
from Crypto.PublicKey import RSA
import random


def checkCon(c1, c2, m):
  conv=0
  if conv == 0:   
    names = input("Enter two participants to communicate: ")
    delim = " "
    partners = names.split(delim)
    while len(partners)!=2:
       names = input("Enter two participants to communicate: ")
       delim = " "
       partners = names.split(delim)

    first_name = partners[0]
    second_name = partners[1]

    if first_name== c1.name:
      if second_name == m.name:
         conv1(c1, m)
      elif second_name == c2.name:
        conv2(c1, c2)
    elif first_name == c2.name: 
        if second_name == c1.name: 
           conv3(c2, c1)
    elif names == "exit now":
        conv=-1
  return conv    

      
 


def conv1(c1, m): #ce trimite A catre KeyManager
    ok=False
    while(ok==False):
      request = input("Enter your request: ")
      if request == "give the key" or request == "key":
          ok=True
          key = m.encryptKey()
          c1.encrypt_key=key
          



def conv2(c1, c2):  #ce trimite A catre B 
  if c1.mod == " ":
     mod = input(" {} :Choose between ECB or CBC: ".format(c1.name))

     if mod=="ECB":
         c1.mod=mod
         c2.mod=mod
         
     elif mod=="CBC":
         c1.mod=mod
         c2.mod=mod

     if(c1.encrypt_key):
         c2.encrypt_key=c1.encrypt_key  # dau cheia criptata si lui B
         c1.kc1_decr = c1.decrypt_key()  # decriptez sa ajun la cheia k 
         c2.kc2_decr = c2.decrypt_key()  # cheia k
     else:
         print("{} first you should get the key from KeyManager".format(c1.name))
         checkCon(c1, c2, m) 
  elif c2.is_ready:
    if c1.mod == "CBC":
      c1.is_ready = True
      c1.encrypt_file_cbc()
    elif c1.mod == "ECB":
      c1.encrypt_file_ecb()
      c1.is_ready = True



def conv3(c2, c1):  # ce trimite B catre A
  if c2.is_ready == False:
    ok=False 
    while ok == False:
      start = input("{} if you want to start to commnuicate with {} write start : ".format(c2.name, c1.name))
      if start == "start":
        ok=True
        c2.is_ready = True
  else:
    if c1.is_ready:
      # print(c2.decrypt_file(c1.cipher))      
      print(c2.decrypt_file(c1.iv))
      print(c1.file)



if __name__ == "__main__":

  block_size = 16
  # key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
  # print(key)
  key2 = bytearray(urandom(block_size))
  # print(key2)
  iv = Random.new().read(AES.block_size)
  name1 = input("Enter first name client: ")
  c1 = Client1(name1, iv, key2)
  c1.file = "trimite mesaj A catre B"

  name2 =  input("Enter second name client: ")
  c2 = Client2(name2, iv, key2)

  name_manager =input("Enter name manager: ")
  m = Manager(name_manager, iv, key2)

  conv = 0
  while(conv != -1):
    conv = checkCon(c1, c2, m)








  



  
