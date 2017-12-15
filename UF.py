# Created for BADS 2018
# See README.md for details
# Python 3

class UF(object):
    """
    The UF class represents a union-find data type (also known as the 
    disjoint-sets data type). It supports the union and find operations, along
    with a connected operation for determining whether two sites are in the same
    component and a count operation that returns the total number of components.

    The union-find data type models connectivity among a set of n sites, named 0
    through n-1. The is-connected-to relation must be an equivalence relation:
        * Reflexive: p is connected to p.
        * Symmetric: If p is connected to q, then q is connected to p.
        * Transitive: If p is connected to q and q is connected to r, then
                           p is connected to r.

    This implementation uses weighted quick union by rank with path compression by 
    halving. Initializing a data structure with n sites takes linear time. Afterwards, 
    the union, find, and connected operations take logarithmic time (in the worst case) 
    and the count operation takes constant time. Moreover, the amortized time per union, 
    find, and connected operation has inverse Ackermann complexity.

    For additional documentation, see Section 1.5 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
    """

    def __init__(self, n):
        """
        Initializes an empty union-find data structure with n sites, 
        0 through n-1. Each site is initially in its own component.

        :param n: the number of sites
        """
        self._count = n
        self._parent = list(range(n))
        self._rank = [0]*n

    def _validate(self, p):
        # validate that p is a valid index
        n = len(self._parent)
        if p < 0 or p >= n:
            raise ValueError('index {} is not between 0 and {}'.format(p, n))

    def union(self, p, q):
        """
        Merges the component containing site p with the
        component containing site q.

        :param p: the integer representing one site
        :param q: the integer representing the other site
        """
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return

        # make root of smaller rank point to root of larger rank
        if self._rank[root_p] < self._rank[root_q]:
            self._parent[root_p] = root_q
        elif self._rank[root_p] > self._rank[root_q]:
            self._parent[root_q] = root_p
        else:
            self._parent[root_q] = root_p
            self._rank[root_p] += 1
        
        self._count -= 1

    def find(self, p):
        """
        Returns the component identifier for the component containing site p.

        :param p: the integer representing one site
        :return: the component identifier for the component containing site p
        """
        self._validate(p);
        while p != self._parent[p]:
            self._parent[p] = self._parent[self._parent[p]] # path compression by halving
            p = self._parent[p]
        return p

    def connected(self, p, q):
        """
        Returns true if the two sites are in the same component.

        :param p: the integer representing one site
        :param q: the integer representing the other site
        :return: true if the two sites p and q are in the same component; false otherwise
        """
        return self.find(p) == self.find(q)

    def count(self):
        return self._count

import sys
from stdlib import stdio

# Reads in a an integer n and a sequence of pairs of integers 
# (between 0 and n-1) from standard input, where each integer
# in the pair represents some site; if the sites are in different 
# components, merge the two components and print the pair to standard output.
if __name__ == '__main__':
    if len(sys.argv) > 1:
        try: 
            sys.stdin = open(sys.argv[1])
        except IOError:
            print("File not found, using standard input instead")
    n = stdio.readInt()
    uf = UF(n)
    while stdio.hasNextLine():
        p = stdio.readInt()
        q = stdio.readInt()
        if uf.connected(p, q):
            continue
        uf.union(p, q)
        print('{} {}'.format(p, q))
    print('number of components: {}'.format(uf.count()))
        