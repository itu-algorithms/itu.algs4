# Created for BADS 2018
# See README.md for details
# Python 3
import sys, os
def setpath():
    exe = sys.argv[0]
    p = os.path.split(exe)[0]
    sys.path.insert(0, os.path.join(p, '..', 'stdlib'))
    sys.path.insert(0, os.path.join(p, '..', 'errors'))
    sys.path.insert(0, p)
setpath()
import stdio
from errors import NoSuchElementException, IllegalArgumentException

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

    # Returns true if this symbol table is empty.
    def is_empty(self):
        return self.size() == 0

    # Returns all keys in this symbol table.
    # To iterate over all of the keys in the symbol table named {@code st},
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

    # Returns the smallest key in this symbol table greater than or equal to {@code key}.
    def ceiling(self, key):
        if key is None:
            raise IllegalArgumentException("called ceiling() with None key")
        keys = self.keys()

        #TODO continue.. 
      

    public Key ceiling(Key key) {
        if (key == null) throw new IllegalArgumentException("called ceiling() with null key");
        Key k = st.ceilingKey(key);
        if (k == null) throw new NoSuchElementException("all keys are less than " + key);
        return k;
    }

    /**
     * Returns the largest key in this symbol table less than or equal to {@code key}.
     *
     * @param  key the key
     * @return the largest key in this symbol table less than or equal to {@code key}
     * @throws NoSuchElementException if there is no such key
     * @throws IllegalArgumentException if {@code key} is {@code null}
     */
    public Key floor(Key key) {
        if (key == null) throw new IllegalArgumentException("called floor() with null key");
        Key k = st.floorKey(key);
        if (k == null) throw new NoSuchElementException("all keys are greater than " + key);
        return k;
    }

    /**
     * Unit tests the {@code ST} data type.
     *
     * @param args the command-line arguments
     */
    public static void main(String[] args) {
        ST<String, Integer> st = new ST<String, Integer>();
        for (int i = 0; !StdIn.isEmpty(); i++) {
            String key = StdIn.readString();
            st.put(key, i);
        }
        for (String s : st.keys())
            StdOut.println(s + " " + st.get(s));
    }
}
