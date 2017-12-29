# Created for BADS 2018
# See README.md for details
# This is python3
import sys
import struct
"""
Binary standard output. This class provides methods for converting
some primitive type variables (boolean, byte, char, and int)
to sequences of bits and writing them
to an output stream.
The output stream can be standard output or another outputstream.
Uses big-endian (most-significant byte first).

The client must flush() the output stream when finished writing bits.

The client should not intermix calls to BinaryOut with calls to stdout;
otherwise unexpected behavior will result.
"""
class BinaryStdOut:
	out = sys.stdout.buffer
	buffer_ = 0
	n = 0
	is_init = False
	@staticmethod
	def _initialize():
		BinaryStdOut.buffer_ = 0 #8-bit buffer of bits to write out
		BinaryStdOut.n = 0 #number of bits used in buffer
		BinaryStdOut.is_init = True
	@staticmethod
	def _writeBit(x):
		if(not BinaryStdOut.is_init):
			BinaryStdOut._initialize()
		BinaryStdOut.buffer_ <<= 1
		if(x):
			BinaryStdOut.buffer_ |=1
		BinaryStdOut.n += 1
		if(BinaryStdOut.n == 8):
			BinaryStdOut._clearBuffer()
	@staticmethod
	def _writeByte(x):
		if(not BinaryStdOut.is_init):
			BinaryStdOut._initialize()
		assert x >= 0 and x < 256
		#optimized if byte-alligned
		if(BinaryStdOut.n == 0):
			BinaryStdOut.out.write(struct.pack('B',x))
			return
		#otherwise write one bit at a time
		for i in range(0,8):
			bit = ((x >> (8 - i - 1)) & 1) == 1
			BinaryStdOut._writeBit(bit)
	@staticmethod
	def _clearBuffer():
		if(not BinaryStdOut.is_init):
			BinaryStdOut._initialize()
		if(BinaryStdOut.n == 0):
			return
		if(BinaryStdOut.n > 0):
			BinaryStdOut.buffer_ <<= (8-BinaryStdOut.n)
		BinaryStdOut.out.write(struct.pack('B',BinaryStdOut.buffer_))
		BinaryStdOut.n = 0
		BinaryStdOut.buffer_ = 0
	@staticmethod
	def flush():
		BinaryStdOut._clearBuffer()
		BinaryStdOut.out.flush()
	@staticmethod
	def close():
		BinaryStdOut.flush()
		BinaryStdOut.out.close()
		BinaryStdOut.is_init = False
	@staticmethod
	def write_bool(x):
		BinaryStdOut._writeBit(x)
	@staticmethod
	def write_byte(x):
		BinaryStdOut._writeByte(x & 0xff)

	def write_int(x):
		BinaryStdOut._writeByte(((x >> 24)& 0xff))
		BinaryStdOut._writeByte(((x >> 16)& 0xff))
		BinaryStdOut._writeByte(((x >> 8)& 0xff))
		BinaryStdOut._writeByte(((x >> 0)& 0xff))

	def write_char(x):
		if(ord(x)<0 or ord(x)>=256):
			raise ValueError("Illegal 8-bit char = {}".format(x))
		BinaryStdOut._writeByte(ord(x))

	def write_string(s):
		for i in s:
			BinaryStdOut.write_char(s[i])
def main():
	for i in sys.argv[1]:
		BinaryStdOut.write_char(i)
	BinaryStdOut.close()
if __name__ == '__main__':
	main()