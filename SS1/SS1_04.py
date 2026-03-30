

def ror(x, n, w=8):
    n %= w
    mask = (1 << w) - 1
    return ((x >> n) | (x << (w - n))) & mask

def rol(x, n, w=8):
    n %= w
    mask = (1 << w) - 1
    return ((x << n) | (x >> (w - n))) & mask

with open('/home/lorenzopatti/Scaricati/flag.txt.aes', 'rb') as f:
    ciphertext = f.read()

plaintext = bytearray()
for i, b in enumerate(ciphertext):
    plaintext.append(rol(b, i + 1))

print(plaintext)  
print(plaintext.hex()) 
print(plaintext.decode('utf-8', errors='replace'))  