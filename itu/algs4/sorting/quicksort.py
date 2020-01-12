# Created for BADS 2018
# see README.md for details
# Python 3

"""
The quicksort module provides methods for sorting an array and selecting
the ith smallest element in an array using quicksort.

For additional documentation, see Section 2.3 of Algorithms, 4th Edition
by Robert Sedgewick and Kevin Wayne.

:original author: Robert Sedgewick and Kevin Wayne
:original java code: https://algs4.cs.princeton.edu/23quicksort/Quick.java.html
"""

import sys

from itu.algs4.stdlib import stdio, stdrandom


def sort(array):
    """
    Rearranges the array in ascending order, using the natural order
    """
    stdrandom.shuffle(array)
    _sort(array, 0, len(array) - 1)

# quicksort the subarray from array[lo] to array[hi]
def _sort(array, lo, hi):
    if hi <= lo:
        return
    j = _partition(array, lo, hi)
    _sort(array, lo, j-1)
    _sort(array, j+1, hi)

# partition the subarray array[lo..hi] so that
# array[lo..j-1] <= array[j] <= array[j+1..hi]
# and return the index j
def _partition(array, lo, hi):
    i = lo
    j = hi + 1
    v = array[lo]
    while True:

        while array[i+1] < v:
            i += 1
            if i == hi:
                break
        i += 1

        # find item on hi to swap
        while v < array[j-1]:
            j -= 1
            if j == lo:
                break
        j -= 1

        # check if pointers cross
        if i >= j:
            break

        _exch(array, i, j)

    # put partitioning item v at a[j]
    _exch(array, lo, j)

    # now array[lo .. j-1] <= a[j] <= a[j+1 .. hi]
    return j

def select(array, k):
    """
    Rearranges the array so that array[k] contains the kth smalles key;
    array[0] through array[k-1] are less than (or equal to) array[k];
    and array[k+1] through array[n-1] are greather than (or equal to)
    array[k]

    :param array: the array
    :param k: the rank of the key
    :return: the key of rank k
    """
    stdrandom.shuffle(array)
    lo = 0
    hi = len(array) - 1
    while hi > lo:
        i = _partition(array, lo, hi)
        if i > k:
            hi = i - 1
        elif i < k:
            lo = i + 1
        else:
            return array[i]
    return array[lo]

# exchange array[i] and array[j]
def _exch(array, i, j):
    swap = array[i]
    array[i] = array[j]
    array[j] = swap


###########################################################
##### Check if array is sorted - useful for debugging #####
###########################################################

def is_sorted(array):
    return _is_sorted(array, 0, len(array) - 1)

def _is_sorted(array, lo, hi):
    for i in range(lo + 1, hi + 1):
        if array[i] < array[i-1]:
            return False
    return True

# print array to standard output
def show(array):
    stdio.write(" ".join(array))


if __name__ == "__main__":
    array = stdio.readAllStrings()
    sort(array)
    assert is_sorted(array)
    show(array)

    # shuffle
    stdrandom.shuffle(array)

    # display results again using select
    print()
    for i in range(0, len(array)):
        ith = str(select(array, i))
        stdio.writeln(ith)
