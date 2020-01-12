import sys
from typing import Generic, List, TypeVar

from itu.algs4.stdlib import stdio

T = TypeVar('T')

# Created for BADS 2018
# See README.md for details
# This is python3

"""
The binary_search module provides a method for binary
searching for an item in a sorted array.
The index_of operation takes logarithmic time in the worst case.
"""


def index_of(a: List[T], key: T):
    """
    Returns the index of the specified key in the specified array.
    :param a: the array of items, must be sorted in ascending order
    :param key: the search key
    :return: index of key in array if present -1 otherwise
    """
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


def main():
    """
    Reads strings from first input file and sorts them
    Reads strings from second input file and prints every string not in first input file
    """
    if len(sys.argv) == 3:
        sys.stdin = open(sys.argv[1])
        arr = stdio.readAllStrings()
        arr.sort()
        sys.stdin = open(sys.argv[2])
        while not stdio.isEmpty():
            key = stdio.readString()
            if index_of(arr, key) == -1:
                print(key)


if __name__ == '__main__':
    main()
