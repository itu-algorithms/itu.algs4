#!/python ??
# Created for BADS 2018
# see README.md for details
# this is python3 

import sys

class Bag:
    """
    The Bag class .....

    """
    class Node:
        def __init__(self):
            self._next = None
            self._item = None


    def __init__(self):
        self._first = None
        self._n = 0

    def is_empty(self):
        return self._first is None

    def size(self):
        return self._n

    def add(self, item):
        """
        Adds the item to this bag.
        
        :param item: the item to add to this bag
        """
        oldfirst = self._first
        self._first = self.Node()
        self._first.item = item
        self._first.next = oldfirst
        self._n += 1

        # DECISION: we do the other thing
    # class ListIterator:        
    #     def __init__(self, first):
    #         self._current = first
    
    #     def __next__(self):
    #         if self._current is None: 
    #             raise StopIteration
    #         item = self._current.item
    #         self._current = self._current.next
    #         return item

    # def xx__iter__(self):
    #     return self.ListIterator(self._first)

    def __iter__(self):
        current = self._first
        while not current is None:
            yield current.item
            current = current.next



# start of the script itself
if __name__ == '__main__':
    b = Bag()
    b.add(3)
    b.add(5)
    print('size ', b.size())
    b.add(3)

    print(b)
    
    for item in b:
        print(item)
