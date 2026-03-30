m1 = '158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf'
m2 = '73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2'


def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

print( xor( bytes.fromhex(m1), bytes.fromhex(m2)))

"""
SPIEGAZIONE OPERAZIONE XOR TRA BYTE
-----------------------------------
Questa riga esegue un'operazione XOR bit a bit tra due sequenze (a e b).

1. zip(a, b):
   Prende le due sequenze e le accoppia elemento per elemento. 
   Esempio: se a=[1, 2] e b=[3, 4], zip produce (1,3) e (2,4).
   Si ferma quando la sequenza più corta finisce.

2. [x ^ y for x, y in ...]:
   È una 'list comprehension'. Per ogni coppia (x, y), esegue l'operazione 
   matematica XOR (^). 
   - In crittografia, lo XOR è fondamentale perché è reversibile: 
     Se (A ^ B) = C, allora (C ^ B) = A.

3. bytes([...]):
   Trasforma la lista di numeri risultanti (es. [110, 105, 108]) di nuovo 
   in un oggetto di tipo bytes pronto per essere decodificato o trasmesso.
"""

# Esempio d'uso:
# a = b"secret"
# b = b"keykey"
# flag = bytes([x ^ y for x, y in zip(a, b)])