#!/usr/bin/python

mystring = "Hello, World"

print mystring

c = 0xcc
def singlebytexor(c, buf):
	ret = bytearray(len(buf))
	for i in range(len(buf)):
 		ret[i] = c ^ ord(buf[i])
	return ret
	
res = singlebytexor(c, mystring)

SpiffyPrint(res)