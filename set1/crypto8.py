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


def uniquechunks(buf, size):
    bufcount = {}
    uniqs = 0
    for bufno in range(0, len(buf)/chunksize):
        tbuf = binascii.hexlify(buf[bufno*size:(bufno+1)*size])
        if  tbuf not in bufcount:
            bufcount[tbuf] = 1
            uniqs += 1
        else:
            bufcount[tbuf] += 1


    return uniqs



with open("./8.txt") as f:
    content  = f.readlines()

for line in content:
    b = binascii.unhexlify(line.strip())
    print "Line", lineno, "has", uniquechunks(b, chunksize), "unique chunks"
    lineno += 1

# Line 133 is ours


