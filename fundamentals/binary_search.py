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
    arr = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25]
    for i in range(1, 25):
        if index_of(arr, i) is -1:
            print(i)
