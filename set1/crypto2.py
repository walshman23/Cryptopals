#!/usr/bin/python

import binascii

# 2. Fixed XOR
# 
# Write a function that takes two equal-length buffers and produces
# their XOR sum.
# 
# The string:
# 
# 1c0111001f010100061a024b53535009181c
# 
# ... after hex decoding, when xor'd against:
# 
# 686974207468652062756c6c277320657965
# 
# ... should produce:
# 
# 746865206b696420646f6e277420706c6179


## Need to check that buffers are of equal length, die if not

def xor(buf1, buf2):
	assert len(buf1) == len(buf2)
	ret = bytearray(len(buf1))
	for i in range(len(buf1)):
 		ret[i] = ord(buf1[i]) ^ ord(buf2[i])
	return ret
	

buf1 = binascii.unhexlify("1c0111001f010100061a024b53535009181c") # Given
buf2 = binascii.unhexlify("686974207468652062756c6c277320657965") # Given

s = xor(buf1, buf2)


# Let's see what we have gotten
print s
print binascii.hexlify(s)  # the kid don't play




