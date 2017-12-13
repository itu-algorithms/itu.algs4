import sys

class Bag:
    def __init__(self):
        self._first = None
        self._n = 0

    def isEmpty(self):
        return self._first is None

    def size(self):
        return self._n

    def add(self, item):
        oldfirst = self._first
        self._first = Node()
        self._first.item = item
        self._first.next = oldfirst
        self._n += 1

    def __iter__(self):
        return ListIterator(self._first)

class Node:
    def __init__(self):
        self._next = None
        self._item = None

class ListIterator:        
    def __init__(self, first):
        self.current = first
    
    def __next__(self):
        if self.current is None: 
            raise StopIteration
            
        item = self.current.item
        self.current = self.current.next
        return item
