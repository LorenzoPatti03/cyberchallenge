import struct

# Byte estratti da DAT_00104020 (Ghidra)
# Uso una stringa esadecimale per evitare errori di virgole o spazi
hex_data = (
    "54000000 c3000000 22010000 8b010000 df010000 44020000 b6020000 ea020000 "
    "5e030000 c3030000 22040000 8b040000 c0040000 1f050000 87050000 dc050000 "
    "49060000 aa060000 f8060000 57070000 cb070000 fb070000 5a080000 cc080000 "
    "ff080000 42090000 b7090000 090a0000 7c0a0000 e10a0000 400b0000 a40b0000 "
    "d50b0000 4b0c0000 b40c0000 220d0000 870d0000"
)

# Puliamo la stringa e convertiamola in byte reali
clean_hex = hex_data.replace(" ", "").replace("\n", "")
binary_data = bytes.fromhex(clean_hex)

# 1. Estraiamo gli interi a 32-bit (Little Endian)
# 'I' sta per unsigned int, '<' sta per Little Endian
targets = []
for i in range(0, len(binary_data), 4):
    val = struct.unpack('<I', binary_data[i:i+4])[0]
    targets.append(val)

# 2. Ricostruiamo la stringa risolvendo la somma cumulativa
password = ""
current_sum = 0

for t in targets:
    char_code = t - current_sum
    password += chr(char_code)
    current_sum = t

print("-" * 30)
print(f"STRINGA TROVATA: {password}")
print("-" * 30)

# Comando per testare il programma
print(f"\nProva a lanciare il programma così:")
print(f"./nome_programma \"{password}\"")