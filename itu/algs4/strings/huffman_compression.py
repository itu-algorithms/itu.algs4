# Created for BADS 2018
# See README.md for details
# This is python3 
"""
The Huffman compression module provides static methods for compressing
and expanding a binary input using Huffman codes over the 8-bit extended
ASCII alphabet

For additional documentation, see Section 5.5 of Algorithms, 4th edtition
by Robert Sedgewick and Kevin Wayne.
"""
import sys

from itu.algs4.sorting.min_pq import MinPQ
from itu.algs4.stdlib.binary_stdin import BinaryStdIn
from itu.algs4.stdlib.binary_stdout import BinaryStdOut

_R = 256
class _Node:
	def __init__(self, ch, freq, left, right):
		self.ch = ch
		self.freq = freq
		self.left = left
		self.right = right
	def is_leaf(self):
		left = self.left
		right = self.right
		assert(left is None and right is None or left is not None and right is not None)
		return left is None and right is None
	def __gt__(self, that):
		return self.freq > that.freq
def compress():
	"""
	Reads a sequence of 8-bit bytes from standard input; compresses them
	using Huffman codes with an 8-bit alphabet; and writes the results
	to standard input.
	"""
	s = BinaryStdIn.read_string()
	#Tabulate frequency counts
	freq = [0 for i in range(0,_R)]
	for i in range(0,len(s)):
		freq[ord(s[i])] += 1
	#Build Huffman trie
	root = _build_trie(freq)
	#Build code table
	st = [None for i in range(0,_R)]
	_build_code(st, root, "")
	#Print trie for decoder
	_write_trie(root)
	#Print number of bytes in original uncompressed message
	BinaryStdOut.write_int(len(s))
	#Use Huffman code to encode input
	for i in range (0,len(s)):
		code = st[ord(s[i])]
		for j in range(0,len(code)):
			if(code[j]=='0'):
				BinaryStdOut.write_bool(False)
			elif(code[j]=='1'):
				BinaryStdOut.write_bool(True)
			else:
				raise ValueError("Illegal state")
	BinaryStdOut.close()
	
#Build the Huffman trie given frequencies
def _build_trie(freq):
	pq = MinPQ()
	for i in range(0,_R):
		if(freq[i] > 0):
			pq.insert(_Node(chr(i), freq[i], None, None))
	if(pq.size() == 0):
		raise ValueError("The provided file is empty")
	if(pq.size() == 1):
		if(freq[ord('\0')]==0):
			pq.insert(_Node('\0', 0, None, None))
		else:
			pq.insert(_Node('\1', 0, None, None))
	while(pq.size() > 1):
		left = pq.del_min()
		right = pq.del_min()
		parent = _Node('\0', left.freq + right.freq, left, right)
		pq.insert(parent)
	return pq.del_min()

#Write bitstring-encoded trie to standard output
def _write_trie(x):
	if(x.is_leaf()):
		BinaryStdOut.write_bool(True)
		BinaryStdOut.write_char(x.ch)
		return
	BinaryStdOut.write_bool(False)
	_write_trie(x.left)
	_write_trie(x.right)
	
#Make a lookup table from symbols and their encodings
def _build_code(st, x, s):
	if(not x.is_leaf()):
		_build_code(st, x.left, s+'0')
		_build_code(st, x.right, s+'1')
	else:
		st[ord(x.ch)] = s
		

def expand():
	"""
	Reads a sequence of bits that represents a Huffman-compressed message from
	standard input; expands them; and writes the results to standard output.
	"""
	BinaryStdIn.is_empty()
	root = _read_trie()
	length = BinaryStdIn.read_int()
	for i in range(0,length):
		x = root
		while(not x.is_leaf()):
			bit = BinaryStdIn.read_bool()
			if(bit):
				x = x.right
			else:
				x = x.left
		BinaryStdOut.write_char(x.ch)
	BinaryStdOut.close()
	
def _read_trie():
	isLeaf = BinaryStdIn.read_bool()
	if(isLeaf):
		return _Node(BinaryStdIn.read_char(), -1, None, None)
	else:
		return _Node('\0', -1, _read_trie(), _read_trie())
	
def main():
	"""
	Sample client that calss compress() if the command-line
	argument is "-", and expand() if it is "+".
	"""
	if(sys.argv[1] == '-'):
		compress()
	elif(sys.argv[1] == '+'):
		expand()
	else:
		raise ValueError("Illegal command line argument")
	
if __name__ == '__main__':
	main()
