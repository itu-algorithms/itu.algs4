# Created for BADS 2018
# See README.md for details
# This is python3 
import sys
"""
The Quick3String module provides functions for sorting an
array of strings using 3-way radix quicksort
"""
def sort(a):
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
		print item
def is_sorted(a):
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
	a = sys.argv[1:]
	sort(a)
	assert is_sorted(a)
	_show(a)
if __name__ == "__main__":
    main()