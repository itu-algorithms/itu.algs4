# Created for BADS 2018
# see README.md for details
# This is python3 

import math

from itu.algs4.fundamentals.queue import Queue
from itu.algs4.fundamentals.uf import UF
from itu.algs4.sorting.min_pq import MinPQ


class LazyPrimMST:
    """
    The LazyPrimMST class represents a data type for computing a
    minimum spanning tree in an edge-weighted graph.
    The edge weights can be positive, zero, or negative and need not
    be distinct. If the graph is not connected, it computes a minimum
    spanning forest, which is the union of minimum spanning trees
    in each connected component. The weight() method returns the 
    weight of a minimum spanning tree and the edges() method
    returns its edges.

    This implementation uses a lazy version of Prim's algorithm
    with a binary heap of edges.
    The constructor takes time proportional to E log E
    and extra space (not including the graph) proportional to E,
    where V is the number of vertices and E is the number of edges.
    Afterwards, the weight() method takes constant time
    and the edges() method takes time proportional to V.
    """
    FLOATING_POINT_EPSILON = 1E-12

    def __init__(self,  G):
        """
        Compute a minimum spanning tree (or forest) of an edge-weighted graph.
        :param G: the edge-weighted graph
        """
        self._weight = 0.0                  # total weight of MST
        self._mst = Queue()                 # edges in the MST        
        self._marked = [False] * G.V()      # marked[v] = True if v on tree
        self._pq = MinPQ()                  # edges with one endpoint in tree

        for v in range(G.V()):              # run Prim from all vertices to
            if not self._marked[v]: 
                self._prim(G, v)            # get a minimum spanning forest

        # check optimality conditions
        assert self._check(G)

    def _prim(self, G, s):
        # run Prim's algorithm
        self._scan(G, s)
        while not self._pq.is_empty():                  # better to stop when mst has V-1 edges
            e = self._pq.del_min()                      # smallest edge on pq
            v = e.either()                              # two endpoints
            w = e.other(v)                              
            assert self._marked[v] or self._marked[w]
            if self._marked[v] and self._marked[w]:     # lazy, both v and w already scanned
                continue
            self._mst.enqueue(e)                        # add e to MST
            self._weight += e.weight()
            if not self._marked[v]: self._scan(G, v)    # v becomes part of tree
            if not self._marked[w]: self._scan(G, w)    # w becomes part of tree
        
    
    def _scan(self, G, v):
        # add all edges e incident to v onto pq if the other endpoint has not yet been scanned
        assert not self._marked[v]
        self._marked[v] = True
        for e in G.adj(v):
            if not self._marked[e.other(v)]: 
                self._pq.insert(e)
    
    def edges(self): 
        """
        Returns the edges in a minimum spanning tree (or forest).
        :returns: the edges in a minimum spanning tree (or forest) as
            an iterable of edges
        """
        return self._mst

    def weight(self):
        """
        Returns the sum of the edge weights in a minimum spanning tree (or forest).
        :returns: the sum of the edge weights in a minimum spanning tree (or forest)
        """    
        return self._weight
    
    def _check(self, G):
        # check optimality conditions (takes time proportional to E V lg* V)
        
        totalWeight = 0.0 # check weight
        for e in self.edges():
            totalWeight += e.weight()
        
        if abs(totalWeight - self.weight()) > LazyPrimMST.FLOATING_POINT_EPSILON:
            error = "Weight of edges does not equal weight(): {} vs. {}\n".format(totalWeight, self.weight())           
            print(error, file=sys.stderr)
            return False

        # check that it is acyclic
        uf = UF(G.V())
        for e in self.edges():
            v = e.either()
            w = e.other(v)
            if uf.connected(v, w):
                print("Not a forest", file=sys.stderr)
                return False            
            uf.union(v, w)
        
        # check that it is a spanning forest
        for e in G.edges():
            v = e.either()
            w = e.other(v)
            if not uf.connected(v, w):
                print("Not a forest", file=sys.stderr)
                return False

        # check that it is a minimal spanning forest (cut optimality conditions)
        for e in self.edges():
            # all edges in MST except e
            uf = UF(G.V())
            for f in self._mst:
                x = f.either()
                y = f.other(x)
                if f != e: 
                    uf.union(x, y)            

            # check that e is min weight edge in crossing cut
            for f in G.edges():
                x = f.either()
                y = f.other(x)
                if not uf.connected(x, y):
                    if f.weight() < e.weight():
                        error = "Edge {} violates cut optimality conditions".format(f)
                        print(error, file=sys.stderr)
                        return False
        return True

if __name__ == "__main__":
    import sys
    from itu.algs4.stdlib.instream import InStream
    from itu.algs4.stdlib import stdio
    from itu.algs4.graphs.edge_weighted_graph import EdgeWeightedGraph
    
    In = InStream(sys.argv[1])
    G = EdgeWeightedGraph.from_stream(In)
    mst = LazyPrimMST(G)
    for e in mst.edges():
        stdio.writeln(e)    
    stdio.writef("%.5f\n", mst.weight())
