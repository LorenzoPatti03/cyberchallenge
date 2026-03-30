from base64 import b64decode
s1 = 'ZmxhZ3t3NDF0XzF0c19hbGxfYjE=='
s1 = b64decode(s1).decode()

"""
SPIEGAZIONE CODIFICA BASE64
---------------------------

Il Base64 è un sistema di codifica che trasforma dati binari in una stringa di 
caratteri ASCII (testo semplice). È essenziale per trasmettere dati su canali 
che supportano solo testo (come email o JSON).

COME FUNZIONA:
1. RAGGRUPPAMENTO: Prende i dati originali a blocchi di 3 byte (24 bit totali).
2. DIVISIONE: Divide questi 24 bit in 4 nuovi gruppi da 6 bit ciascuno.
3. CONVERSIONE: Ogni gruppo da 6 bit (che può avere un valore da 0 a 63) 
   viene mappato su un carattere specifico usando l'alfabeto Base64:
   - A-Z (0-25)
   - a-z (26-51)
   - 0-9 (52-61)
   - + e / (62-63)



IL PADDING (=):
Se i dati originali non sono multipli di 3 byte, alla fine della stringa 
vengono aggiunti uno o due simboli "=" come "riempitivo" per completare 
l'ultimo blocco di bit.

ESEMPIO IN PYTHON:
import base64
encoded = base64.b64encode(b'ciao') # Risultato: b'Y2lhbw=='
"""

# Qui inizia il tuo codice...

s2 = 664813035583918006462745898431981286737635929725

# Calcoliamo i byte necessari (arrotondando per eccesso)
n_bytes = (s2.bit_length() + 7) // 8

# Convertiamo in bytes
b2 = s2.to_bytes(n_bytes, 'big')

# Decodifichiamo i bytes in stringa e stampiamo
s2 = b2.decode()

print(s1 + "" + s2)

"""
SPIEGAZIONE CONVERSIONE: INTERO -> BYTES -> STRINGA
--------------------------------------------------

1. n.bit_length(): 
   Restituisce il numero di bit necessari a rappresentare l'intero in binario.
   Esempio: il numero 255 ha 8 bit (11111111).

2. (n.bit_length() + 7) // 8:
   Formula per calcolare quanti BYTE (gruppi di 8 bit) servono per contenere il numero.
   - Si aggiunge 7 per arrotondare per eccesso (evitando che 1 bit rimanga fuori).
   - // è la divisione intera.

3. to_bytes(lunghezza, 'big'):
   Trasforma l'intero in una sequenza di byte reali (es. b'\x61').
   - 'big' (Big-Endian): Ordina i byte partendo dal più significativo (come leggiamo noi).
   - 'little' (Little-Endian): Ordina i byte partendo dal meno significativo.

4. decode('utf-8'):
   Il metodo finale. Prende i byte grezzi e li traduce in caratteri leggibili
   seguendo la tabella UTF-8 (es. il byte 0x61 diventa la lettera 'a').
"""


