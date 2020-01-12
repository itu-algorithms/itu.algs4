# Created for BADS 2018
# See README.md for details
# This is python3 
"""
The Insertion module provides static methods for sorting an
array using insertion sort.

This implementation makes ~ 1/2 n^2 compares and exchanges in
the worst case, so it is not suitable for sorting large arbitrary arrays.
More precisely, the number of exchanges is exactly equal to the number
of inversions. So, for example, it sorts a partially-sorted array
in linear time.
The sorting algorithm is stable and uses O(1) extra memory.
 """
import sys
from typing import List, TypeVar

T = TypeVar('T')

def sort(a: List[T]):
	"""
	Rearranges the array in ascending order, using the natural order.
	:param a: the array to be sorted.
	"""
	#Sort a[] into increasing order.
	N = len(a)
	for i in range(1,N):
		#Insert a[i] among a[i-1], a[i-2], a[i-3]...
		for j in range(i,0,-1):
			if not _less(a[j], a[j-1]):
				break
			_exch(a,j,j-1)
			
def _less(v: T, w: T):
	return v < w

def _exch(a: List[T], i: int, j: int):
	t = a[i]
	a[i] = a[j]
	a[j] = t
	
def _show(a: List[T]):
	#Prints the array on a single line
	for item in a:
		print(item, end=' ')
	print()
	
def is_sorted(a: List[T]):
	"""
	Returns true if a is sorted.
	:param a: the array to be checked.
	:returns: True if a is sorted.
	"""
	for i in range(1,len(a)):
		if _less(a[i], a[i-1]):
			return False
	return True

def main():
	"""
	Reads in a sequence of strings from standard input; Shellsorts them;
	and prints them to standard output in ascending order.
	"""
	a = sys.argv[1:]
	sort(a)
	assert is_sorted(a)
	_show(a)
	
if __name__ == "__main__":
	main()
