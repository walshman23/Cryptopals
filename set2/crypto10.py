#!/usr/local/bin/python

__author__ = 'Walshman23'
import sys
sys.path.insert(1, "../common") # Want to locate modules in our 'common' directory

# CBC mode is a block cipher mode that allows us to encrypt irregularly-sized messages, despite the fact that a block
# cipher natively only transforms individual blocks.
#
# In CBC mode, each ciphertext block is added to the next plaintext block before the next call to the cipher core.
#
# The first plaintext block, which has no associated previous ciphertext block, is added to a
# "fake 0th ciphertext block" called the initialization vector, or IV.
#
# Implement CBC mode by hand by taking the ECB function you wrote earlier, making it encrypt instead of decrypt
# (verify this by decrypting whatever you encrypt to test), and using your XOR function from the previous exercise
# to combine them.
# The file at http://cryptopals.com/static/challenge-data/10.txt is intelligible (somewhat) when CBC decrypted against
#  "YELLOW SUBMARINE" with an IV of all ASCII 0


import binascii
import utils

from Crypto.Cipher import AES

blocksize = 16
key = b'YELLOW SUBMARINE'
iv = blocksize*chr(0)

cipher_encrypt = AES.new(key, AES.MODE_CBC, iv)
cipher_decrypt = AES.new(key, AES.MODE_CBC, iv)


plaintext="Attack at Dawn!\n"

#with open("./10.txt") as f:
#buf = f.read(blocksize)
ciphertext = cipher_encrypt.encrypt(plaintext)

print plaintext, "->", ciphertext, "->", cipher_decrypt.decrypt(ciphertext)

