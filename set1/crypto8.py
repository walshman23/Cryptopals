#!/usr/local/bin/python

__author__ = 'Walshman23'

#
# In this file are a bunch of hex-encoded ciphertexts.
#
# One of them has been encrypted with ECB.
#
# Detect it.
#
# Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext.
#


# The approach is to find the ciphertext which has the fewest unique 16-byte chunks.

import sys
sys.path.insert(1, "../common") # Want to locate modules in our 'common' directory
import binascii

lineno=1
chunksize=16


# TODO: write real code to count unique chunks in buffer
def uniquechunks(buf, size):
    return 42


with open("./8.txt") as f:
    content  = f.readlines()

for line in content:
    b = binascii.unhexlify(line.strip())
    print "Line", lineno, "has", uniquechunks(b, chunksize), "unique chunks of length", chunksize
    lineno += 1


