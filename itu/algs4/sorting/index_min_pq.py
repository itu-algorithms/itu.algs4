# Created for BADS 2018
# See README.md for details
# Python 3

from itu.algs4.errors.errors import IllegalArgumentException, NoSuchElementException


class IndexMinPQ:
    """
    The IndexMinPQ class represents an indexed priority queue of generic keys.
    It supports the usual insert and delete-the-minimum
    operations, along with delete and change-the-key
    methods. In order to let the client refer to the keys on the priority queue,
    an integer between 0 and maxN - 1
    is associated with each key-the client uses this integer to specify
    which key to delete or change.
    It also supports methods for peeking at the minimum key,
    testing if the priority queue is empty, and iterating through
    the keys.
    This implementation uses a binary heap along with an array to associate
    keys with integers, in the given range.
    The insert, delete-the-minimum, delete, change-key, decrease-key, and increase-key
    operations take logarithmic time.
    The is-empty, size, min-index, min-key, and key-of operations take constant time.
    Construction takes time proportional to the specified capacity.
    """
    def __init__(self, max_n):
        """
        Initializes an empty indexed priority queue with indices between 0
        and max_n - 1.
        :param max_n: the keys on this priority queue are indices from 0 to max_n - 1
        :raises IllegalArgumentException: if max_n < 0
        """
        self.max_n = max_n
        self.n = 0
        self.keys = [None] * (max_n + 1)
        self.pq = [0] * (max_n + 1)
        self.qp = [-1] * (max_n + 1)

    def insert(self, i, key):
        """
        Associates key with index i
        :param i: an index
        :param key: the key to associate with index i
        :raises IllegalArgumentException: unless 0 <= i < max_n
        :raises IllegalArgumentException: if there already is an item associated with index i
        """
        if i < 0 or i >= self.max_n:
            raise IllegalArgumentException("index is not within range")
        if self.contains(i):
            raise IllegalArgumentException("index is already in the priority queue")
        self.n += 1
        self.qp[i] = self.n
        self.pq[self.n] = i
        self.keys[i] = key
        self._swim(self.n)

    def contains(self, i):
        """
        Is i an index on this priority queue?
        :param i: an index
        :return: True if i is an index on this priority queue False otherwise
        :rtype: bool
        :raises IllegalArgumentException: unless 0 <= i < max_n
        """
        if i < 0 or i >= self.max_n:
            raise IllegalArgumentException("index is not within range")
        return self.qp[i] != -1

    def change_key(self, i, key):
        """
        Change the key associated with index i to the specified value.
        :param i: the index of the key to change
        :param key: change the key associated with index i to this key
        :raises IllegalArgumentException: unless 0 <= i < max_n
        :raises NoSuchElementException: if no key is associated with index i
        """
        if i < 0 or i >= self.max_n:
            raise IllegalArgumentException("index is not within range")
        if not self.contains(i):
            raise NoSuchElementException("index is not in the priority queue")
        self.keys[i] = key
        self._swim(self.qp[i])
        self._sink(self.qp[i])

    def decrease_key(self, i, key):
        """
        Decrease the key associated with index i to the specified value.
        :param i: the index of the key to decrease
        :param key: decrease the key associated with index i to this key
        :raises IllegalArgumentException: unless 0 <= i < max_n
        :raises IllegalArgumentException: if key >= key_of(i)
        :raises NoSuchElementException: if no key is associated with index i
        """
        if i < 0 or i >= self.max_n:
            raise IllegalArgumentException("index is not within range")
        if not self.contains(i):
            raise IllegalArgumentException("index is not in the priority queue")
        if self.keys[i] <= key:
            raise IllegalArgumentException("calling decrease_key() with given argument would not strictly decrease the key")
        self.keys[i] = key
        self._swim(self.qp[i])

    def increase_key(self, i, key):
        """
        Increase the key associated with index i to the specified value.
        :param i: the index of the key to increase
        :param key: increase the key associated with index i to this key
        :raises IllegalArgumentException: unless 0 <= i < max_n
        :raises IllegalArgumentException: if key <= key_of(i)
        :raises NoSuchElementException: if no key is associated with index i
        """
        if i < 0 or i >= self.max_n:
            raise IllegalArgumentException("index is not within range")
        if not self.contains(i):
            raise NoSuchElementException("index is not in the priority queue")
        if self.keys[i] >= key:
            raise IllegalArgumentException("calling increase_key() with given argument would not strictly increase the key")
        self.keys[i] = key
        self._sink(self.qp[i])

    def delete(self, i):
        """
        Remove the key associated with index i
        :param i: the index of the key to remove
        :raises IllegalArgumentException: unless 0 <= i < max_n
        :raises NoSuchElementException: if no key is associated with index i
        """
        if i < 0 or i >= self.max_n:
            raise IllegalArgumentException("index is not in range")
        if not self.contains(i):
            raise NoSuchElementException("index is not in the priority queue")
        index = self.qp[i]
        self._exch(index, self.n)
        self.n -= 1
        self._sink(index)
        self.keys[i] = None
        self.qp[i] = -1

    def min_index(self):
        """
        Returns an index associated with a minimum key.
        :return: an index associated with a minimum key
        :rtype: int
        :raises NoSuchElementException: if this priority queue is empty
        """
        if self.n == 0:
            raise NoSuchElementException("Priority queue underflow")
        return self.pq[1]

    def min_key(self):
        """
        Returns a minimum key.
        :return: a minimum key
        :raises NoSuchElementException: if this priority queue is empty
        """
        if self.n == 0:
            raise NoSuchElementException("Priority queue underflow")
        return self.keys[self.pq[1]]

    def del_min(self):
        """
        Removes a minimum key and returns its associated index.
        :return: an index associated with a minimum key
        :raises NoSuchElementException: if this priority queue is empty
        :rtype: int
        """
        if self.n == 0:
            raise NoSuchElementException("Priority queue underflow")
        _min = self.pq[1]
        self._exch(1, self.n)
        self.n -= 1
        self._sink(1)
        self.qp[_min] = -1
        self.keys[_min] = None
        self.pq[self.n+1] = -1
        return _min

    def is_empty(self):
        """
        Returns True if this priority queue is empty.
        :return: True if this priority queue is empty False otherwise
        :rtype: bool
        """
        return self.n == 0

    def size(self):
        """
        Returns the number of keys on this priority queue.
        :return: the number of keys on this priority queue
        :rtype: int
        """
        return self.n

    def __len__(self):
        return self.size()

    def key_of(self, i):
        """
        Returns the key associated with index i.
        :param i: the index of the key to return
        :return: the key associated with index i
        :raises IllegalArgumentException: unless 0 <= i < max_n
        :raises NoSuchElementException: if no key is associated with index i
        """
        if i < 0 or i >= self.max_n:
            raise IllegalArgumentException("index is out of range")
        if not self.contains(i):
            raise IllegalArgumentException("index is not on the priority queue")
        return self.keys[i]

    def _exch(self, i, j):
        """
        Exchanges the position of items at index i and j on the heap.
        :param i: index of the first item
        :param j: index of the second item
        """
        self.pq[i], self.pq[j] = self.pq[j], self.pq[i]
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    def _greater(self, i, j):
        """
        Returns True if key at index i on the heap is greater than key at index j.
        :param i: index of the first item
        :param j: index of the second item
        :return: True if key at index i on the heap is greater than key at index j
        :rtype: bool
        """
        return self.keys[self.pq[i]] > self.keys[self.pq[j]]

    def _swim(self, k):
        """
        Moves item at index k up to a legal position on the heap.
        :param k: Index of the item on the heap to be moved
        """
        while k > 1 and self._greater(k//2, k):
            self._exch(k, k//2)
            k = k//2

    def _sink(self, k):
        """
        Moves item at index k down to a legal position on the heap.
        :param k: Index of the item on the heap to be moved
        """
        while 2*k <= self.n:
            j = 2*k
            if j < self.n and self._greater(j, j+1):
                j += 1
            if not self._greater(k, j):
                break
            self._exch(k, j)
            k = j

    def __iter__(self):
        """
        Iterates over all the items in this priority queue in ascending order.
        """
        copy = IndexMinPQ(len(self.pq)-1)
        for i in range(1, self.n + 1):
            copy.insert(self.pq[i], self.keys[self.pq[i]])
        while not copy.is_empty():
            yield copy.del_min()


def main():
    """
    Inserts a bunch of strings to an indexed priority queue,
    deletes and prints them, inserts them again, and prints them
    using an iterator.
    """
    strings = ["it", "was", "the", "best", "of", "times", "it", "was", "the", "worst"]
    pq = IndexMinPQ(len(strings))
    for i in range(len(strings)):
        pq.insert(i, strings[i])
    while not pq.is_empty():
        i = pq.del_min()
        print("{} {}".format(i, strings[i]))
    print()
    for i in range(len(strings)):
        pq.insert(i, strings[i])
    for i in pq:
        print("{} {}".format(i, strings[i]))
    while not pq.is_empty():
        pq.del_min()


if __name__ == '__main__':
    main()
