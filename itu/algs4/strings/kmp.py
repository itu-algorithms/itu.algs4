# Created for BADS 2018
# See README.md for details
# This is python3 
import sys


"""
The KMP (Knuth-Morris-Pratt) class finds the first occurrence 
of a pattern string in a text string.
This implementation uses a version of the Knuth-Morris-Pratt substring search
algorithm. The version takes time as space proportional to
N + M R in the worst case, where N is the length
of the text string, M is the length of the pattern, and R
is the alphabet size.
"""
class KMP:
	def __init__(self, pat):
		"""
    	Preprocesses the pattern string.
    	:param pat: the pattern string
    	"""
		self.pat = pat
		M = len(pat)
		R = 256
		self.dfa = [[0 for c in range(0,M)] for r in range(0,R)]
		self.dfa[ord(pat[0])][0] = 1
		X = 0
		for j in range (1,M):
			#Compute dfa[][j]
			for c in range(0,R):
				self.dfa[c][j] = self.dfa[c][X] #Copy mismatch cases
			self.dfa[ord(pat[j])][j] = j+1 #Set match case
			X = self.dfa[ord(pat[j])][X] #Update restart state
	def search(self, txt):
		"""
		Returns the index of the first occurrrence of the pattern string
     	in the text string.
     	:param txt: the text string
     	:return: the index of the first occurrence of the pattern string 
     	in the text string; N if no such match
		"""
		N = len(txt)
		M = len(self.pat)
		j = 0
		i = 0
		while(i < N and j < M):
			j = self.dfa[ord(txt[i])][j]
			i += 1
		if(j==M): #found (hit end of pattern)
			return i-M 
		else: #not found (hit end of text)
			return N
def main():
	"""
	Takes a pattern string and an input string as command-line arguments;
    searches for the pattern string in the text string; and prints
    the first occurrence of the pattern string in the text string.
    Will print the pattern after the end of the string if no match is found.
	"""
	pat = sys.argv[1]
	txt = sys.argv[2]
	kmp = KMP(pat)
	print("text:    {}".format(txt))
	offset = kmp.search(txt)
	print("pattern: ",end='')
	for i in range(0,offset):
		print("",end=' ')
	print(pat)
	
if __name__ == "__main__":
	main()
