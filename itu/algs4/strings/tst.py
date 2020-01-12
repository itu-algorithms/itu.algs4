# created for BADS 2018
# see README.md for details
# Python 3

import sys

from itu.algs4.fundamentals.queue import Queue
from itu.algs4.stdlib import stdio

try:
    q = Queue()
    q.enqueue(1)
except AttributeError:
    print('ERROR - unable to import python algs4 Queue class')
    sys.exit(1)
 
 # Symbol table with string keys, implemented using a ternary search
 # trie (TST).
 
"""
  The TST class represents an symbol table of key-value
  pairs, with string keys and generic values.
  It supports the usual put, get, contains,
  delete, size, and is-empty methods.
  It also provides character-based methods for finding the string
  in the symbol table that is the longest prefix of a given prefix,
  finding all strings in the symbol table that start with a given prefix,
  and finding all strings in the symbol table that match a given pattern.
  A symbol table implements the associative array abstraction:
  when associating a value with a key that is already in the symbol table,
  the convention is to replace the old value with the new value.
  This class uses the convention that
  values cannot be None setting the
  value associated with a key to None is equivalent to deleting the key
  from the symbol table.
  This implementation uses a ternary search trie.
"""

class TST(object):
    class Node():
        def __init__(self):
            self.c = None       # character
            self.left = None    # left, middle and right subtries
            self.mid = None
            self.right = None
            self.val = None     # value associated with string

    def __init__(self):
        self.n = 0         # size
        self.root = None   # root of TST

    
    # @return the number of key-value pairs in this symbol table
    def size(self):
        return self.n

    def __len__(self):
        return self.size()

    # Does this symbol table contain the given key?
    # @param key the key
    # @return True if this symbol table contains key and
    #     False otherwise
    # @raises ValueError if key is None
    def contains(self, key):
        if key is None:
            raise ValueError("argument of contains is None") # TODO maybe get a specific exception, like IllegalArgumentException in Java
        return self.get(key) is not None

    # Returns the value associated with the given key.
    # @param key the key
    # @return the value associated with the given key if the key is in the symbol table
    #     and null if the key is not in the symbol table
    # @raises ValueError if key is None
    def get(self, key):
        if key is None:
            raise ValueError("calls get() with null argument" ) # TODO IllegalArgumentException?
        if len(key) == 0:
            raise ValueError("key must have length >=1") # TODO IllegalArgumentException?
        x = self._get(self.root, key, 0)
        if x is None:
            return None
        return x.val

    # return subtrie corresponding to given key
    def _get(self, x, key, d):
        if x is None:
            return None
        if len(key) == 0:
            raise ValueError("key nust have length >= 1")
        c = key[d]
        if c < x.c: 
            return self._get(x.left, key, d)
        elif c > x.c:
            return self._get(x.right, key, d)
        elif d < len(key) -1:
            return self._get(x.mid, key, d+1)
        else:
            return x

    # Inserts the key-value pair into the symbol table, overwriting the old value
    # with the new value if the key is already in the symbol table.
    # If the value is None, this effectively deletes the key from the symbol table.
    # @param key the key
    # @param val the value
    # @raises ValueError if key is None
    
    def put(self, key, val):
        if key is None:
            raise ValueError("calls put() with null key") # TODO IllegalArgumentException 
        if not self.contains(key):
            self.n += 1
        self.root = self._put(self.root, key, val, 0)

    def _put(self, x, key, val, d):
        c = key[d]
        if x is None:
            x = self.Node()
            x.c = c
        if c < x.c:
            x.left = self._put(x.left, key, val, d)
        elif c > x.c:
            x.right = self._put(x.right, key, val, d)
        elif d < len(key) -1:
            x.mid = self._put(x.mid, key, val, d+1)
        else:
            x.val = val

        return x

    # Returns the string in the symbol table that is the longest prefix of query,
    # or None, if no such string.
    # @param query the query string
    # @return the string in the symbol table that is the longest prefix of query,
    #     or None if no such string
    # @raises ValueError if query is None
    
    def longest_prefix_of(self, query):
        if query is None:
            raise ValueError("calls longest_path_of() with None argument")
        if len(query) == 0:
            return None
        length = 0
        x = self.root
        i = 0
        while (x is not None and i < len(query)):
            c = query[i]
            if c < x.c:
                x = x.left
            elif c > x.c:
                x = x.right
            else:
                i += 1
                if x.val is not None:
                    length = i
                x = x.mid
        return query[0:length]

    # Returns all keys in the symbol table as an Iterable.
    # To iterate over all of the keys in the symbol table named st,
    # use the foreach notation: for key in st.keys().
    # @return all keys in the symbol table as an Iterable
    
    def keys(self):
        queue = Queue()
        self._collect(self.root, "", queue)
        return queue
        
    # Returns all of the keys in the set that start with prefix.
    # @param prefix the prefix
    # @return all of the keys in the set that start with prefix,
    #     as an iterable
    # @raises ValueError if prefix is None
    
    def keys_with_prefix(self, prefix):
        if prefix is None:
            raise ValueError("calls keys_with_prefix with null argument") # TODO IllegalArgumentException
        queue = Queue()
        x = self._get(self.root, prefix, 0)
        if x is None:
            return queue
        if x.val is not None:
            queue.enqueue(prefix)
        self._collect(x.mid, prefix, queue)
        return queue

    # all keys in subtrie rooted at x with given prefix
    def _collect(self, x, prefix, queue):
        if x is None:
            return
        self._collect(x.left, prefix, queue)
        if x.val is not None:
            queue.enqueue(prefix + str(x.c))
        self._collect(x.mid, prefix + str(x.c), queue)
        self._collect(x.right, prefix, queue)
    
    # Returns all of the keys in the symbol table that match pattern,
    # where . symbol is treated as a wildcard character.
    # @param pattern the pattern
    # @return all of the keys in the symbol table that match pattern,
    #     as an iterable, where . is treated as a wildcard character.
    
    def keys_that_match(self, pattern):
        queue = Queue()
        self._collect_match(self.root, "", 0, pattern, queue)
        return queue
        
    def _collect_match(self, x, prefix, i, pattern, queue):
        if x is None:
            return
        c = pattern[i] 
        if c == '.' or c <x.c:
            self._collect_match(x.left, prefix, i, pattern, queue)
        if c == '.' or c == x.c:
            if i == len(pattern) -1 and x.val is not None:
                queue.enqueue(prefix + str(x.c)) 
            if i < len(pattern) -1:
                self._collect_match(x.mid, prefix + x.c, i+1, pattern, queue)
        if c == '.' or c > x.c:
            self._collect_match(x.right, prefix, i, pattern, queue)

# * Unit tests the TST data type.
def test():
    st = TST()
    st.put("abc", 0)
    keys = [k for k in st.keys()]
    assert keys == ["abc"]
    assert st.get("abc") == 0
    st.put("a", 1)
    st.put("b", 2)
    st.put("c", 3)
    #st.delete("abc")
    #assert "abc" not in [k for k in st.keys()]
    assert st.get("a") == 1
    assert st.get("b") == 2
    assert st.get("c") == 3
    st.put("hello", 10)
    assert st.contains("hello")
    assert st.contains("not there") is False
    st.put("he", 20)
    assert st.longest_prefix_of("hell") == "he"
    st.put("jello", 30)
    q = st.keys_that_match(".e.l.")
    assert q.size() == 2 and "jello" in q and "hello" in q
    print("tests passed.")

if __name__ == '__main__':
    test()
    st = TST()
    i = 0
    # build symbol table from stdin
    print("Insert keys (Ctrl-D to stop):")
    while not stdio.isEmpty():
        key = stdio.readString()
        st.put(key, i)
        i += 1
    # print results
    if st.size() < 100:
        print('keys(""):')
        for key in st.keys():
            print("{} {}".format(key, st.get(key)))
        print()
            
        print("longestPrefixOf(\"shellsort\"):")
        print(st.longest_prefix_of("shellsort"))
        print()

        print("longestPrefixOf(\"shell\"):")
        print(st.longest_prefix_of("shell"))
        print()

        print("keysWithPrefix(\"shor\"):")
        for s in st.keys_with_prefix("shor"):
            print(s)
        print()

        print("keysThatMatch(\".he.l.\"):")
        for s in st.keys_that_match(".he.l."):
            print(s)
