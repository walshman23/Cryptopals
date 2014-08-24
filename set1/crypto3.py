#!/usr/bin/python

# // ------------------------------------------------------------
# 
# 3. Single-character XOR Cipher
# 
# The hex encoded string:
# 
#      1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
# 
# ... has been XOR'd against a single character. Find the key, decrypt
# the message.
# 
# Write code to do this for you. How? Devise some method for "scoring" a
# piece of English plaintext. (Character frequency is a good metric.)
# Evaluate each output and choose the one with the best score.
# 
# Tune your algorithm until this works.

import sys
sys.path.insert(1, "../common") # Want to locate modules in our 'common' directory
import binascii
import string
import utils
import ltrfreq






b = binascii.unhexlify("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736") # Given

scores = []
results = []


for key in range(256):
	candidatebuf = utils.xor(key, b)
	scores.append(ltrfreq.totcscore(candidatebuf) + ltrfreq.norvigscore(candidatebuf)) # Score this candidate buffer, add its score to list
	spiffy = utils.SpiffyPrint(candidatebuf)
	print  scores[key] , key, spiffy
	results.append(spiffy)
	
print "Highest score is", max(scores), " Sekrit message is", results[scores.index(max(scores))]

	


	
	
	

	




