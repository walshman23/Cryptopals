#!/usr/bin/python


# // ------------------------------------------------------------
# 4. Detect single-character XOR
# 
# One of the 60-character strings at:
# 
#  https://gist.github.com/3132713
# 
# has been encrypted by single-character XOR. Find it. (Your code from
# #3 should help.)

import sys
sys.path.insert(1, "../common") # Want to locate modules in our 'common' directory


import string
import binascii
import ltrfreq
import utils

scores = []
results = []
lineno = 0



with open("gistfile1.txt") as f:
	for line in f:
		lineno = lineno + 1;		
		hexstring = string.rstrip(line)
		b = binascii.unhexlify(hexstring) 	
		for key in range(256):
			candidatebuf = utils.xor(key, b)
			scores.append(ltrfreq.totcscore(candidatebuf) + ltrfreq.norvigscore(candidatebuf)) 
			spiffy = utils.SpiffyPrint(candidatebuf)
			results.append(spiffy)
				

print "Highest score is", max(scores), " Sekrit message is", results[scores.index(max(scores))]
print "Sekrit message came from line", scores.index(max(scores))/256 + 1

# Now that the party is jumping. //  7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f