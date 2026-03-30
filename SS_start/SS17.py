from pwn import *

HOST = "software-17.challs.olicyber.it"
PORT = 13000

r = remote(HOST, PORT)

# 1. Inizio
r.recvuntil(b"per iniziare ...")
r.sendline(b"a")

# 2. Ciclo per i 10 step
for i in range(10):
    print(r.recvuntil(b"["))

    print(r.recvuntil(b"["))

    data = r.recvline()

    data1 = data.strip().decode()[:len(data)-2].replace(",","").split()

    print(data1)

    data1 = [ int(n) for n in data1] 
    
    # Convertiamo e sommiamo
    numeri = [int(n) for n in data1]
    risultato = sum(numeri)
    
    print(f"Step {i+1}: Invio somma {risultato}")
    
    # Aspettiamo che il server ci chieda "Somma? :" prima di inviare
    r.recvuntil(b"Somma? :")
    r.sendline(str(risultato).encode())

# 3. Finiti i 10 step, il server manda la flag
print("\n--- FLAG ---")
r.interactive()