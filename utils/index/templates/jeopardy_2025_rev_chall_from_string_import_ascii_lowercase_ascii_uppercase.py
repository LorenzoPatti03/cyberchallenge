from string import ascii_lowercase, ascii_uppercase

from pwn import *

HOST = "rev-chall.challs.cyberchallenge.it"
PORT = 38211
r = remote(HOST, PORT)

alfabeto = ascii_lowercase + '{_*!}0123456789' 
print(alfabeto)
flag = ['C','C','I','T','{','4','n','d','_','t','h','3','_','b','3','s','t','_','r','3','v','_','p','l','4','y','3','r','_','4','w','4','r','d','_','g','0','3','s','_','t','0','_','d','5','3','5','a','2','7','4','}']
score = []

for i in range(20):
    data = r.recvuntil(b"flag:")
    
    for c in alfabeto:
        print("".join(flag) + c)
        prova = bin(int.from_bytes( ("".join(flag) + c).encode(), "big") )
        
        r.sendline( prova )
        
        data = r.recvline().decode()
        print(data)
        data = int(data.split(' ')[3])
        score.append(data)
        if data == ((len(flag)+1) * 9 ) - len(flag):
            print('tmp_flag: ' + "".join(flag) + c)
            print(score)
            score = []
            flag.append(c)
            break
        
        
print( "".join(flag))
