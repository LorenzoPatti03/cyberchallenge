import string
import base64
import binascii
from itertools import product

"""
Brute force completo su due chiavi da 4 caratteri minuscoli.

Strategia:
1) Prova tutte le combinazioni di k1 e k2 (26^4 * 26^4).
2) Decifra il ciphertext due volte:
     d = decrypt(c, k2)
     p = decrypt(d, k1)
3) Se p coincide con il plaintext noto, si ferma subito.
"""



m = "See you later in the city center"
c = "QSldSTQ7HkpIJj9cQBY3VUhbQ01HXD9VRBVYSkE6UWRQS0NHRVE3VUQrTDE="



def decrypt(enc, key):
    dec = []
    try:
        enc = base64.urlsafe_b64decode(enc.encode('ascii')).decode('ascii')
    except (binascii.Error, UnicodeDecodeError):
        return None
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((128 + ord(enc[i]) - ord(key_c)) % 128)
        dec.append(dec_c)
    return "".join(dec)


def all_keys(length=4):
    for chars in product(string.ascii_lowercase, repeat=length):
        yield "".join(chars)


def brute_force_keys(known_plaintext, final_ciphertext):
    for k2 in all_keys(4):
        d = decrypt(final_ciphertext, k2)
        if d is None:
            continue
        for k1 in all_keys(4):
            p = decrypt(d, k1)
            if p is None:
                continue
            if p == known_plaintext:
                return k1, k2, d
    return None


result = brute_force_keys(m, c)

if result is None:
    print("Nessuna chiave trovata")
else:
    k1, k2, d = result
    print(f"k1 = {k1}")
    print(f"k2 = {k2}")
    print(f"d  = {d}")
    print(f"KEY = {k1 + k2}")