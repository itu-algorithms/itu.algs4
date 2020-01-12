# Created for BADS 2018
# See README.md for details
# This is python3 
"""
The LSW module provides static methods for compressing and
expanding a binary input using LZW over the 8-bit extended
ASCII alphabet with 12-bit codewords.

For additional documentation see Section 5.5 of
Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
"""
import sys

from itu.algs4.stdlib.binary_stdin import BinaryStdIn
from itu.algs4.stdlib.binary_stdout import BinaryStdOut
from itu.algs4.strings.tst import TST

_R = 256
_L = 4096
_W = 12
def compress():
	"""
	Reads a sequence of 8-bit bytes from standard input; compresses
	them using LZW compression with 12-bit codewords; and writes the results
	to standard output.
	"""
	input_ = BinaryStdIn.read_string()
	st = TST()
	for i in range(0,_R):
		st.put(""+chr(i),i)
	code = _R+1
	while(len(input_) > 0):
		s = st.longest_prefix_of(input_)
		BinaryStdOut.write_int(st.get(s),_W)
		t = len(s)
		if(t < len(input_) and code < _L):
			st.put(input_[0:t+1],code)
			code += 1
		input_ = input_[t:]
	BinaryStdOut.write_int(_R,_W)
	BinaryStdOut.close()
	
def expand():
	"""
	Reads a sequence of bit encoded using LZW compression with
	12-bit codewords from standard input; expands them; and writes
	the results to standard output.
	"""
	st = ["" for i in range(0,_L)]
	i = 0
	while(i < _R):
		st[i] = ""+chr(i)
		i += 1
	st[i] = ""
	i += 1

	codeword = BinaryStdIn.read_int(_W)
	if(codeword == _R):
		return
	val = st[codeword]
	while(True):
		BinaryStdOut.write_string(val)
		codeword = BinaryStdIn.read_int(_W)
		if(codeword == _R):
			break
		s = st[codeword]
		if(i == codeword):
			s = val + val[0]
		if(i < _L):
			st[i] = val+s[0]
			i+=1
		val = s
	BinaryStdOut.close()
	
def main():
	"""
	Sample client that calls compress() if the command-line
	argument is "-", and expand() if it is "+".

        Example: echo huhu | python3 algs4/strings/lzw.py - | python3 algs4/strings/lzw.py +
	"""
	if(sys.argv[1] == '-'):
		compress()
	elif(sys.argv[1] == '+'):
		expand()
	else:
		raise ValueError("Illegal command line argument")
	
if __name__ == '__main__':
	main()
