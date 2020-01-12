# Created for BADS 2018
# See README.md for details
# This is python3 
import sys


class LinearProbingHashST:
	"""
	The LinearProbingHashST class represents a symbol table of dynamic
	key-value pairs.
	It supports the usual put, get, contains, delete, size, 
	and is-empty methods.
	It also provides a key_list method for iterating over all of the keys.
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
	def __init__(self, capacity = 4):
		"""
		Initializes an empty symbol table with the specified initial capacity.
		If no capacity is specified, it defaults to 4.

		:param capacity: the initial capacity
		"""
		self.m = capacity
		self.n = 0
		self.keys = [None for i in range(0,self.m)]
		self.values = [None for i in range(0,self.m)]

	def size(self):
		"""
		Returns the number of key-value pairs in this symbol table.

		:returns: the number of key-value pairs in this symbol table.
		"""
		return self.n

	def __len__(self):
                return self.size()

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

	def _hash(self, key):
		#Hash value between 0 and M-1
		return (hash(key) & 0x7fffffff) % self.m

	def _resize(self, capacity):
		# Resizes the hash table to the given capacity by re-hashing all of the keys
		temp = LinearProbingHashST(capacity)
		for i in range(0,self.m):
			if(self.keys[i] is not None):
				temp.put(self.keys[i], self.values[i])
		self.keys = temp.keys
		self.values = temp.values
		self.m = temp.m

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
			raise ValueError("argument to put() is None")
		if(value is None):
			self.delete(key)
			return
		# Double table size if 50% full
		if (self.n >= self.m/2):
			self._resize(2*self.m)

		i = self._hash(key)
		while(self.keys[i] is not None):
			if(self.keys[i] == key):
				self.values[i] = value
				return
			i = (i+1) % self.m
		self.keys[i] = key
		self.values[i] = value
		self.n += 1

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
		while(self.keys[i] is not None):
			if(self.keys[i] == key):
				return self.values[i]
			i = (i+1) % self.m
		return None

	def delete(self, key):
		"""
		Removes the specified key and its associated value from this symbol table
		(if the key is in this symbol table).

		:param key: the key
		:raises ValueError: if key is None
		"""
		if(key is None):
			raise ValueError("argument to delete() is None")
		if(not self.contains(key)):
			return
		# Find position i of key
		i = self._hash(key)
		while(not key == self.keys[i]):
			i = (i+1) % self.m
		# Delete key and associated value
		self.keys[i] = None
		self.values[i] = None
		# Rehash all keys in same cluster
		i = (i+1) % self.m
		while(self.keys[i] is not None):
			# Delete keys[i] and values[i] and reinsert
			keyToRehash = self.keys[i]
			valueToReash = self.values[i]
			self.keys[i] = None
			self.values[i] = None
			self.n -= 1
			self.put(keyToRehash, valueToReash)
			i = (i+1) % self.m
		self.n -= 1

		# Halves table size if it's less than 12.5% full
		if(self.n > 0 and self.n <= self.m/8):
			self._resize(self.m/2)

		assert self._check()

	def key_list(self):
		"""
		Returns the keys in the symbol table as an iterable
		:returns: A list containing all keys
		"""
		keys = []
		for i in range(0,self.m):
			if(self.keys[i] is not None):
				keys.append(self.keys[i])
		return keys

	def _check(self):
		# Integrity check - don't check after each put() because
		# integrity is not maintained during delete()
		if(self.m < 2*self.n):
			print("Hash table size m = {}; List size n = {}".format(self.m, self.n))
			return False
		for i in range(0,self.m):
			if(self.keys[i] is None):
				continue
			elif(self.get(self.keys[i]) != self.values[i]):
				print("get[{}] = {}; values[i] = {}".format(self.keys[i], self.get(self.keys[i]), self.values[i]))
				return False
		return True

def main():
	"""
	Unit tests the LinearProbingHashST data type.
	"""
	st = LinearProbingHashST()
	i = 1
	for key in sys.argv[1:]:
		st.put(key, i)
		i += 1
	for key in st.key_list():
		print("{} {}".format(key, st.get(key)))
if __name__ == "__main__":
    main()
