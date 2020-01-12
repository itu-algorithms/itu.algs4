# Created for BADS 2018
# See README.md for details
# Python 3

"""
This module provides functions for sorting arrays of strings using msd sort.

For additional documentation, see Section 5.1 of Algorithms, 4th Edition 
by Robert Sedgewick and Kevin Wayne.
"""

cutoff = 15

# compare characters at position d
def _less(a, b, d):
    return a[d] < b[d]

# insertion sort a[lo..hi], starting at dth character
def _insertion(a, lo, hi, d):
    for i in range(lo, hi+1):
        j = i
        while j>lo and _less(a[j], a[j-1], d):
            a[j], a[j-1] = a[j-1], a[j]
            j -= 1

# sort from a[lo] to a[hi], starting at the dth character
def _sort(a, lo, hi, d, aux, radix):
    global cutoff
    
    if hi <= lo+cutoff:
        _insertion(a, lo, hi, d)
        return
    
    # compute frequency counts
    count = [0]*(radix+2)
    for i in range(hi+1):
        ch = ord(a[i][d]) # get number representation of character
        count[ch + 2] += 1

    # compute cumulates
    for r in range(radix+1):
        count[r+1] += count[r]

    # move data
    for i in range(hi+1):
        ch = ord(a[i][d])
        aux[count[ch+1]] = a[i]
        count[ch+1] += 1

    # copy back
    for i in range(hi+1):
        a[i] = aux[i-lo]
    
    # recursively sort for each character (excludes sentinel -1)
    for r in range(radix):
        _sort(a, lo + count[r], lo + count[r+1] - 1, d+1, aux, radix)

def sort(a, radix=256):
    """
    Rearranges the array of 32-bit integers in ascending order.
    Currently assumes that the integers are nonnegative.
    
    :param a: the array to be sorted
    """
    n = len(a)
    aux = [None]*n
    _sort(a, 0, n-1, 0, aux, radix)
        

import sys

from itu.algs4.stdlib import stdio

if __name__ == '__main__':
    if len(sys.argv) > 1:
        try: 
            sys.stdin = open(sys.argv[1])
        except IOError:
            print("File not found, using standard input instead")
    
    a = stdio.readAllStrings()
    sort(a)
    for elem in a:
        print(elem)    
