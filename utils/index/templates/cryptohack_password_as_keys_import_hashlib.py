

import hashlib

import requests

ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

with open('/usr/share/dict/words', 'r') as f:
    words_db = set(word.strip().lower() for word in f)
    

for word in words_db:
    # KEY deve essere una stringa esadecimale per l'URL
    key_hex = hashlib.md5(word.encode()).hexdigest()
    
    url = f'https://aes.cryptohack.org/passwords_as_keys/decrypt/{ciphertext}/{key_hex}/'
    r = requests.get(url)
    data = r.json()
    print(f"Trying key: {word} -> {key_hex}")
    if "plaintext" in data:
        pt_hex = data["plaintext"]
        # Convertiamo in byte per cercare la flag senza rischiare crash di decode()
        pt_bytes = bytes.fromhex(pt_hex)
        
        if b"crypto{" in pt_bytes:
            print(f"Flag trovata: {pt_bytes.decode()}")
            break