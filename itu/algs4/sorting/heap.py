# Created for BADS 2018
# See README.md for details
# Python 3

import sys

from itu.algs4.stdlib import stdio


"""
The heap module provides a function for heapsorting an array.
"""


def sort(pq):
    """
    Rearranges the array in ascending order, using the natural order.
    :param pq: the array to be sorted
    """
    n = len(pq)
    for k in range(n//2, 0, -1):
        _sink(pq, k, n)
    while n > 1:
        _exch(pq, 1, n)
        n -= 1
        _sink(pq, 1, n)


def _sink(pq, k, n):
    """
    Moves item at index k down to a legal position on the heap.
    :param k: Index of the item to be moved
    :param n: Amount of items left on the heap
    """
    while 2*k <= n:
        j = 2*k
        if j < n and _less(pq, j, j+1):
            j += 1
        if not _less(pq, k, j):
            break
        _exch(pq, k, j)
        k = j


def _less(pq, i, j):
    """
    Check if item at index i is greater than item at index j on the heap.
    Indices are "off-by-one" to support 1-based indexing
    :param pq: the heap
    :param i: index of the first item
    :param j: index of the second item
    :return: True if item at index i is smaller than item at index j otherwise False
    """
    return pq[i - 1] < pq[j - 1]


def _exch(pq, i, j):
    """
    Exchanges the positions of items at index i and j on the heap.
    Indices are "off-by-one" to support 1-based indexing.
    :param pq: the heap
    :param i: index of the first item
    :param j: index of the second item
    """
    pq[i-1], pq[j-1] = pq[j-1], pq[i-1]


def _show(pq):
    """
    Print the contents of the array
    :param pq: the array to be printed
    """
    for i in range(len(pq)):
        print(pq[i])


def main():
    """
    Reads in a sequence of strings from stdin
    heapsorts them, and prints the result in ascending order.
    """
    a = stdio.readAllStrings()
    sort(a)
    _show(a)


if __name__ == '__main__':
    main()
