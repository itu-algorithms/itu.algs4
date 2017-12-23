# Created for BADS 2018
# See README.md for details
# This is python3
import sys
from random import shuffle
"""
The Quick3Way module provides static methods for sorting an
array using quicksort with 3-way partitioning.
"""
def sort(a):
	shuffle(a) #Eliminate depence on input.
	_sort(a, 0, len(a)-1)
def _sort(a, lo, hi):
	if(hi <= lo):
		return
	lt = lo
	i = lo+1
	gt = hi
	v = a[lo]
	while(i <= gt):
		cmpr = _compare(a[i],v)
		if(cmpr < 0):
			_exch(a,lt,i)
			lt += 1
			i += 1
		elif(cmpr > 0):
			_exch(a, i, gt)
			gt -= 1
		else:
			i += 1
	_sort(a,lo,lt-1)
	_sort(a,gt+1,hi)
	assert is_sorted(a)
def _compare(a,b):
	return (a > b) - (b > a)
def _less(v, w):
	return _compare(v,w) < 0
def _exch(a, i, j):
	t = a[i]
	a[i] = a[j]
	a[j] = t
def _show(a):
	#Prints the array on a single line
	for item in a:
		sys.stdout.write(item+" ")
	print
def is_sorted(a):
	for i in range(1,len(a)):
		if _less(a[i], a[i-1]):
			return False
	return True
def main():
	a = sys.argv[1:]
	sort(a)
	_show(a)
if __name__ == "__main__":
    main()
