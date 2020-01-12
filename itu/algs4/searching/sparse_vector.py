# Created for BADS 2018
# See README.md for details
# This is python3
from math import sqrt

from itu.algs4.searching.seperate_chaining_hst import SeparateChainingHashST


class SparseVector:
	"""
	The SparseVector class represents a d-dimensional mathematical vector.
	Vectors are mutable: their values can be changed after they are created.
	It includes methods for addition, subtraction,
	dot product, scalar product, unit vector and Euclidean norm.

	The implementation is a symbol table of indices and values for which the vector
	coordinates are nonzero. This makes it efficient when most of the vector coordinates
	are zero.
	"""
	def __init__(self, d):
		"""
		Initializes a d-dimensional zero vector.
		:param d: the dimension of the vector
		"""
		self.d = d
		self.st = SeparateChainingHashST()

	def put(self, i, value):
		"""
		Sets the ith coordinate of this vector to the specified value.

		:param i: the index
		:param value: the new value
		:raises ValueError: unless i is between 0 and d-1
		"""
		if(i < 0 or i >= self.d):
			raise ValueError("Illegal index")
		if(value == 0.0):
			self.st.delete(i)
		else:
			self.st.put(i,value)
	def get(self, i):
		"""
		Returns the ith coordinate of this vector.

		:param i: the index
		:returns: the value of the ith coordinate of this vector
		:raises ValueError: unless i is between 0 and d-1
		"""
		if(i < 0 or i >= self.d):
			raise ValueError("Illegal index")
		if(self.st.contains(i)):
			return self.st.get(i)
		else:
			return 0.0

	def nnz(self):
		"""
		Returns the number of nonzero entries in this vector.

		:returns: the number of nonzero entries in this vector.
		"""
		return self.st.size()

	def dimension(self):
		"""
		Returns the dimension of this vector.
		
		:returns: the dimension of this vector.
		"""
		return self.d

	def dot(self, that):
		"""
		Returns the inner product of this vector with the specified vector.

		:param that: the other vector
		:returns: the dot product between this vector and that vector
		:raises ValueError: if the lengths of the two vectors are not equal
		"""
		if(self.d != that.d):
			raise ValueError("Vector lengths disagree")
		sum = 0.0

		#iterate over the vector with the fewest nonzeroes
		if(self.st.size() <= that.st.size()):
			for i in self.st.keys():
				if(that.st.contains(i)):
					sum += self.get(i) * that.get(i)
		else:
			for i in that.st.keys():
				if(self.st.contains(i)):
					sum += self.get(i) * that.get(i)
		return sum

	def magnitude(self):
		"""
		Returns the magnitude of this vector.
		This is also known as the L2 norm or the Euclidean norm.

		:returns: the magnitude of this vector
		"""
		return sqrt(self.dot(self))

	def scale(self, alpha):
		"""
		Returns the scalar-vector product of this vector with the specified scalar.

		:param alpha: the scalar
		:returns: the scalar-vector product of this vector with the specified scalar
		"""
		c = SparseVector(self.d)
		for i in self.st.keys():
			c.put(i, alpha*self.get(i))
		return c

	def plus(self, that):
		"""
		Returns the sum of this vector and the specified vector.

		:param that: the vector to add to this vector
		:returns: the sum of this vector and that vector
		:raises ValueError: if the dimension of the two vectors are not equal
		"""
		if(self.d != that.d):
			raise ValueError("Vector lengths disagree")
		c = SparseVector(self.d)
		for i in self.st.keys():
			c.put(i, self.get(i))
		for i in that.st.keys():
			c.put(i, that.get(i) + c.get(i))
		return c

	def __repr__(self):
		return ''.join( ("(%s,%s)" % (str(i), self.st.get(i))) for i in self.st.keys())
		
def main():
	"""
	Unit tests the SparseVector data type.
	"""
	a = SparseVector(10)
	b = SparseVector(10)
	a.put(3, 0.50)
	a.put(9, 0.75)
	a.put(6, 0.11)
	a.put(6, 0.00)
	b.put(3, 0.60)
	b.put(4, 0.90)
	print("a       = {}".format(a))
	print("b       = {}".format(b))
	print("a dot b = {}".format(a.dot(b)))
	print("a + b   = {}".format(a.plus(b)))
if __name__ == "__main__":
    main()
