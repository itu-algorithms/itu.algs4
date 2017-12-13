class Stack:
    def __init__(self):
        self._first = None
        self._n = 0

    def isEmpty(self):
        return self._n == 0

    def size(self):
        return self._n

    def push(self, item):
        oldfirst = self._first
        self._first = Node()
        self._first._item = item
        self._first._next = oldfirst        
        self._n += 1
    
    def pop(self):
        item = self._first._item
        self._first = self._first._next
        self._n -= 1
        return item

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
            
        item = self.current._item
        self.current = self.current._next
        return item
