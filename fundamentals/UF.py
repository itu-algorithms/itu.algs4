class UF(object):
    """
    Union-find implementation: QuickFind, union by rank, path halving


    ?? more from the docstring there ??

    corresponds to https://algs4.cs.princeton.edu/code/edu/princeton/cs/algs4/UF.java.html
    """

    def __init__(self, n):
        self.count = n
        self.parent = list(range(n))
        self.size = [1]*n

    def _validate(self, p):
        n = len(self.parent)
        if p < 0 or p >= n:
            raise ValueError('index {} is not between 0 and {}'.format(p, n))

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return

        if self.size[root_p] < self.size[root_q]:
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        else:
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]
        
        self.count -= 1

    def find(self, p):
        self._validate(p);
        while p != self.parent[p]:
            p = self.parent[p]
        return p

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def count(self):
        return self.count

# ?? the main method from .. (based on stdin)
