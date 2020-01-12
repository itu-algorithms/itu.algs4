# created for BADS 2018
# See README.md for details
# Python 3

import sys

from itu.algs4.fundamentals.queue import Queue
from itu.algs4.stdlib import stdio

try:
    q = Queue()
    q.enqueue(1)
except AttributeError:
    print('ERROR - Could not import itu.algs4 queue')
    sys.exit(1)


"""
 *  The TrieST class represents an symbol table of key-value
 *  pairs, with string keys and generic values.
 *  It supports the usual put, get, contains,
 *  delete, size, and is-empty methods.
 *  It also provides character-based methods for finding the string
 *  in the symbol table that is the longest prefix of a given prefix,
 *  finding all strings in the symbol table that start with a given prefix,
 *  and finding all strings in the symbol table that match a given pattern.
 *  A symbol table implements the associative array abstraction:
 *  when associating a value with a key that is already in the symbol table,
 *  the convention is to replace the old value with the new value.
 *  This class uses the convention that
 *  values cannot be None, setting the
 *  value associated with a key to None is equivalent to deleting the key
 *  from the symbol table.
 *  This implementation uses a 256-way trie.
 *  The put, contains, delete, and
 *  longest prefix operations take time proportional to the length
 *  of the key (in the worst case). Construction takes constant time.
 *  The size, and is-empty operations take constant time.
 """


class TrieST(object):
    R = 256     # extended ASCII

    # R-way trie node
    class Node(object):
        R = 256
        def __init__(self):
            self.val = None
            self.next = [None] * self.R  # array of nodes of length R 

    def __init__(self):
        self._root = self.Node()    # root of trie
        self._n = 0                 # number of keys in trie


    # Returns the value associated with the given key.
    # @param key: the key
    # @return: the value associated with the given key if the key is in the symbol table
    #     and None if the key is not in the symbol table
    # @raises TypeError if key is None
    
    def get(self, key):
        x = self._get(self._root, key, 0)
        return None if x is None else x.val

    # Does this symbol table contain the given key?
    # @param key: the key
    # @returns True if this symbol table contains key and
    #     False otherwise
    # @raises TypeError if key is None

    def contains(self, key):
        return self.get(key) is not None
    
    def _get(self, x, key, d):
        if x is None:
            return None
        if d == len(key):
            return x
        c = key[d]
        return self._get(x.next[ord(c)], key, d+1) 

    # Inserts the key-value pair into the symbol table, overwriting the old value
    # with the new value if the key is already in the symbol table.
    # If the value is None, this effectively deletes the key from the symbol table.
    # @param key: the key
    # @param val: the value
    # @raises TypeError if key is None
    
    def put(self, key, val):
        if val is None:
            self.delete(key)
        else:
            self._root = self._put(self._root, key, val, 0)

    def _put(self, x, key, val, d):
        if x is None:
            x = self.Node()
        if d == len(key):
            if x.val is None:
                self._n +=1
            x.val = val
            return x
        c = key[d]
        x.next[ord(c)] = self._put(x.next[ord(c)], key, val, d+1)
        return x
    
    # @return the number of key-value pairs in this symbol table
    def size(self):
        return self._n

    def __len__(self):
        return self.size()

    # Is this symbol table empty?
    # @return True if this symbol table is empty and False otherwise
    def is_empty(self):
        return self.size() == 0
    
    
    # Returns all keys in the symbol table as an iterable object.
    # To iterate over all of the keys in the symbol table named st,
    # use the foreach notation: for key in st.keys().
    # @return all keys in the symbol table as an iterable object
    
    def keys(self):
        return self.keys_with_prefix('')

    # Returns all of the keys in the set that start with prefix.
    # @param prefix: the prefix
    # @return all of the keys in the set that start with prefix,
    #     as an iterable
    
    def keys_with_prefix(self, prefix):
        results = Queue()
        x = self._get(self._root, prefix, 0)
        self._collect(x, prefix, results)
        return results
    
    def _collect(self, x, prefix, results):
        if x is None:
            return
        if x.val is not None:
            results.enqueue(prefix)
        for c in range(0, self.R):
            self._collect(x.next[c], prefix + chr(c), results)

    # Returns all of the keys in the symbol table that match pattern,
    # where . symbol is treated as a wildcard character.
    # @param pattern the pattern
    # @return all of the keys in the symbol table that match pattern,
    #     as an iterable, where . is treated as a wildcard character.
    
    def keys_that_match(self, pattern):
        results = Queue()
        self._collect_match(self._root, '', pattern, results) 
        return results
    
    def _collect_match(self, x, prefix, pattern, results):
        if x is None:
            return None
        d = len(prefix)
        if d == len(pattern) and x.val is not None:
            results.enqueue(prefix) 
        if d >= len(pattern):
            return
        c = pattern[d]
        if c == '.':
            for c in range(0, self.R): 
                self._collect_match(x.next[c], prefix + chr(c), pattern, results) 
        else:
            self._collect_match(x.next[ord(c)], prefix + c, pattern, results)

    
    # Returns the string in the symbol table that is the longest prefix of query,
    # or None, if no such string.
    # @param query the query string
    # @return the string in the symbol table that is the longest prefix of query,
    #  or None if no such string
    # @raises TypeError if query is None
    
    def longest_prefix_of(self, query):
        length = self._longest_prefix_of(self._root, query, 0, -1)
        if length == -1:
            return None
        else:
            return query[:length]

    # returns the length of the longest string key in the subtrie
    # rooted at x that is a prefix of the query string,
    # assuming the first d character match and we have already
    # found a prefix match of given length (-1 if no such match)
    
    def _longest_prefix_of(self, x, query, d, length):
        if x is None:
            return length
        if x.val is not None:
            length = d
        if d == len(query):
            return length
        c = query[d]
        return self._longest_prefix_of(x.next[ord(c)], query, d+1, length) 
  
    # Removes the key from the set if the key is present.
    # @param key the key
    # @raises TypeError if key is None
    
    def delete(self, key):
        self._root = self._delete(self._root, key, 0)


    def _delete(self, x, key, d):
        if x is None:
            return None
        if d == len(key):
            if x.val is not None:
                self._n += -1
            x.val = None
        else:
            c = key[d]
            x.next[ord(c)] = self._delete(x.next[ord(c)], key, d+1) 
        
        # remove subtrie rooted at x if it is completely empty
        if x.val is not None:
            return x
        for c in range(0, self.R):
            if x.next[c] is not None:
                return x
        return None

def test():
    st = TrieST()
    st.put("abc", 0)
    keys = [k for k in st.keys()]
    assert keys == ["abc"]
    assert st.get("abc") == 0
    st.put("a", 1)
    st.put("b", 2)
    st.put("c", 3)
    st.delete("abc")
    assert "abc" not in [k for k in st.keys()]
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
    st = TrieST()
    i = 0
    print("Insert keys (Ctrl-D to stop):")
    while not stdio.isEmpty(): 
        key = stdio.readString()
        st.put(key, i)
        i += 1
    # print results
    if st.size() < 100:
        print('keys(""):')
        for key in st.keys():
            print('{} {}'.format(key, st.get(key)))
        print()
    print('longest_prefix_of("shellsort"):')
    print(st.longest_prefix_of('shellsort'))
    print()
    print('longest_prefix_of("quicksort")')
    print(st.longest_prefix_of('quicksort'))
    print()
    print('keys_with_prefix("shor")')
    for s in st.keys_with_prefix('shor'):
        print(s)
    print()
    print('keys_that_match("he.l.")')
    for s in st.keys_that_match('he.l.'):
        print()
