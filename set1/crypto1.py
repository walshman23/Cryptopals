#!/usr/bin/python 

# Chris Walsh is to be blamed 

#------------------------------------------------------------
#
# 1. Convert hex to base64 and back.
#
# The string:
#
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
#
# should produce:
#
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
#
# Now use this code everywhere for the rest of the exercises. Here's a
# simple rule of thumb:
#
# Always operate on raw bytes, never on encoded strings. Only use hex
# and base64 for pretty-printing.
#

import base64
import string
import binascii

hexstring_1 = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d" # Given
desideratum = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'  # Wanted

print "Original hex string: "
print hexstring_1
print "What we want:  "
print desideratum

barr = bytearray.fromhex(hexstring_1)
result_1 = string.rstrip(base64.encodestring(barr))

print "What we have: "
print result_1


# Now we have our result and can see if it is what is desired
result_1 == desideratum

# Converting from base64 back to hex

hexstring_2 = binascii.hexlify(binascii.a2b_base64(desideratum))


print "Rebuilt hex string: " 
print hexstring_2


# Is this what we started with?

hexstring_1 == hexstring_2  # should be TRUE

print barr   # See below

### I'm killing your brain like a poisonous mushroom





