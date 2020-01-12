# Created for BADS 2018
# See README.md for details
# Python 3

"""
 *  Execution:    python kosaraju_sharir_scc.py filename.txt
 *  Dependencies: Digraph TransitiveClosure InStream DepthFirstOrder
 *  Data files:   https:#algs4.cs.princeton.edu/42digraph/tinyDG.txt
 *                https:#algs4.cs.princeton.edu/42digraph/mediumDG.txt
 *                https:#algs4.cs.princeton.edu/42digraph/largeDG.txt
 *
 *  Compute the strongly-connected components of a digraph using the
 *  Kosaraju-Sharir algorithm.
 *
 *  Runs in O(E + V) time.
 *
 *  % python kosaraju_sharir_scc.py tinyDG.txt
 *  5 strong components
 *  1 
 *  0 2 3 4 5 
 *  9 10 11 12 
 *  6 8 
 *  7
 *
"""
import sys

from itu.algs4.errors.errors import IllegalArgumentException
from itu.algs4.fundamentals.queue import Queue
from itu.algs4.graphs.depth_first_order import DepthFirstOrder
from itu.algs4.graphs.digraph import Digraph
from itu.algs4.graphs.transitive_closure import TransitiveClosure
from itu.algs4.stdlib.instream import InStream


class KosarajuSharirSCC:

    """
     * Computes the strong components of the digraph G.
     * @param G the digraph
     """
    def __init__(self, G):
        self._marked = [False]*G.V()     # marked[v] = has vertex v been visited?
        self._id = [0]*G.V()             # id[v] = id of strong component containing v
        self._count = 0                  # number of strongly-connected components

        # compute reverse postorder of reverse graph
        dfo = DepthFirstOrder(G.reverse())

        # run DFS on G, using reverse postorder to guide calculation
        for v in dfo.reverse_post():
            if not self._marked[v]:
                self._dfs(G, v)
                self._count+=1

        # check that id[] gives strong components
        assert self._check(G)
    

    # DFS on graph G
    def _dfs(self, G, v): 
        self._marked[v] = True
        self._id[v] = self._count
        for w in G.adj(v):
            if not self._marked[w]:
                self._dfs(G, w)
        
    """
     * Returns the number of strong components.
     * @return the number of strong components
     """
    def count(self):
        return self._count

    """
     * Are vertices v and w in the same strong component?
     * @param  v one vertex
     * @param  w the other vertex
     * @return true if vertices v and w are in the same
     *         strong component, and false otherwise
     * @throws IllegalArgumentException unless 0 <= v < V
     * @throws IllegalArgumentException unless 0 <= w < V
     """
    def strongly_connected(self, v, w):
        self._validate_vertex(v)
        self._validate_vertex(w)
        return self._id[v] == self._id[w]
    

    """
     * Returns the component id of the strong component containing vertex v.
     * @param  v the vertex
     * @return the component id of the strong component containing vertex v
     * @throws IllegalArgumentException unless 0 <= s < V
     """
    def id(self, v):
        self._validate_vertex(v)
        return self._id[v]

    # does the id[] array contain the strongly connected components?
    def _check(self, G):
        tc =  TransitiveClosure(G)
        for v in range(G.V()): 
            for w in range(G.V()):
                if self.strongly_connected(v, w) != (tc.reachable(v, w) and tc.reachable(w, v)):
                    return False
        return True
    

    # throw an IllegalArgumentException unless 0 <= v < V
    def _validate_vertex(self, v):
        V = len(self._marked)
        if v < 0 or v >= V:
            raise IllegalArgumentException("vertex {} is not between 0 and {}".format(v,V-1))
    

def main(args):
    stream =  InStream(args[0])
    G =  Digraph.from_stream(stream)
    scc =  KosarajuSharirSCC(G)

    # number of connected components
    m = scc.count()
    print("{} strong components".format(m))

    # compute list of vertices in each strong component
    components = [Queue() for i in range(m)]
    
    for v in range(G.V()):
        components[scc.id(v)].enqueue(v)
    
    # print results
    for i in range(m):
        for v in components[i]: 
            print(str(v), end=' ')
        print()

if __name__ == '__main__':
    main(sys.argv[1:])
