
from Crypto.Util.number import isPrime, getPrime
import random
import string
import os
from math import gcd

from pwn import *
'''
HOST = "RSA-slot-machine.challs.cyberchallenge.it"
PORT = 38214
r = remote(HOST, PORT)


data =  r.recvuntil(b'encrypted!')
print(data)
data = r.recvline().decode()
print(data)
data = r.recvline().decode()
print(data)


n = data.split(' ')[2]
print(n)


for _ in range(150):
    data = r.recvuntil(b'choice:')
    print(data)
    
    r.sendline(b'block_idx')
    
    
data = r.recvuntil(b'choice:')


r.sendline(b'respin')

data = r.recvline().decode()
print(data)


new_n = data.split(' ')[3]
print(new_n)


print()
cont = 0


for i in range(len(n)):
    if n[i] == new_n[i]:
        cont += 1
        
print( cont)
'''
