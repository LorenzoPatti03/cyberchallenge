flag = [0x43, 0xa1, 0x52, 0x8a, 0xb7, 0x1b, 0xa1, 0x68, 0x5f, 0xb1, 0x1a, 0x86, 0xf5, 0x93, 0xcc, 0xc2, 0x6c, 0xaf, 0xdc, 0xad, 0x03, 0x7b, 0xd1, 0xd0, 0x5f, 0x31, 0x4e, 0x2c, 0x53, 0x13, 0xe0, 0xc8, 0x37, 0xbe, 0x00]
'''    transform = (byte)(index >> 31);
    transform = ((char)index + (transform >> 5) & 7) - (transform >> 5) & 7;
    mamory[index] = (byte)flag[index] >> transform | flag[index] << 8 - transform;
    encrypt_string(flag,mamory,index + 1);'''

result = []

for i in range(len(flag)):
    transform = i >> 31
    transform = ((i + (transform >> 5) & 7)) - ((transform >> 5) & 7)
    item = (flag[i] << transform) | (flag[i] >> (8 - transform)) 
    result.append(chr(item & 0xff))
    
    
    
    
print(''.join(result))