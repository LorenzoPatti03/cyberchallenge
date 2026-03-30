import string

def brute_force_xor_no_clue(ciphertext):
    data = bytes.fromhex(ciphertext)
    
    # Definiamo cosa consideriamo "leggibile" (lettere, numeri, spazi, punteggiatura)
    printable = set(string.printable.encode())

    for key in range(256):
        decoded = bytes([b ^ key for b in data])
        
        # Calcoliamo quanti caratteri sono effettivamente leggibili
        printable_count = sum(1 for b in decoded if b in printable)
        
        # Se quasi tutti i caratteri (es. > 90%) sono leggibili, stampiamo!
        if printable_count / len(decoded) > 0.9:
            print(f"Chiave: {key} ({chr(key)})")
            try:
                print(f"Testo: {decoded.decode('ascii')}")
            except:
                print(f"Testo (raw): {decoded}")
            print("-" * 20)

ciphertext = '104e137f425954137f74107f525511457f5468134d7f146c4c'
brute_force_xor_no_clue(ciphertext)