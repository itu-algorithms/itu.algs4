from algs4.fundamentals import binary_search

class ThreeSumFast:
    @staticmethod
    def count(a):
        # Count triples that sum to 0
        sorted(a)
        n = len(a)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if binary_search.index_of(a, -a[i]-a[j]) > i:            
                    count += 1
        return count