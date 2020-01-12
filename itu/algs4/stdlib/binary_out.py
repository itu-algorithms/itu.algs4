# Created for BADS 2018
# See README.md for details
# This is python3
import struct
import sys


"""
Binary output. This class provides methods for converting
some primitive type variables (boolean, byte, char, and int)
to sequences of bits and writing them
to an output stream.
The output stream can be standard output or another outputstream.
Uses big-endian (most-significant byte first).

The client must flush() the output stream when finished writing bits.

The client should not intermix calls to BinaryOut with calls to stdout;
otherwise unexpected behavior will result.
"""
class BinaryOut:
	def __init__(self, os=sys.stdout):
		"""
		Initializes a binary output stream from a
		specified output stream. Defaults to stdin.

		:param os: the output streamt to write to.
		"""
		self.out = os.buffer
		self.buffer = 0 #8-bit buffer of bits to write out
		self.n = 0 #number of bits used in buffer

	def _writeBit(self, x):
		self.buffer <<= 1
		if(x):
			self.buffer |=1
		self.n += 1
		if(self.n == 8):
			self._clearBuffer()

	def _writeByte(self, x):
		assert x >= 0 and x < 256
		#optimized if byte-alligned
		if(self.n == 0):
			self.out.write(struct.pack('B',x))
			return
		#otherwise write one bit at a time
		for i in range(0,8):
			bit = ((x >> (8 - i - 1)) & 1) == 1
			self._writeBit(bit)

	def _clearBuffer(self):
		if(self.n == 0):
			return
		if(self.n > 0):
			self.buffer <<= (8-self.n)
		self.out.write(self.buffer.to_bytes(1,'big'))
		self.n = 0
		self.buffer = 0

	def flush(self):
		self._clearBuffer()
		self.out.flush()

	def close(self):
		self.flush()
		self.out.close()

	def write_bool(self,x):
		self._writeBit(x)

	def write_byte(self,x):
		self._writeByte(x & 0xff)

	def write_int(self,x):
		self._writeByte(((x >> 24)& 0xff))
		self._writeByte(((x >> 16)& 0xff))
		self._writeByte(((x >> 8)& 0xff))
		self._writeByte(((x >> 0)& 0xff))

	def write_char(self, x):
		if(ord(x)<0 or ord(x)>=256):
			raise ValueError("Illegal 8-bit char = {}".format(x))
		self._writeByte(ord(x))

	def write_string(self, s):
		for i in s:
			self.write_char(s[i])
def main():
	out = BinaryOut()
	for i in sys.argv[1]:
		out.write_char(i)
	out.close()
if __name__ == '__main__':
	main()
