# Created for BADS 2018
# See README.md for details
# This is python3 
import sys
"""
The LinearProbingHashST class represents a symbol table of dynamic
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

This implementation uses a linear probing hash table. It requires that
the key type overrides the __eq__ and __hash__ methods.
The expected time per put, contains, or remove
operation is constant, subject to the uniform hashing assumption.
The size, and is-empty operations take constant time.
Construction takes constant time.
"""
class LinearProbingHashST:
	"""
	Initializes an empty symbol table with the specified initial capacity.
	If no capacity is specified, it defaults to 4.

	:param capacity: the initial capacity
	"""
	def __init__(self, capacity = 4):
		self.m = capacity
		self.n = 0
		keys = [None for i in range(0,self.m)]
		values = [None for i in range(0,self.m)]

	def size(self):
		"""
		Returns the number of key-value pairs in this symbol table.

		:returns: the number of key-value pairs in this symbol table.
		"""
		return self.n

	def is_empty(self):
		"""
		Returns True if this symbol table is empty.

		:returns: True if this symbol table is empty;
					False otherwise
		"""
		return self.n == 0

	def contains(self, key):
		"""
		Returns True if this symbol table contains the specified key.

		:param key: the key
		:returns: True if this symbol table contains the key;
					False otherwize
		:raises ValueError: if key is None
		"""
		if(key is None):
			raise ValueError("argument to contains() is None")
		return self.get(key) is not None