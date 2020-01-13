# Created for BADS 2018
# See README.md for details
# Python 3
import sys

from itu.algs4.errors.errors import IllegalArgumentException, NoSuchElementException
from itu.algs4.stdlib import stdio


"""
 The ST class represents an ordered symbol table of generic
 key-value pairs.
"""

class ST:
    def __init__(self):
        self._st = dict()

    # Returns the value associated with the given key in this symbol table.
    def get(self, key):
        if key is None:
           raise IllegalArgumentException("called get() with None key")
        return self._st.get(key)

    # Inserts the specified key-value pair into the symbol table, overwriting the old 
    # value with the new value if the symbol table already contains the specified key.
    # Deletes the specified key (and its associated value) from this symbol table
    # if the specified value is None.
    def put(self, key, val):
        if key is None:
            raise IllegalArgumentException("called put() with None key")
        if val is None:
            self._st.pop(key, None)
        else:
            self._st[key] = val

    # Removes the specified key and its associated value from this symbol table     
    # (if the key is in this symbol table).
    def delete(self, key):
        if key is None:
            raise IllegalArgumentException("called delete() with None key")
        self._st.pop(key, None)

    # Returns true if this symbol table contain the given key.
    def contains(self, key):
        if key is None:
            raise IllegalArgumentException("called contains() with None key")
        return key in self._st

    # Returns the number of key-value pairs in this symbol table.
    def size(self):
        return len(self._st)

    def __len__(self):
        return self.size()

    # Returns true if this symbol table is empty.
    def is_empty(self):
        return self.size() == 0

    # Returns all keys in this symbol table.
    # To iterate over all of the keys in the symbol table named st,
    # use the foreach notation: for key in st.keys() .
    def keys(self):
        return self._st.keys()

    def __iter__(self):
        for k in self.keys():
            yield k

    # Returns the smallest key in this symbol table.
    def min(self):
        if self.is_empty():
            raise NoSuchElementException("called min() with empty symbol table")
        return min(self._st)

    # Returns the largest key in this symbol table.
    def max(self):
        if self.is_empty():
            raise NoSuchElementException("called max() with empty symbol table")
        return max(self._st)

    # Returns the smallest key in this symbol table greater than or equal to key.
    def ceiling(self, key):
        if key is None:
            raise IllegalArgumentException("called ceiling() with None key")
        keys = self.keys()
        ceiling = None
        for k in keys:
            if (ceiling is None and k >= key) or (ceiling is not None and k>=key and k<ceiling):
                ceiling = k
        if ceiling is None:
            raise NoSuchElementException("all keys are less than " + str(key))
        return ceiling

    # Returns the largest key in this symbol table less than or equal to key.
    def floor(self, key):
        if key is None:
            raise IllegalArgumentException("called floor() with None key")
        keys = self.keys()
        floor = None
        for k in keys:
            if (floor is None and k <= key) or (floor is not None and k<=key and k>floor):
                floor = k
        if floor is None:
            raise NoSuchElementException("all keys are greater than " + str(key))
        return floor

def test():
    st = ST()
    st.put("one", 1)
    assert ["one"] == list(st.keys()) 
    assert st.get("one") == 1
    assert st.contains("one")
    st.delete("one")
    assert st.is_empty()
    st.put("aaa", 1)
    st.put("bbb", 2)
    st.put("ccc", 3)
    st.put("ddd", 4)
    st.put("eee", 5)
    assert st.ceiling("ccc") == "ccc"
    assert st.ceiling("dad") == "ddd"
    assert st.floor("ccc") == "ccc"
    assert st.floor("dad") == "ccc"
    for k in st:
        assert k in st.keys()
    assert st.min() == "aaa"
    assert st.max() == "eee"
    print("tests passed.")

if __name__ == '__main__':
    test()
    st = ST()
    i = 0
    while not stdio.isEmpty():
        key = stdio.readString()
        st.put(key, i)
        i += 1
    for s in st.keys():
        print(s + " " + str(st.get(s)))
