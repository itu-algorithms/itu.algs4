# Created for BADS 2018
# See README.md for details
# This is python3
import sys
import struct
from binaryout import BinaryOut
"""
Binary standard input. This module provides methods for reading
in bits from standard input, either one bit at a time (as a boolean),
8 bits at a time (as a char) or 32 bits at a time (as an int)

All primitive types are assumed to be represented in big-endian order.

The client should not mix class to BinaryIn with calls to stdin,
otherwise unexpected behavior will result.
"""
class BinaryIn:
	EOF = -1
	ins = sys.stdin.buffer
	n = 0
	buffer_ = 0
	is_init = False
	@staticmethod
	def _initialize():
		BinaryIn.buffer_ = 0
		BinaryIn.n = 0
		BinaryIn._fillBuffer()
		BinaryIn.is_init = True
	@staticmethod
	def _fillBuffer():
		x = BinaryIn.ins.read(1)
		if(x == b''):
			BinaryIn.buffer_ = BinaryIn.EOF
			BinaryIn.n = -1
			return
		BinaryIn.buffer_ = struct.unpack('B',x)[0]
		BinaryIn.n = 8
	@staticmethod
	def close():
		"""
		Close this input stream and release any associated system resources
		"""
		if(not BinaryIn.is_init):
			_initialize
		BinaryIn.ins.close()
		BinaryIn.is_init = False
	@staticmethod
	def is_empty():
		if(not BinaryIn.is_init):
			BinaryIn._initialize()
		return BinaryIn.buffer_ == BinaryIn.EOF
	@staticmethod
	def read_bool():
		if(BinaryIn.is_empty()):
			raise EOFError("Reading from empty input stream")
		BinaryIn.n -= 1
		bit = ((BinaryIn.buffer_ >> BinaryIn.n) & 1) == 1
		if(BinaryIn.n == 0):
			BinaryIn._fillBuffer()
		return bit
	@staticmethod
	def read_char():
		if(BinaryIn.is_empty()):
			raise EOFError("Reading from empty input stream")
		if(BinaryIn.n==8):
			x = BinaryIn.buffer_
			BinaryIn._fillBuffer()
			return chr(x & 0xff)
		x = BinaryIn.buffer_
		x <<= (8-BinaryIn.n)
		oldN = BinaryIn.n
		if(BinaryIn.is_empty()):
			raise EOFError("Reading from empty input stream")
		BinaryIn._fillBuffer()
		BinaryIn.n = oldN
		x |= (BinaryIn.buffer_>> BinaryIn.n)
		return chr(x & 0xff)
	@staticmethod
	def read_string():
		if(BinaryIn.is_empty()):
			raise EOFError("Reading from empty input stream")
		sb = ""
		while(not BinaryIn.is_empty()):
			sb += BinaryIn.read_char()
		return sb

	@staticmethod
	def read_int():
		x = 0
		for i in range(0,4):
			c = BinaryIn.read_char()
			x <<=8
			x |= ord(c)
		return x

def main():
	out = BinaryOut()
	while(not BinaryIn.is_empty()):
		out.write_char(BinaryIn.read_char())
if __name__ == '__main__':
	main()