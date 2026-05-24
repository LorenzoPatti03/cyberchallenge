from pwn import *

HOST = "software-18.challs.olicyber.it"
PORT = 13001

r = remote(HOST, PORT)

print(r.recvuntil(b'iniziare ...').decode())
r.sendline(b"a")

for i in range(100):
    print(r.recvuntil(b'restituiscimi '))

    data = r.recvline()
    print(data)
    data = data.split()
    data_str = data[0]
    tipo_pkt = data[3]
    num = int(data_str, 16) #prima trasformo in numero cosi glielo faccio intepreta come nuemro a p64
    if tipo_pkt == '64-bit'.encode():
        payload = p64(num)
    else:
        payload = p32(num)

    r.send(payload)

print('----------------------------')
print(r.recvline())
print(r.recvline())
