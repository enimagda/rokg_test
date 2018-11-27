# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 13:56:38 2018
@author: magdad
"""

#import numpy as np
'''import math
import hashlib
import rsa
import secrets
import string'''
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
import random

def eGCD(a, b):
    if b == 0:
        return (a, 1, 0)
    [x1, y1, x2, y2] = [1, 0, 0, 1]
    while b != 0:
        [q, r] = [a//b, a%b]
        [a, b] = [b, r]
        x = x1 - q * x2
        [x1, x2] = [x2, x]
        y = y1 - q * y2
        [y1, y2] = [y2, y]
    return [a, x1, y1]

def Inverse(a, n):
    [d, X, Y] = eGCD(a, n)
    if d != 1:
        return 0
    return X % n
#if __name__==__main__:
rand= Random.new().read
CH_obf=random.randint(1024,10000000000000000)
demoHash=12333211234567504662111
print("demoHash:",demoHash)
print("CH_obf:",CH_obf)
key = RSA.generate(1024, rand) #generate pub and priv key
print("keys.d:",key.d)

PK = key.publickey() # pub key export for exchange
print("PK(N):",PK)


encrypted = PK.encrypt(CH_obf, 32)
#message to encrypt is in the above line 'encrypt this message'
obfHash=demoHash*encrypted[0] %key.n
print("obfHash:",obfHash)
print ('encrypted message:' , encrypted) #ciphertext
f = open ('encryption.txt', 'w')
f.write(str(encrypted)) #write ciphertext to file
f.close()

#decrypted code below

f = open('encryption.txt', 'r')
message = f.read()


decrypted = key.decrypt(ast.literal_eval(str(message)))
print(type(ast.literal_eval(str(message))))
print ('decrypted:', decrypted)

f = open ('encryption.txt', 'w')
f.write(str(message))
f.write(str(decrypted))
f.close()

demoKey=key.decrypt((obfHash,None))*Inverse(CH_obf,key.n)%key.n
auth=PK.encrypt(demoKey,32)
skipR=key.decrypt(demoHash)
