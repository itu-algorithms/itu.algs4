# Created for BADS 2018
# See README.md for details
# Python 3

"""
This module provides functions for sorting arrays of strings using lsd sort.

For additional documentation, see Section 5.1 of Algorithms, 4th Edition 
by Robert Sedgewick and Kevin Wayne.
"""

def sort(a, w, radix=256):
    """
     Rearranges the array of w-character strings in ascending order.
     
     :param a: the array to be sorted
     :param w: the number of characters per string
     :param radix: an optional number specifying the size of the alphabet to sort
    """
    
    n = len(a)
    aux = [None]*n
    
    for d in range (w-1, -1, -1): # from w-i to 0
        # sort by key-indexed counting on dth character
        
        # compute frequency counts
        count = [0]*(radix+1)
        for i in range(n):
            ch = ord(a[i][d]) # get number representation of character
            count[ch + 1] += 1
    
        # compute cumulates
        for r in range(radix):
            count[r+1] += count[r]
    
        # move data
        for i in range(n):
            ch = ord(a[i][d])
            aux[count[ch]] = a[i]
            count[ch] += 1
    
        # copy back
        for i in range(n):
            a[i] = aux[i]

import sys

from itu.algs4.stdlib import stdio

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try: 
            sys.stdin = open(sys.argv[1])
        except IOError:
            print("File not found, using standard input instead")
    
    a = stdio.readAllStrings()
    sort(a, 3)
    for elem in a:
        print(elem)    
