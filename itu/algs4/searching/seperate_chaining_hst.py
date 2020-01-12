# Created for BADS 2018
# See README.md for details
# This is python3 
import sys

from itu.algs4.searching.sequential_search_st import SequentialSearchST


class SeparateChainingHashST:
	"""
	The SeparateChainingHashST class represents a symbol table of dynamic
	key-value pairs.
	It supports the usual put, get, contains, delete, size, 
	and is-empty methods.
	It also provides a keys method for iterating over all of the keys.
	A symbol table implements the associative array abstraction:
	when associating a value with a key that is already in the symbol table,
	the convention is to replace the old value with the new value.
	Unlike the Map-class in Java, this class uses the convention that
	values cannot be null/None. Setting the
	value associated with a key to None is equivalent to deleting the key
	from the symbol table.

	This implementation uses a separate chaining hash table. It requires that
	the key type overrides the __eq__ and __hash__ methods.
	The expected time per put, contains, or remove
	operation is constant, subject to the uniform hashing assumption.
	The size, and is-empty operations take constant time.
	Construction takes constant time.
	"""
	def __init__(self, M = 997):
		self.M = M #Hash table size
		self.N = 0 #Number of pairs
		self.st = [SequentialSearchST() for i in range(0,M)] #Array of ST objects

	def _hash(self, key):
		#Hash value between 0 and M-1
		return (hash(key) & 0x7fffffff) % self.M

	def get(self, key):
		"""
		Returns the value associated with the specified key.

		:param key: the key
		:returns: the value associated with the key in the symbol table;
					None if no such value
		:raises ValueError: if key is None
		"""
		if(key is None):
			raise ValueError("argument to get() is None")
		i = self._hash(key)
		return self.st[i].get(key)

	def put(self, key, value):
		"""
		Inserts the specified key-value paur into the symbol table, overwriting the old
		value with the new value if the symbol table already contains the specified key.
		Deletes the specified key (and its associated value) from this symbol table
		if the specified value is None.

		:param key: the key
		:param value: the value
		:raises ValueError: if key is None.
		"""
		if(key is None):
			raise ValueError("first argument to put() is None")
		if(value is None):
			self.delete(key)
			return
		i = self._hash(key)
		if(not self.st[i].contains(key)):
			self.N += 1
		self.st[i].put(key, value)
		self.st[self._hash(key)].put(key, value)

	def size(self):
		"""
		Returns the number of key-value pairs in this symbol table.

		:returns: the number of key-value pairs in this symbol table.
		"""
		return self.N

	def is_empty(self):
		"""
		Returns true if the symbol table is empty.

		:returns: True if this symbol table is empty;
					False otherwise.
		"""
		return (self.N == 0)

	def contains(self, key):
		"""
		Returns true if this symbol table contains the specified key.

		:param key: the key
		:returns: True if this symbol table contains the key;
					False otherwise.
		:raises ValueError: if key is None.
		"""
		if(key == None):
			raise ValueError("argument to contains() is None")
		return self.get(key) is not None

	def delete(self, key):
		"""
		Removes the specified key and its associated value from this symbol table
		(if the key is in this symbol table).

		:param key: the key
		:raises ValueError: if key is None
		"""
		if(key is None):
			raise ValueError("argument to delete() is None")
		i = self._hash(key)
		if(self.st[i].contains(key)):
			self.N -= 1
		self.st[i].delete(key)

	def keys(self):
		"""
		Returns the keys in the symbol table as an iterable
		:returns: A list containing all keys
		"""
		keys = []
		for i in range(0,self.M):
			for key in self.st[i].keys():
				keys.append(key)
		return keys

	def __len__(self):
		return self.size()
def main():
	"""
	Unit tests the SeparateChainingHashST data type.
	"""
	st = SeparateChainingHashST()
	i = 0
	for key in sys.argv[1:]:
		st.put(key, i)
		i += 1
	for key in st.keys():
		print('{} {}'.format(key, st.get(key)))
		
if __name__ == "__main__":
	main()
