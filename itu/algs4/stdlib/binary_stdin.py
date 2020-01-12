# Created for BADS 2018
# See README.md for details
# This is python3
import struct
import sys

from itu.algs4.stdlib.binary_stdout import BinaryStdOut


"""
Binary standard input. This class provides methods for reading
in bits from standard input, either one bit at a time (as a boolean),
8 bits at a time (as a char) or 32 bits at a time (as an int)

All primitive types are assumed to be represented in big-endian order.

The client should not mix class to BinaryStdIn with calls to stdin,
otherwise unexpected behavior will result.
"""
class BinaryStdIn:
	EOF = -1
	ins = sys.stdin.buffer
	n = 0
	buffer_ = 0
	is_init = False
	@staticmethod
	def _initialize():
		BinaryStdIn.buffer_ = 0
		BinaryStdIn.n = 0
		BinaryStdIn._fill_buffer()
		BinaryStdIn.is_init = True
	@staticmethod
	def _fill_buffer():
		x = BinaryStdIn.ins.read(1)
		if(x == b''):
			BinaryStdIn.buffer_ = BinaryStdIn.EOF
			BinaryStdIn.n = -1
			return
		BinaryStdIn.buffer_ = struct.unpack('B',x)[0]
		BinaryStdIn.n = 8
	@staticmethod
	def close():
		"""
		Close this input stream and release any associated system resources
		"""
		if(not BinaryStdIn.is_init):
			_initialize
		BinaryStdIn.ins.close()
		BinaryStdIn.is_init = False
	@staticmethod
	def is_empty():
		if(not BinaryStdIn.is_init):
			BinaryStdIn._initialize()
		return BinaryStdIn.buffer_ == BinaryStdIn.EOF
	@staticmethod
	def read_bool():
		if(BinaryStdIn.is_empty()):
			raise EOFError("Reading from empty input stream")
		BinaryStdIn.n -= 1
		bit = ((BinaryStdIn.buffer_ >> BinaryStdIn.n) & 1) == 1
		if(BinaryStdIn.n == 0):
			BinaryStdIn._fill_buffer()
		return bit
	@staticmethod
	def read_char():
		if(BinaryStdIn.is_empty()):
			raise EOFError("Reading from empty input stream")
		if(BinaryStdIn.n==8):
			x = BinaryStdIn.buffer_
			BinaryStdIn._fill_buffer()
			return chr(x & 0xff)
		x = BinaryStdIn.buffer_
		x <<= (8-BinaryStdIn.n)
		oldN = BinaryStdIn.n
		if(BinaryStdIn.is_empty()):
			raise EOFError("Reading from empty input stream")
		BinaryStdIn._fill_buffer()
		BinaryStdIn.n = oldN
		x |= (BinaryStdIn.buffer_>> BinaryStdIn.n)
		return chr(x & 0xff)
	@staticmethod
	def read_string():
		if(BinaryStdIn.is_empty()):
			raise EOFError("Reading from empty input stream")
		sb = ""
		while(not BinaryStdIn.is_empty()):
			sb += BinaryStdIn.read_char()
		return sb

	@staticmethod
	def read_int(r=32):
		if(r==32):
			x = 0
			for i in range(0,4):
				c = BinaryStdIn.read_char()
				x <<=8
				x |= ord(c)
			return x
		if(r<1 or r>32):
			raise ValueError("Illegal value for r = {}".format(r))
		x = 0
		for i in range(0,r):
			x <<= 1
			bit = BinaryStdIn.read_bool()
			if(bit):
				x |= 1
		return x

def main():
	while(not BinaryStdIn.is_empty()):
		BinaryStdOut.write_char(BinaryStdIn.read_char())
if __name__ == '__main__':
	main()
