class ThreeSum:
    @staticmethod
    def count(a):
        # Count triples that sum to 0
        n = len(a)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if a[i] + a[j] + a[k] == 0:
                        count += 1
        return count
