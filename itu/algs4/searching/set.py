# Created for BADS 2018
# See README.md for details
# Python 3
import sys

from itu.algs4.errors.errors import (
    IllegalArgumentException,
    NoSuchElementException,
    UnsupportedOperationException,
)


"""
Set implementation using Python's set() type.
Does not allow duplicates.
"""

class SET:
    # Initializes a new set that is an independent copy of the specified set, or an empty one.
    def __init__(self, x=None):
        self._set = set() if x is None else x._set.copy()

    # Adds the key to this set (if it is not already present).
    def add(self, key):
        if key is None:
            raise IllegalArgumentException("called add() with a None key")
        self._set.add(key)

    # Returns true if this set contains the given key.
    def contains(self, key):
        if key is None:
            raise IllegalArgumentException("called contains() with a None key")
        return key in self._set

    # Removes the specified key from this set (if the set contains the specified key).
    def delete(self, key):
        if key is None:
            raise IllegalArgumentException("called delete() with a None key")
        if self.contains(key):
            self._set.remove(key)

    # Returns the number of keys in this set.
    def size(self):
        return len(self._set)
        
    def __len__(self):
        return self.size()

    # Returns true if this set is empty.
    def is_empty(self):
        return self.size() == 0
    # Returns all of the keys in this set, as an iterator.
    # To iterate over all of the keys in a set named set, use the
    # foreach notation: for key in set.
    def __iter__(self):
        for k in self._set:
            yield k

    # Returns the largest key in this set.
    def max(self):
        if self.is_empty():
            raise NoSuchElementException("called max() with empty set")
        return max(self._set)

    # Returns the smallest key in this set.
    def min(self):
        if self.is_empty():
            raise NoSuchElementException("called min() with empty set")
        return min(self._set)

    # Returns the smallest key in this set greater than or equal to key.
    def ceiling(self, key):
        if key is None:
            raise IllegalArgumentException("called ceiling() with None key")
        ceiling = None
        for k in self:
            if (ceiling is None and k >= key) or (ceiling is not None and k>=key and k<ceiling):
                ceiling = k
        if ceiling is None:
            raise NoSuchElementException("all keys are less than " + str(key))
        return ceiling

    # Returns the largest key in this set less than or equal to key.
    def floor(self, key):
        if key is None:
            raise IllegalArgumentException("called floor() with None key")
        floor = None
        for k in self:
            if (floor is None and k <= key) or (floor is not None and k<=key and k>floor):
                floor = k
        if floor is None:
            raise NoSuchElementException("all keys are greater than " + str(key))
        return floor

    # Returns the union of this set and that set.
    def union(self, that):
        if that is None:
            raise IllegalArgumentException("called union() with a None argument")
        c = set()
        for x in self:
            c.add(x)
        for x in that:
            c.add(x)
        return c

    # Returns the intersection of this set and that set.
    def intersects(self, that):
        if that is None:
            raise IllegalArgumentException("called intersects() with a null argument")
        c = set()
        if self.size() < that.size():
            for x in self:
                if that.contains(x):
                    c.add(x)
        else:
            for x in that:
                if self.contains(x):
                    c.add(x)
        return c
     
    # Compares this set to the specified set.
    def __eq__(self, other):
        if other is None:
            return False
        if type(other) != type(self):
            return False
        return self._set == other._set

    # This operation is not supported because sets are mutable.
    def hashCode(self):
        raise UnsupportedOperationException("hashCode() is not supported because sets are mutable")
    
    # Returns a string representation of this set.
    def __repr__(self):
        s = []
        for item in self:
            s.append("{}".format(item))
        return "{ " + ''.join(s) + " }"


def main():
    set = SET()
    print("set = " + str(set))

    # insert some keys
    set.add("www.cs.princeton.edu")
    set.add("www.cs.princeton.edu")    # overwrite old value
    set.add("www.princeton.edu")
    set.add("www.math.princeton.edu")
    set.add("www.yale.edu")
    set.add("www.amazon.com")
    set.add("www.simpsons.com")
    set.add("www.stanford.edu")
    set.add("www.google.com")
    set.add("www.ibm.com")
    set.add("www.apple.com")
    set.add("www.slashdot.com")
    set.add("www.whitehouse.gov")
    set.add("www.espn.com")
    set.add("www.snopes.com")
    set.add("www.movies.com")
    set.add("www.cnn.com")
    set.add("www.iitb.ac.in")


    print(set.contains("www.cs.princeton.edu"))
    print(not set.contains("www.harvardsucks.com"))
    print(set.contains("www.simpsons.com"))
    print()

    print("ceiling(www.simpsonr.com) = " + set.ceiling("www.simpsonr.com"))
    print("ceiling(www.simpsons.com) = " + set.ceiling("www.simpsons.com"))
    print("ceiling(www.simpsont.com) = " + set.ceiling("www.simpsont.com"))
    print("floor(www.simpsonr.com)   = " + set.floor("www.simpsonr.com"))
    print("floor(www.simpsons.com)   = " + set.floor("www.simpsons.com"))
    print("floor(www.simpsont.com)   = " + set.floor("www.simpsont.com"))
    print()

    print("set = " + str(set))
    print()

    # print out all keys in this set in lexicographic order
    for s in set:
        print(s)

    print()
    set2 = SET(set)
    print(set == set2)

if __name__ == '__main__':
    main()
