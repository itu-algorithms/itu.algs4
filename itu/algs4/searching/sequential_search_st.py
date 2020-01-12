# Created for BADS 2018
# see README.md for details
# This is python3 

class SequentialSearchST:
    """
    The  SequentialSearchST class represents an (unordered)
    symbol table of generic key-value pairs.
    It supports the usual put, get, contains,
    delete, size, and is-empty methods.
    It also provides a keys method for iterating over all of the keys.
    A symbol table implements the associative array abstraction:
    when associating a value with a key that is already in the symbol table,
    the convention is to replace the old value with the new value.
    The class also uses the convention that values cannot be  None. Setting the
    value associated with a key to  None is equivalent to deleting the key
    from the symbol table.

    This implementation uses a singly-linked list and sequential search.
    It relies on the  equals() method to test whether two keys
    are equal. It does not call either the  compareTo() or
    hashCode() method. 
    The put and delete operations take linear time the
    get and contains operations takes linear time in the worst case.
    The size, and is-empty operations take constant time.
    Construction takes constant time.
    """
    
    class Node:
        # a helper linked list data type
        def __init__(self, key, val, next):
            self.key = key
            self.val = val
            self.next = next

    def __init__(self):
        """Initializes an empty symbol table."""
        self._n = 0         # number of key-value pairs
        self._first = None  # the linked list of key-value pairs


    def size(self):
        """
        Returns the number of key-value pairs in this symbol table.

        :returns: the number of key-value pairs in this symbol table
        """
        return self._n

    def __len__(self):
        return self.size()

    def is_empty(self):
        """
        Returns true if this symbol table is empty.
        
        :returns:  true if this symbol table is empty
                 false otherwise
        """
        return self.size() == 0

    def contains(self, key):        
        """"    
        Returns true if this symbol table contains the specified key.

        :param  key the key
        :returns: true if this symbol table contains key
                  false otherwise
        :raises ValueError: if key is None
        """
        if key is None: raise ValueError("argument to contains() is None")
        return self.get(key) is not None

    def get(self, key):
        """
        Returns the value associated with the given key in this symbol table.
        
        :param key: the key
        :returns: the value associated with the given key if the key is in the symbol table
                    and None if the key is not in the symbol table
        :raises ValueError: if key is None
        """
        if key is None: raise ValueError("argument to get() is None")
        x = self._first
        while x is not None:
            if key == x.key:
                return x.val
            x = x.next
        return None
    
    def put(self, key, val):
        """
        Inserts the specified key-value pair into the symbol table, overwriting the old 
        value with the new value if the symbol table already contains the specified key.
        Deletes the specified key (and its associated value) from this symbol table
        if the specified value is None.
        
        :param key: the key
        :param val: the value
        :raises ValueError: if key is None
        """
        if key is None: raise ValueError("argument to put() is None")
        if val is None:
            self.delete(key)
            return

        x = self._first
        while x is not None:
            if key == x.key:
                x.val = val
                return
            x = x.next

        self._first = self.Node(key, val, self._first)
        self._n += 1

    def delete(self, key):
        """
        Removes the specified key and its associated value from this symbol table     
        (if the key is in this symbol table).    
                
        :param  key the key
        :raises ValueError: if key is None
        """
        if key is None: raise ValueError("argument to delete() is None")
        self._first = self._delete(self._first, key)

    def _delete(self, x, key):
        # delete key in linked list beginning at Node x
        # warning: function call stack too large if table is large
        if x is None: return None
        if key == x.key:
            self._n -= 1
            return x.next

        x.next = self._delete(x.next, key)
        return x

    def keys(self):
        """
        Returns all keys in the symbol table as an  Iterable.
        To iterate over all of the keys in the symbol table named  st,
        use the foreach notation: for Key key in st.keys().
     
        :returns: all keys in the symbol table
        """
        x = self._first
        while x is not None:
            yield x.key
            x = x.next


if __name__ == "__main__":
    from itu.algs4.stdlib import stdio

    st = SequentialSearchST()
    i = 0
    while not stdio.isEmpty():
        key = stdio.readString()
        st.put(key, i)
        i += 1
        
    for s in st.keys():
        stdio.writef("%s %i\n", s, st.get(s))
