
import re
import string

def xor(c, buf):
	ret = bytearray(len(buf))
	for i in range(len(buf)):
 		ret[i] = c ^ ord(buf[i])
	return ret

def rkxor(key, buf):
	assert len(buf) >= len(key)
	ret = bytearray(len(buf))
	for i in range(len(buf)):
 		ret[i] = ord(key[i%len(key)]) ^ ord(buf[i])
	return ret
	
def hamming(s1, s2):
	assert len(s1) == len(s2)
	ret = 0
	for i in range(len(s1)):
		byte = ord(s1[i]) ^ ord(s2[i])
		# slow and evil, but works.  
		# Via http://stackoverflow.com/questions/2576712/using-python-how-can-i-read-the-bits-in-a-byte
		# Ver 2 will use http://code.google.com/p/python-bitstring/
		byte = bin(byte)[2:].rjust(8, '0')  
		# now byte contains a string with 0s and 1s.
		for bit in byte:
			ret = ret + int(bit)

	return ret	
	
# Stolen from http://stackoverflow.com/questions/1800790/munging-non-printable-characters-to-dots-using-string-translate	

def SpiffyPrint(uglystr):
		return re.sub('[^'+string.printable[:-5]+']','.',uglystr)
