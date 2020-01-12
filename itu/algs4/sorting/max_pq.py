# Created for BADS 2018
# see README.md for details
# Python 3

import sys
from typing import Generic, Iterator, List, Optional, TypeVar

from itu.algs4.errors.errors import NoSuchElementException
from itu.algs4.stdlib import stdio

Key = TypeVar('Key')

class MaxPQ(Generic[Key]):
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
    def __init__(self, _max: int = 1):
        """
        Initializes an empty priority queue with the given initial capacity
        :param _max: the initial capacity, default value is 1
        """
        self._pq: List[Optional[Key]] = [None] * (_max + 1)
        self._n = 0

    def insert(self, x: Key) -> None:
        """
        Adds a new key to this priority queue.
        :param x: the new key to add to this priority queue
        """
        if self._n == len(self._pq) - 1:
            self._resize(2 * len(self._pq))
        self._n += 1
        self._pq[self._n] = x
        self._swim(self._n)

    def max(self) -> Key:
        """
        Returns a largest key on this priority queue.
        :return: a largest key on the priority queue
        :raises NoSuchElementException: if this priority queue is empty
        """
        if self.is_empty():
            raise NoSuchElementException("Priority queue underflow")

        assert self._pq[1] is not None
        return self._pq[1]

    def del_max(self) -> Key:
        """
        Removes and returns a largest key on this priority queue.
        :return: a largest key on this priority queue
        :raises NoSuchElementException: if this priority queue is empty
        """
        if self.is_empty():
            raise NoSuchElementException("Priority queue underflow")

        _max = self._pq[1]
        assert _max is not None
        self._exch(1, self._n)
        self._n -= 1
        self._sink(1)
        self._pq[self._n + 1] = None
        if self._n > 0 and self._n == (len(self._pq) - 1) // 4:
            self._resize(len(self._pq) // 2)
        return _max

    def is_empty(self) -> bool:
        """
        Returns True if this priority queue is empty.
        :return: True if this priority queue is empty otherwise False
        :rtype: bool
        """
        return self._n == 0

    def size(self) -> int:
        """
        Returns the number of keys on this priority queue.
        :return: the number of keys on this priority queue
        :rtype: int
        """
        return self._n

    def __len__(self) -> int:
        return self.size()

    def _sink(self, k) -> None:
        """
        Moves item at index k down to a legal position on the heap.
        :param k: Index of the item to be moved
        """
        while 2*k <= self._n:
            j = 2*k
            if j < self._n and self._less(j, j+1):
                j += 1
            if not self._less(k, j):
                break
            self._exch(k, j)
            k = j

    def _swim(self, k: int) -> None:
        """
        Moves item at index k up to a legal position on the heap.
        :param k: Index of the item to be moved
        """
        while k > 1 and self._less(k//2, k):
            self._exch(k, k//2)
            k = k//2

    def _resize(self, capacity: int):
        """
        Copies the contents of the heap to a new array of size capacity.
        :param capacity: The capacity of the new array
        """
        temp: List[Optional[Key]] = [None] * capacity
        for i in range(1, self._n + 1):
            temp[i] = self._pq[i]
        self._pq = temp

    def _less(self, i: int, j: int):
        """
        Check if item at index i is less than item at index j on the heap.
        :param i: index of the first item
        :param j: index of the second item
        :return: True if item at index i is smaller than item at index j otherwise False
        """
        return self._pq[i] < self._pq[j]

    def _exch(self, i: int, j: int):
        """
        Exchanges the position of items at index i and j on the heap.
        :param i: index of the first item
        :param j: index of the second item
        """
        self._pq[i], self._pq[j] = self._pq[j], self._pq[i]

    def __iter__(self) -> Iterator[Key]:
        """
        Iterates over all the items in this priority queue in heap order.
        """
        copy: MaxPQ[Key] = MaxPQ(self.size())
        for i in range(1, self._n + 1):
            key = self._pq[i]
            assert key is not None
            copy.insert(key)
        for i in range(1, copy._n + 1):
            yield copy.del_max()


def main():
    """
    Reads strings from stdin and adds them to a priority queue.
    When reading a '-' it removes a maximum item on the priority queue and prints it to stdout.
    Prints the amount of items left on the priority queue
    """
    pq = MaxPQ()
    while not stdio.isEmpty():
        item = stdio.readString()
        if item != '-':
            pq.insert(item)
        elif not pq.is_empty():
            print(pq.del_max())
    print("({} left on pq)".format(pq.size()))


if __name__ == '__main__':
    main()
