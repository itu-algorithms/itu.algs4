from . import binary_search

class TwoSumFast:
    @staticmethod
    def count(a):
        # Count pairs that sum to 0
        sorted(a)
        n = len(a)
        count = 0
        for i in range(n):
            if binary_search.index_of(a, -a[i]) > i:            
                count += 1
        return count
