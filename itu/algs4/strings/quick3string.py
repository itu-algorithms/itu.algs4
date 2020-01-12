# Created for BADS 2018
# See README.md for details
# This is python3 
"""
The Quick3String module provides functions for sorting an
array of strings using 3-way radix quicksort
"""
import sys


def sort(a):
	"""
	Rearranges the array of strings in ascending order.
	:param a: the array to be sorted.
	"""
	_sort(a, 0, len(a)-1, 0)
	
def _sort(a, lo, hi, d):
	if(hi <= lo):
		return
	lt = lo
	gt = hi
	v = _char_at(a[lo], d)
	i = lo + 1
	while (i <= gt):
		t = _char_at(a[i], d)
		if (t < v):
			_exch(a, lt, i)
			lt += 1
			i += 1
		elif (t > v):
			_exch(a, i, gt)
			gt -= 1
		else:
			i += 1
	_sort(a, lo, lt-1, d)
	if (v >= 0):
		_sort(a, lt, gt, d+1)
	_sort(a, gt+1, hi, d)
	
def _char_at(s, d):
	if(d < len(s)):
		return ord(s[d])
	else:
		return -1
	
def _show(a):
	for item in a:
		print(item)
		
def is_sorted(a):
	"""
	Returns true if a is sorted.
	:param a: the array to be checked.
	:returns: True if a is sorted.
	"""
	for i in range(1,len(a)):
		if _less(a[i], a[i-1]):
			return False
	return True

def _less(v, w):
	return v < w

def _exch(a, i, j):
	t = a[i]
	a[i] = a[j]
	a[j] = t
	
def main():
	"""
	Reads in a sequence of fixed-length strings from standard input;
	3-way radix quicksorts them;
	and prints them to standard output in ascending order.
	"""
	a = sys.argv[1:]
	sort(a)
	assert is_sorted(a)
	_show(a)
	
if __name__ == "__main__":
	main()
