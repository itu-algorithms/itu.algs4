import sys

from itu.algs4.stdlib import stdio

# Created for BADS 2018
# see README.md for details
# Python 3

"""
The selection module provides a function for sorting an
array using selection sort.
"""


def sort(a):
    """
    Rearranges the array in ascending order, using the natural order.
    :param a: the array to be sorted
    """
    _n = len(a)
    for i in range(_n):
        _min = i
        for j in range(i+1, _n):
            if a[j] < a[_min]:
                _min = j
        _exch(a, i, _min)


def _exch(a, i, j):
    """
    Exchanges the the items at index i and j.
    :param a: the array to be sorted
    :param i: the index for the first item
    :param j: the index for the second item
    """
    a[i], a[j] = a[j], a[i]


def _show(a):
    """
    Prints the content of the array.
    :param a: The array to be shown
    """
    for i in range(len(a)):
        print(a[i])


def main():
    """
    Reads strings from stdin, sorts them, and prints the result to stdout.
    """
    a = stdio.readAllStrings()
    sort(a)
    _show(a)


if __name__ == '__main__':
    main()
