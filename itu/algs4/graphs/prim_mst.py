# Created for BADS 2018
# see README.md for details
# This is python3 
import math
import sys

from itu.algs4.fundamentals.queue import Queue
from itu.algs4.fundamentals.uf import UF
from itu.algs4.sorting.index_min_pq import IndexMinPQ


class PrimMST:
    """
    The PrimMST class represents a data type for computing a
    minimum spanning tree in an edge-weighted graph.
    The edge weights can be positive, zero, or negative and need not
    be distinct. If the graph is not connected, it computes a minimum
    spanning forest, which is the union of minimum spanning trees
    in each connected component. The weight() method returns the 
    weight of a minimum spanning tree and the edges() method
    returns its edges.
    
    This implementation uses Prim's algorithm with an indexed
    binary heap.
    The constructor takes time proportional to E log V
    and extra space not including the graph) proportional to V,
    where V is the number of vertices and E is the number of edges.
    Afterwards, the weight() method takes constant time
    and the edges() method takes time proportional to V.
    """

    FLOATING_POINT_EPSILON = 1E-12

    def __init__(self, G):
        """
        Compute a minimum spanning tree (or forest) of an edge-weighted graph.
        :param G: the edge-weighted graph
        """
        self._edge_to = [None] * G.V()         # self._edge_to[v] = shortest edge from tree vertex to non-tree vertex
        self._dist_to = [0.0] * G.V()       # self._dist_to[v] = weight of shortest such edge
        self._marked = [False] * G.V()      # self._marked[v] = True if v on tree, False otherwise
        self._pq = IndexMinPQ(G.V())
        
        for v in range(G.V()):
            self._dist_to[v] = math.inf

        for v in range(G.V()):              # run from each vertex to find
            if not self._marked[v]:         
                 self._prim(G, v)                  # minimum spanning forest

        # check optimality conditions
        assert  self._check(G)

    # run Prim's algorithm in graph G, starting from vertex s
    def _prim(self, G, s):
        self._dist_to[s] = 0.0
        self._pq.insert(s, self._dist_to[s])
        while not self._pq.is_empty():
            v = self._pq.del_min()
            self._scan(G, v)
    
    def _scan(self, G, v):
        # scan vertex v        
        self._marked[v] = True
        for e in G.adj(v):
            w = e.other(v)
            if self._marked[w]: continue         # v-w is obsolete edge
            if e.weight() < self._dist_to[w]:
                self._dist_to[w] = e.weight()
                self._edge_to[w] = e
                if self._pq.contains(w):    self._pq.decrease_key(w, self._dist_to[w])
                else:                       self._pq.insert(w, self._dist_to[w])


    def edges(self):
        """
        Returns the edges in a minimum spanning tree (or forest).
        :returns: the edges in a minimum spanning tree (or forest) as
                an iterable of edges
        """
        mst = Queue()
        for v in range(len(self._edge_to)):
            e = self._edge_to[v]
            if e is not None:
                mst.enqueue(e)
        
        return mst

    def weight(self):
        """
        Returns the sum of the edge weights in a minimum spanning tree (or forest).
        :returns: the sum of the edge weights in a minimum spanning tree (or forest)
        """
        weight = 0.0
        for e in self.edges():
            weight += e.weight()
        return weight

    def _check(self, G):
        # check optimality conditions (takes time proportional to E V lg* V)
        
        totalWeight = 0.0 # check weight
        for e in self.edges():
            totalWeight += e.weight()
        
        if abs(totalWeight - self.weight()) > PrimMST.FLOATING_POINT_EPSILON:
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
                print("Not a spanning forest", file=sys.stderr)
                return False

         # check that it is a minimal spanning forest (cut optimality conditions)
        for e in self.edges():
            # all edges in MST except e
            uf = UF(G.V())
            for f in self.edges():
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
    from itu.algs4.stdlib.instream import InStream
    from itu.algs4.stdlib import stdio
    from itu.algs4.graphs.edge_weighted_graph import EdgeWeightedGraph

    In = InStream(sys.argv[1])
    G = EdgeWeightedGraph.from_stream(In)
    mst = PrimMST(G)
    for e in mst.edges():
        stdio.writeln(e)    
    stdio.writef("%.5f\n", mst.weight())    
