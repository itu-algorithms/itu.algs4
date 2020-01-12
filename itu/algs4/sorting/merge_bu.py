# Created for BADS 2018
# See README.md for details
# Python 3

"""
This module provides functions for sorting an array using bottom-up mergesort.


For additional documentation, see Section 2.1 of Algorithms, 4th Edition 
by Robert Sedgewick and Kevin Wayne.
"""
#  Sorts a sequence of strings from standard input using mergesort

def _is_sorted(a, lo=0, hi=None):
    # If hi is not specified, use whole array
    if hi is None:
        hi = len(a)
        
    # check if sublist is sorted
    for i in range(lo+1, hi):
        if a[i] < a[i-1]:
            return False
    return True

# stably merge a[lo .. mid] with a[mid+1 ..hi] using aux[lo .. hi]
def _merge(a, aux, lo, mid, hi):
    # copy to aux[]
    for k in range(lo, hi+1):
        aux[k] = a[k]
        
    # merge back to a[]
    i, j = lo, mid+1
    for k in range(lo, hi+1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1

def sort(a):
    """
    Rearranges the array in ascending order, using the natural order.
    
    :param a: the array to be sorted
    """
    n = len(a)
    aux = [None]*n
    
    length = 1
    while length < n:
        lo = 0
        while lo < n-length:
            mid = lo+length-1
            hi = min(mid+length, n-1)
            _merge(a, aux, lo, mid, hi)
            lo += 2*length
        length *= 2
    
    assert _is_sorted(a)
    

import sys

from itu.algs4.stdlib import stdio

# Reads in a sequence of strings from standard input or a file 
# supplied as argument to the program; mergesorts them; 
# and prints them to standard output in ascending order.
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
