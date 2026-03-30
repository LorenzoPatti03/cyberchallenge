import os

# --- SIMULAZIONE DEL SERVER (L'ORACOLO) ---
BLOCK_SIZE = 16
KEY = os.urandom(16) # Chiave segreta (l'attaccante non la conosce)

def pkcs7_padding(data):
    pad_len = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([pad_len] * pad_len)

def check_padding(data):
    """L'Oracolo: restituisce True se il padding è valido, False altrimenti."""
    pad_len = data[-1]
    if pad_len < 1 or pad_len > BLOCK_SIZE:
        return False
    return all(b == pad_len for b in data[-pad_len:])

def oracle(ciphertext, iv):
    # In un attacco reale, qui decifreresti con AES. 
    # Per semplicità logica, simuliamo il comportamento post-decifrazione XOR.
    # L'attaccante modifica l'IV per influenzare il plaintext.
    
    # Valore intermedio (risultato di AES_decrypt senza lo XOR finale)
    # NB: In un attacco reale questo valore è fisso ma ignoto.
    intermediate_value = b"\xAA" * 15 + b"\x42" 
    
    # Il plaintext che il server vede è: Intermediate XOR IV
    decrypted_block = bytes([a ^ b for a, b in zip(intermediate_value, iv)])
    return check_padding(decrypted_block)

# --- SIMULAZIONE DELL'ATTACCANTE ---
def padding_oracle_attack_example():
    print("### INIZIO ATTACCO PADDING ORACLE ###")
    
    # Immaginiamo che questo sia l'IV originale intercettato
    original_iv = b"\x00" * 16 
    
    # Vogliamo scoprire l'ultimo byte del valore intermedio
    # Creiamo un IV farlocco che modificheremo
    modified_iv = bytearray([0] * 16)
    
    print(f"Obiettivo: Trovare l'ultimo byte del valore intermedio.")
    print("Provo tutti i valori (0-255) per l'ultimo byte dell'IV...\n")

    found_byte_iv = None
    for val in range(256):
        modified_iv[-1] = val
        
        # Chiediamo all'oracolo se questo IV produce un padding valido (0x01)
        if oracle(None, modified_iv):
            found_byte_iv = val
            print(f"[!] Trovato valore IV che genera padding 0x01: {hex(val)}")
            break

    if found_byte_iv is not None:
        # Calcolo: Intermediate = IV_modificato XOR Padding_atteso
        # In questo caso il padding atteso è 0x01
        intermediate_byte = found_byte_iv ^ 0x01
        print(f"-> Byte intermedio calcolato: {hex(intermediate_byte)}")
        
        # Ora che abbiamo il byte intermedio, recuperiamo il Plaintext originale!
        # Plaintext = Intermediate XOR IV_originale
        plaintext_byte = intermediate_byte ^ original_iv[-1]
        print(f"-> Byte originale del messaggio: {chr(plaintext_byte)} (hex: {hex(plaintext_byte)})")
    else:
        print("Byte non trovato. Qualcosa è andato storto.")

if __name__ == "__main__":
    padding_oracle_attack_example()