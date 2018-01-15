# Created for BADS 2018
# See README.md for details
# This is python3 
import sys
from tst import TST
from stdlib.binary_stdin import BinaryStdIn
from stdlib.binary_stdout import BinaryStdOut
"""
The LSW module provides static methods for compressing and
expanding a binary input using LZW over the 8-bit extended
ASCII alphabet with 12-bit codewords.

For additional documentation see Section 5.5 of
Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
"""
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
	if(sys.argv[1] == '-'):
		compress()
	elif(sys.argv[1] == '+'):
		expand()
	else:
		raise ValueError("Illegal command line argument")
if __name__ == '__main__':
	main()