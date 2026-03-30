from pwn import *

HOST = "software-19.challs.olicyber.it"
PORT = 13002
exe = ELF('/home/lorenzopatti/Scaricati/sw-19')

r = remote(HOST, PORT)

# Fase iniziale
r.recvuntil(b'iniziare ...')
r.sendline(b"a")

print("[*] Ciclo iniziato. Parsing: '-> nome:'")

for i in range(20):
    try:
        # 1. Leggiamo tutto fino alla freccia '-> '
        r.recvuntil(b'-> ')
        
        # 2. Ora leggiamo fino ai due punti ':'
        # Il contenuto tra '-> ' e ':' è il nome della funzione
        name_bytes = r.recvuntil(b':', drop=True)
        name = name_bytes.decode().strip()
        
        print(f"[{i+1}] Trovato: '{name}'", end=" ")
        
        # 3. Cerchiamo l'indirizzo e rispondiamo
        if name in exe.sym:
            addr = exe.sym[name]
            r.sendline(hex(addr).encode())
            print(f"-> Inviato: {hex(addr)}")
        else:
            print(f"\n[!] Errore: '{name}' non trovato nell'ELF!")
            break
            
    except EOFError:
        print("\n[!] Connessione chiusa. Forse troppo lento o errore di risposta.")
        break

# Riceviamo il flag
print("\n--- RISULTATO ---")
print(r.recvall(timeout=1).decode())