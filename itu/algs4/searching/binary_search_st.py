# Created for BADS 2018
# see README.md for details
# This is python3 

from itu.algs4.fundamentals.queue import Queue


class BinarySearchST:
    """
    The BST class represents an ordered symbol table of generic
    key-value pairs.
    It supports the usual put, get, contains,
    delete, size, and is-empty methods.
    It also provides ordered methods for finding the minimum,
    maximum, floor, select, and ceiling.
    It also provides a keys method for iterating over all of the keys.
    A symbol table implements the associative array abstraction:
    when associating a value with a key that is already in the symbol table,
    the convention is to replace the old value with the new value.
    Unlike java.util.Map, this class uses the convention that
    values cannot be None—setting the
    value associated with a key to None is equivalent to deleting the key
    from the symbol table.

    This implementation uses a sorted array. It requires that
    the key type implements the Comparable interface and calls the
    compareTo() and method to compare two keys. It does not call either
    equals() or  hashCode().
    The put and remove operations each take linear time in
    the worst case the contains, ceiling, floor,
    and rank operations take logarithmic time the size,
    is-empty, minimum, maximum, and select
    operations take constant time. Construction takes constant time.
    """
    _INIT_CAPACITY = 2

    def __init__(self, capacity = _INIT_CAPACITY):
        """
        Initializes an empty symbol table with the specified initial capacity.
        :param capacity: the maximum capacity        
        """
        self._keys = [None] * capacity
        self._vals = [None] * capacity
        self._n = 0
    
    def _resize(self, capacity):
        # resize the underlying "arrays"
        assert capacity >= self._n
        tempk = [None] * capacity
        tempv = [None] * capacity
        for i in range(self._n):
            tempk[i] = self._keys[i]
            tempv[i] = self._vals[i]
        
        self._vals = tempv
        self._keys = tempk
    
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
        Returns True if this symbol table is empty.
        
        :returns: True if this symbol table is empty
                False otherwise
        """
        return self.size() == 0

    def contains(self, key):
        """
        Does this symbol table contain the given key?

        :param key: the key
        :returns:  True if this symbol table contains  key and
                False otherwise
        :raises ValueError: if  key is  None
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
        if self.is_empty(): return None
        i = self.rank(key)
        if i < self._n and self._keys[i] == key: return self._vals[i]
        return None
    
    def rank(self, key):
        """
        Returns the number of keys in this symbol table strictly less than  key.
        
        :param key: the key
        :returns: the number of keys in the symbol table strictly less than  key
        :raises ValueError: if  key is  None
        """
        if key is None: raise ValueError("argument to rank() is None") 

        lo = 0
        hi = self._n-1 
        while lo <= hi: 
            mid = int(lo + (hi - lo) / 2)
            if key < self._keys[mid]: hi = mid - 1 
            elif key > self._keys[mid]: lo = mid + 1 
            else: return mid         
        return lo
    
    def put(self, key, val):
        """
        Inserts the specified key-value pair into the symbol table, overwriting the old 
        value with the new value if the symbol table already contains the specified key.
        Deletes the specified key (and its associated value) from this symbol table
        if the specified value is None.
        
        :param key: the key
        :param val: the value
        :raises ValueError: if  key is None
        """
        if key is None: raise ValueError("first argument to put() is None") 

        if val is None:
            self.delete(key)
            return
        
        i = self.rank(key)

        # key is already in table
        if i < self._n and self._keys[i] == key:
            self._vals[i] = val
            return        

        # insert new key-value pair
        if self._n == len(self._keys): self._resize(2*len(self._keys))

        j = self._n
        while j > i:
            self._keys[j] = self._keys[j-1]
            self._vals[j] = self._vals[j-1]
            j -= 1
        
        self._keys[i] = key
        self._vals[i] = val
        self._n += 1

        assert self._check()
     
    def delete(self, key):
        """
        Removes the specified key and associated value from this symbol table
        (if the key is in the symbol table).
        
        :param key: the key
        :raises ValueError: if  key is  None
        """
        if key is None: raise ValueError("argument to delete() is None") 
        if self.is_empty(): return

        # compute rank
        i = self.rank(key)
        n = self._n

        # key not in table
        if i == n or self._keys[i] != key:
            return

        j = i
        while j < self._n-1:
            self._keys[j] = self._keys[j+1]
            self._vals[j] = self._vals[j+1]
            j += 1

        self._n -= 1
        n = self._n
        self._keys[n] = None  # to avoid loitering
        self._vals[n] = None

        # resize if 1/4 full
        if n > 0 and n == len(self._keys)/4: self._resize(len(self._keys)/2)

        assert self._check()
    
    def deleteMin(self):
        """
        Removes the smallest key and associated value from this symbol table.
        
        :raises ValueError: if the symbol table is empty
        """
        if self.is_empty(): raise ValueError("Symbol table underflow error")
        self.delete(self.min())    

    def deleteMax(self):
        """
        Removes the largest key and associated value from this symbol table.
        
        :raises ValueError: if the symbol table is empty
        """
        if self.is_empty(): raise ValueError("Symbol table underflow error")
        self.delete(self.max())
    
   #*************************************************************************
   #                    Ordered symbol table methods.
   #*************************************************************************
    
    def min(self):
        """
        Returns the smallest key in this symbol table.
        
        :returns: the smallest key in this symbol table
        :raises ValueError: if this symbol table is empty
        """
        if self.is_empty(): raise ValueError("called min() with empty symbol table")
        return self._keys[0]
    

    def max(self):
        """
        Returns the largest key in this symbol table.
        
        :returns: the largest key in this symbol table
        :raises ValueError: if this symbol table is empty
        """
        if self.is_empty(): raise ValueError("called max() with empty symbol table")
        return self._keys[self._n-1]
   
    def select(self, k):
        """
        Return the kth smallest key in this symbol table.
        
        :param k: the order statistic
        :returns: the  kth smallest key in this symbol table
        :raises ValueError: unless k is between 0 and n-1
        """
        if k < 0 or k >= self.size():
            raise ValueError("called select() with invalid argument: {}".format(k))
        
        return self._keys[k]
    
    def floor(self, key):
        """
        Returns the largest key in this symbol table less than or equal to  key.
        
        :param key: the key
        :returns: the largest key in this symbol table less than or equal to  key
        :raises ValueError: if there is no such key
        :raises ValueError: if  key is  None
        """
        if key is None: raise ValueError("argument to floor() is None") 
        i = self.rank(key)
        if i < self._n and key == self._keys[i]: return self._keys[i]
        if i == 0: return None
        else: return self._keys[i-1]
    

    
    def ceiling(self, key):
        """
        Returns the smallest key in this symbol table greater than or equal to key.
        
        :param key: the key
        :returns: the smallest key in this symbol table greater than or equal to key
        :raises ValueError: if there is no such key
        :raises ValueError: if key is None
        """
        if key is None: raise ValueError("argument to ceiling() is None") 
        i = self.rank(key)
        if i == self._n: return None 
        else: return self._keys[i]
    
    def size_between(self, lo, hi):
        """
        Returns the number of keys in this symbol table in the specified range.
        
        :param lo: minimum endpoint
        :param hi: maximum endpoint
        :returns: the number of keys in this symbol table between lo 
            (inclusive) and  hi (inclusive)
        :raises ValueError: if either lo or hi is None
        """
        if lo is None: raise ValueError("first argument to size() is None") 
        if hi is None: raise ValueError("second argument to size() is None") 

        if lo > hi: return 0
        if self.contains(hi): return self.rank(hi) - self.rank(lo) + 1
        else:                 return self.rank(hi) - self.rank(lo)
   
    def keys(self):
        """
        Returns all keys in this symbol table as an  Iterable.
        To iterate over all of the keys in the symbol table named  st,
        use the foreach notation: for (Key key : st.keys()).
        
        :returns: all keys in this symbol table
        """
        return self.keys_between(self.min(), self.max())
    
    def keys_between(self, lo, hi):
        """
        Returns all keys in this symbol table in the given range,
        as an  Iterable.
        
        :param lo: minimum endpoint
        :param hi: maximum endpoint
        :returns: all keys in this symbol table between lo 
            (inclusive) and hi (inclusive)
        :raises ValueError: if either lo or hi are None
        """
        if lo is None: raise ValueError("first argument to keys() is None") 
        if hi is None: raise ValueError("second argument to keys() is None") 

        queue = Queue() 
        if lo > hi: return queue

        i = self.rank(lo)
        end = self.rank(hi)
        while i < end:
            queue.enqueue(self._keys[i])
            i += 1

        if self.contains(hi): queue.enqueue(self._keys[self.rank(hi)])
        return queue 

   #*************************************************************************
   #                    Check internal invariants.
   #*************************************************************************

    def _check(self):
        return self._is_sorted() and self._rank_check()
    
    
    def _is_sorted(self):
        # are the items in the array in ascending order?
        i = 1
        while i < self.size():
            if self._keys[i] < self._keys[i -1]: return False
            i += 1
        return True
    
    def _rank_check(self):
        # check that rank(select(i)) = i
        for i in range(self.size()):
            if i != self.rank(self.select(i)): return False
        for i in range(self.size()):
            if self._keys[i] != self.select(self.rank(self._keys[i])): return False
        return True
        
if __name__ == "__main__":
    from itu.algs4.stdlib import stdio

    st = BinarySearchST()
    i = 0
    while not stdio.isEmpty():
        key = stdio.readString()
        st.put(key, i)
        i += 1
        
    for s in st.keys():
        stdio.writef("%s %i\n", s, st.get(s))
