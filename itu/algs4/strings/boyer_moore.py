# Created for BADS 2018
# See README.md for details
# This is python3 
import sys


class BoyerMoore:
    """
    The BoyerMoore class finds the first occurence of a pattern string
    in a text string.
    This implementation uses the Boyer-Moore algorithm (with the bad-character
    rule, but not the strong good suffix rule).
    """
    
    def __init__(self, pat):
        """
        Preprocesses the pattern string.
        :param pat: the pattern string
        """
        self.pat = pat
        M = len(pat)
        R = 256
        self.right = [-1 for i in range(0,R)] #-1 for chars not in pattern
        for j in range(0,M):
            self.right[ord(pat[j])] = j
            
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
        skip = 0
        i = 0
        #for i in range(0,N-M+1,skip):
        while(i <= N-M):
            skip = 0
            for j in range(M-1,-1,-1):
                if not(self.pat[j] == txt[i+j]):
                    skip = j-self.right[ord(txt[i+j])]
                    if(skip < 1):
                        skip = 1
                    break
            if(skip == 0):
                return i
            i += skip
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
    bm = BoyerMoore(pat)
    print("text:    {}".format(txt))
    offset = bm.search(txt)
    print("pattern:",end=" ")
    for i in range(0,offset):
        print("", end=" ")
    print(pat)
    
if __name__ == "__main__":
    main()
