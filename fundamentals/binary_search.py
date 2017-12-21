import sys
from stdlib import stdio
# Created for BADS 2018
# See README.md for details
# This is python3

"""
The binary_search module provides a method for binary
searching for an item in a sorted array.
The index_of operation takes logarithmic time in the worst case.
"""


def index_of(a, key):
    lo = 0
    hi = len(a) - 1
    while hi >= lo:
        mid = lo + (hi - lo)//2
        if a[mid] < key:
            lo = mid + 1
        elif a[mid] > key:
            hi = mid - 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    if len(sys.argv) is 3:
        sys.stdin = open(sys.argv[1])
        arr = stdio.readAllStrings()
        arr.sort()
        sys.stdin = open(sys.argv[2])
        while not stdio.isEmpty():
            key = stdio.readString()
            if index_of(arr, key) is -1:
                print(key)
