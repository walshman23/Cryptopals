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
maxkeylength = 41


with open("set1/gistfile3132752.txt") as f:
    for line in f:
        decoded += binascii.a2b_base64(line)

buflength = len(decoded)




for keysize in range(minkeylength, maxkeylength):
    numbufs = buflength/keysize
    print "Input contains", buflength, "bytes, allowing for", numbufs,"buffers of", keysize,"bytes to be read"
    for i in range(1,numbufs/2):
        #read pair of bufs
        tbuf1 = decoded[(i-1)*keysize:i*keysize]
        tbuf2 = decoded[(i)*keysize:(i+1)*keysize]
        #score pair of bufs

        #add score to accumulator
        #end
    #Score for this keysize is (accumulator/bufpairs)/keysize


