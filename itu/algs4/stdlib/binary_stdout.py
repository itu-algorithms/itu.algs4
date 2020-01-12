# Created for BADS 2018
# See README.md for details
# This is python3
import struct
import sys


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
	def _write_bit(x):
		if(not BinaryStdOut.is_init):
			BinaryStdOut._initialize()
		BinaryStdOut.buffer_ <<= 1
		if(x):
			BinaryStdOut.buffer_ |=1
		BinaryStdOut.n += 1
		if(BinaryStdOut.n == 8):
			BinaryStdOut._clear_buffer()
	@staticmethod
	def _write_byte(x):
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
			BinaryStdOut._write_bit(bit)
	@staticmethod
	def _clear_buffer():
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
		BinaryStdOut._clear_buffer()
		BinaryStdOut.out.flush()
	@staticmethod
	def close():
		BinaryStdOut.flush()
		BinaryStdOut.out.close()
		BinaryStdOut.is_init = False
	@staticmethod
	def write_bool(x):
		BinaryStdOut._write_bit(x)
	@staticmethod
	def write_byte(x):
		BinaryStdOut._write_byte(x & 0xff)
	@staticmethod
	def write_int(x, r=32):
		if(r == 32):
			BinaryStdOut._write_byte(((x >> 24)& 0xff))
			BinaryStdOut._write_byte(((x >> 16)& 0xff))
			BinaryStdOut._write_byte(((x >> 8)& 0xff))
			BinaryStdOut._write_byte(((x >> 0)& 0xff))
			return
		if(r < 1 or r > 16):
			raise ValueError("Illegal value for r = {}".format(r))
		if(x < 0 or x >= (1 << r)):
			raise ValueError("Illegal {}-bit char = {}".format(r,x))
		for i in range(0,r):
			bit = ((x >> (r - i - 1)) & 1) == 1
			BinaryStdOut._write_bit(bit)
	@staticmethod
	def write_char(x, r=8):
		if(r==8):
			if(ord(x)<0 or ord(x)>=256):
				raise ValueError("Illegal 8-bit char = {}".format(x))
			BinaryStdOut._write_byte(ord(x))
			return
		if(r < 1 or r > 16):
			raise ValueError("Illegal value for r = {}".format(r))
		if(ord(x) >= (1 << r)):
			raise ValueError("Illegal {}-bit char = {}".format(r,x))
		for i in range(0,r):
			bit = ((x >> (r - i - 1)) & 1) == 1
			BinaryStdOut._write_bit(bit)

	def write_string(s, r=8):
		for i in s:
			BinaryStdOut.write_char(i,r)
def main():
	for i in sys.argv[1]:
		BinaryStdOut.write_char(i)
	BinaryStdOut.close()
if __name__ == '__main__':
	main()
