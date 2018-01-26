#!/python ??
# Created for BADS 2018
# see README.md for details
# this is python3 

class Bag:
    """
    The Bag class represents a bag (or multiset) of 
    generic items. It supports insertion and iterating over the 
    items in arbitrary order.

    This implementation uses a singly linked list with a static nested class Node.
    See LinkedBag for the version from the
    textbook that uses a non-static nested class.
    See ResizingArrayBag for a version that uses a resizing array.
    The add, is_empty, and size operations
    take constant time. Iteration takes time proportional to the number of items.
    """
    class Node:
        # helper linked list class
        def __init__(self):
            self._next = None
            self._item = None

    def __init__(self):
        """
        Initializes an empty bag.
        """
        self._first = None # beginning of bag
        self._n = 0        # number of elements in bag 

    def is_empty(self):
        """
        Returns true if this bag is empty.

        :returns: true if this bag is empty
                  false otherwise
        """
        return self._first is None

    def size(self):
        """
        Returns the number of items in this bag.

        :returns: the number of items in this bag
        """
        return self._n

    def add(self, item):
        """
        Adds the item to this bag.
        
        :param item: the item to add to this bag
        """
        oldfirst = self._first
        self._first = self.Node()
        self._first._item = item
        self._first._next = oldfirst
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
        """
        Returns an iterator that iterates over the items in this bag in arbitrary order.

        :returns: an iterator that iterates over the items in this bag in arbitrary order
        """
        current = self._first
        while not current is None:
            yield current._item
            current = current._next

    def __repr__(self):
        out = '{'
        for elem in self:
            out += '{}, '.format(elem)
        return out + '}'


# start of the script itself
if __name__ == '__main__':
    import sys
    sys.path.append("..")
    from algs4.stdlib import stdio

    bag = Bag()
    while not stdio.isEmpty():
        item = stdio.readString()
        bag.add(item)

    stdio.writef("size of bag = %i\n", bag.size())
    
    for s in bag:
        stdio.writeln(s)
    
