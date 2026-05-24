from pwn import *

HOST = "piecewise.challs.cyberchallenge.it"
PORT = 9110


r = remote(HOST,PORT)


def first_step():
    print( r.readline().decode()   )
    r.sendline(b'\n')
    print( r.readline().decode()   )
    
def third_step():
    print(r.recvuntil(b'number ')  )
    number = int(r.recvline().strip().split()[0])
    # 64-bit big-endian integer
    r.sendline((number).to_bytes(8, byteorder='big'))
    print(r.recvline().decode())
    
#first_step()
#first_step()
third_step()

