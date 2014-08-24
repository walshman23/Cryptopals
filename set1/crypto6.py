#!/usr/bin/python

# // ------------------------------------------------------------
#  
#  6. Break repeating-key XOR
#  
#  The buffer at the following location:
#  
#  https://gist.github.com/3132752
#  
#  is base64-encoded repeating-key XOR. Break it.
#  
#  Here's how:
#  
#  a. Let KEYSIZE be the guessed length of the key; try values from 2 to
#  (say) 40.
#  
#  b. Write a function to compute the edit distance/Hamming distance
#  between two strings. The Hamming distance is just the number of
#  differing bits. The distance between:
#  
#   this is a test
#  
#  and:
#  
#   wokka wokka!!!
#  
#  is 37.
#  
#  c. For each KEYSIZE, take the FIRST KEYSIZE worth of bytes, and the
#  SECOND KEYSIZE worth of bytes, and find the edit distance between
#  them. Normalize this result by dividing by KEYSIZE.
#  
#  d. The KEYSIZE with the smallest normalized edit distance is probably
#  the key. You could proceed perhaps with the smallest 2-3 KEYSIZE
#  values. Or take 4 KEYSIZE blocks instead of 2 and average the
#  distances.
#  
#  e. Now that you probably know the KEYSIZE: break the ciphertext into
#  blocks of KEYSIZE length.
#  
#  f. Now transpose the blocks: make a block that is the first byte of
#  every block, and a block that is the second byte of every block, and
#  so on.
#  
#  g. Solve each block as if it was single-character XOR. You already
#  have code to do this.
#  
#  e. For each block, the single-byte XOR key that produces the best
#  looking histogram is the repeating-key XOR key byte for that
#  block. Put them together and you have the key.
#

import sys
sys.path.insert(1, "../common") # Want to locate modules in our 'common' directory


import string
import binascii
import utils
import ltrfreq

s1 = "this is a test"
s2 = "wokka wokka!!!"

hamster = utils.hamming(s1, s2)
print hamster

assert hamster == 37


# That's all for now - below here doesnt work

decoded = []
bytes1 = []
bytes2 = []

minkeylength = 2
maxkeylength = 40


with open("./gistfile3132752.txt") as f:
    rawf = f.read()
    decoded += binascii.a2b_base64(rawf)

buflength = len(decoded)




for keysize in range(minkeylength, maxkeylength + 1):
    numbufs = buflength/keysize
    bufpairs = numbufs/2
  #  print "Input contains", buflength, "bytes, allowing for", numbufs,"buffers of", keysize,"bytes to be read"
    accumulator = 0.0;
    for bufpairno in range(1,bufpairs,2):
        #read pair of bufs
        #  print "buf1",(bufpairno-1)*keysize, bufpairno*keysize - 1
        #  print "buf2",bufpairno*keysize, (bufpairno+1)*keysize - 1
        tbuf1 = decoded[(bufpairno-1)*keysize:bufpairno*keysize - 1] #Check this
        tbuf2 = decoded[(bufpairno)*keysize:(bufpairno+1)*keysize - 1] #This too

        #score pair of bufs
        accumulator = accumulator + utils.hamming(tbuf1,tbuf2)

    #Score for this keysize is (accumulator/bufpairs)/keysize
    print "Score for keylength", keysize, "is", (accumulator/bufpairs)/keysize

# Keysize of 2 seems lowest. Hmmm. I smell a bug.
