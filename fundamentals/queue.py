import sys
from stdlib import stdio
from errors.errors import NoSuchElementException

# Created for BADS 2018
# See README.md for details
# This is python3


class Queue:
    """
    The Queue class represents a first-in-first-out (FIFO)
    queue of generic items.
    It supports the usual enqueue and dequeue
    operations, along with methods for peeking at the first item,
    testing if the queue is empty, and iterating through the items in FIFO order
    This implementation uses a singly linked list with a nested class for the linked-list nodes
    The enqueue, dequeue, peek, size, and is_empty operations all take constant time in the worst case
    """
    class Node:
        def __init__(self, item, next):
            """
            Initializes a new node
            :param item: the item to be stored in the node
            :param next: the next node in the queue
            """
            self.item = item
            self.next = next

    def __init__(self):
        """
        Initializes an empty queue.
        """
        self._first = None
        self._last = None
        self._n = 0

    def enqueue(self, item):
        """
        Adds the item to this queue.
        :param item: the item to add
        """
        old_last = self._last
        self._last = self.Node(item, None)
        if self.is_empty():
            self._first = self._last
        else:
            old_last.next = self._last
        self._n += 1

    def dequeue(self):
        """
        Removes and returns the item on this queue that was least recently added.
        :return: the item on this queue that was least recently added.
        :raises NoSuchElementException: if this queue is empty
        """
        if self.is_empty():
            raise NoSuchElementException("Queue underflow")

        item = self._first.item
        self._first = self._first.next
        self._n -= 1
        if self.is_empty():
            self._last = None
        return item

    def is_empty(self):
        """
        Returns true if this queue is empty.
        :return: True if this queue is empty otherwise False
        :rtype: bool
        """
        return self._first is None

    def size(self):
        """
        Returns the number of items in this queue.
        :return: the number of items in this queue
        :rtype: int
        """
        return self._n

    def __len__(self):
        return self.size()

    def peek(self):
        """
        Returns the item least recently added to this queue.
        :return: the item least recently added to this queue
        :raises NoSuchElementException: if this queue is empty
        """
        if self.is_empty():
            raise NoSuchElementException("Queue underflow")

        return self._first.item

    def __iter__(self):
        """
        Iterates over all the items in this queue in FIFO order.
        """
        curr = self._first
        while curr is not None:
            yield curr.item
            curr = curr.next

    def __repr__(self):
        """
        Returns a string representation of this queue.
        :return: the sequence of items in FIFO order, separated by spaces
        """
        s = []
        for item in self:
            s.append("{} ".format(item))
        return ''.join(s)


def main():
    """
    Reads strings from an input file and adds them to a queue.
    When reading a '-' it removes the least recently added item and prints it.
    Prints the amount of items left on the queue.
    """
    if len(sys.argv) > 1:
        queue = Queue()
        sys.stdin = open(sys.argv[1])
        while not stdio.isEmpty():
            input_item = stdio.readString()
            if input_item != '-':
                queue.enqueue(input_item)
            elif not queue.is_empty():
                print(queue.dequeue())
        print('({} left on queue)'.format(queue.size()))


if __name__ == '__main__':
    main()
