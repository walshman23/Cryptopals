#!/usr/local/bin/python

__author__ = 'Walshman23'

import sys
sys.path.insert(1, "../common") # Want to locate modules in our 'common' directory


# A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of plaintext into ciphertext.
# But we almost never want to transform a single block; we encrypt irregularly-sized messages.
#
# One way we account for irregularly-sized messages is by padding, creating a plaintext that is an even
# multiple of the blocksize. The most popular padding scheme is called PKCS#7.
#
# So: pad any block to a specific block length, by appending the number of bytes of padding to the end of the block.
# For instance,
#
# "YELLOW SUBMARINE"
#
# ... padded to 20 bytes would be:
#
# "YELLOW SUBMARINE\x04\x04\x04\x04"


# Get block from stdin

# Use 16 as block size

blocksize=16

buf = sys.stdin.read()

if len(buf) < blocksize:
    padlen = blocksize - len(buf)
else:
    padlen = len(buf) % blocksize

sys.stdout.write(buf)

if padlen != 0:
    sys.stdout.write(chr(padlen)*padlen)




