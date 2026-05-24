import itertools

from Crypto.Cipher import AES


KEY = b"yn9RB3Lr43xJK2"

last_block_hex = "78c670cb67a9e5773d696dc96b78c4e0"
first_block_prefix_hex = "c5"
first_block_suffix_hex = "d49e"
first_block_prefix = bytes.fromhex(first_block_prefix_hex)
first_block_suffix = bytes.fromhex(first_block_suffix_hex)
last_block = bytes.fromhex(last_block_hex)

msg = "AES with CBC is very unbreakable".encode()


def xor_bytes(left, right):
    return bytes(a ^ b for a, b in zip(left, right))


found_key = None
recovered_first_ciphertext = None

for b1, b2 in itertools.product(range(256), repeat=2):
    key = KEY + bytes([b1, b2])

    aes = AES.new(key, AES.MODE_ECB)
    plain_last_block = aes.decrypt(last_block)
    candidate_first_ciphertext = xor_bytes(plain_last_block, msg[16:32])

    if candidate_first_ciphertext.startswith(first_block_prefix) and candidate_first_ciphertext.endswith(first_block_suffix):
        found_key = key
        recovered_first_ciphertext = candidate_first_ciphertext
        break


print("Chiave trovata: ", found_key)
print("Primo blocco cifrato: ", recovered_first_ciphertext)

aes = AES.new(found_key, AES.MODE_ECB)
decrypted_first_block = aes.decrypt(recovered_first_ciphertext)
IV = xor_bytes(decrypted_first_block, msg[0:16])
print("IV trovato: ", IV)

# Logica usata:
# 1) In CBC ogni blocco viene cifrato con la formula C_i = E_K(P_i XOR C_{i-1}),
#    dove C_0 coincide con l'IV.
# 2) Parto dall'ultimo blocco cifrato C_2, lo decifro con AES in ECB per ottenere
#    D_K(C_2). Questo non e' ancora il plaintext, perche' in CBC va ancora tolto
#    l'effetto del blocco precedente.
# 3) Faccio XOR tra D_K(C_2) e il plaintext noto del secondo blocco P_2: cosi'
#    ricavo il ciphertext del primo blocco C_1.
# 4) Le prime informazioni del challenge mi dicono solo alcuni byte di C_1
#    (prefisso c5 e suffisso d49e). Provo quindi tutte le 65536 possibilita'
#    delle ultime due byte della key e tengo solo la candidata che produce un
#    C_1 coerente con quei byte noti.
# 5) Una volta trovata la key, decifro C_1 con AES-ECB e faccio XOR con P_1.
#    Il risultato e' l'IV, perche' in CBC il primo blocco usa proprio l'IV al
#    posto del blocco precedente.
    

