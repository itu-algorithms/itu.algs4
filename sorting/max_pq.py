import sys
from stdlib import stdio

# Created for BADS 2018
# see README.md for details
# Python 3

"""
The MaxPQ class represents a priority queue of generic keys.
It supports the usual insert and delete-the-maximum
operations, along with methods for peeking at the maximum key,
testing if the priority queue is empty, and iterating through the keys.
This implementation uses a binary heap.
The insert and delete-the-maximum operations take logarithmic amortized time.
The max, size and is_empty operations take constant time.
Construction takes time proportional to the specified capacity.
"""


class MaxPQ:
    def __init__(self, _max=1):
        self._pq = [None] * (_max + 1)
        self._n = 0

    def insert(self, x):
        if self._n is len(self._pq) - 1:
            self._resize(2 * len(self._pq))
        self._n += 1
        self._pq[self._n] = x
        self._swim(self._n)

    def max(self):
        return self._pq[1]

    def del_max(self):
        _max = self._pq[1]
        self._exch(1, self._n)
        self._n -= 1
        self._sink(1)
        self._pq[self._n + 1] = None
        if self._n > 0 and self._n is (len(self._pq) - 1) // 4:
            self._resize(len(self._pq) // 2)
        return _max

    def is_empty(self):
        return self._n == 0

    def size(self):
        return self._n

    def _sink(self, k):
        while 2*k <= self._n:
            j = 2*k
            if j < self._n and self._less(j, j+1):
                j += 1
            if not self._less(k, j):
                break
            self._exch(k, j)
            k = j

    def _swim(self, k):
        while k > 1 and self._less(k//2, k):
            self._exch(k, k//2)
            k = k//2

    def _resize(self, capacity):
        temp = [None] * capacity
        for i in range(1, self._n + 1):
            temp[i] = self._pq[i]
        self._pq = temp

    def _less(self, i, j):
        return self._pq[i] < self._pq[j]

    def _exch(self, i, j):
        self._pq[i], self._pq[j] = self._pq[j], self._pq[i]

    def __iter__(self):
        for i in range(1, self._n + 1):
            yield self._pq[i]


if __name__ == '__main__':
    pq = MaxPQ()

    if len(sys.argv) > 1:
        sys.stdin = open(sys.argv[1])
        while not stdio.isEmpty():
            item = stdio.readString()
            if item is not '-':
                pq.insert(item)
            elif not pq.is_empty():
                print(pq.del_max())
        print("({} left on pq)".format(pq.size()))
        sys.stdin.close()
