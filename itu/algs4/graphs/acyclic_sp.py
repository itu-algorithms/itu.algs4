# Created for BADS 2018
# see README.md for details
# This is python3 

import math

from itu.algs4.fundamentals.stack import Stack
from itu.algs4.graphs.topological import Topological


class AcyclicSP:
    """
    The AcyclicSP class represents a data type for solving the
    single-source shortest paths problem in edge-weighted directed acyclic
    graphs (DAGs). The edge weights can be positive, negative, or zero.

    This implementation uses a topological-sort based algorithm.
    The constructor takes time proportional to V + E,
    where V is the number of vertices and E is the number of edges.
    Each call to distTo(int) and has_path_to(int) takes constant time
    each call to pathTo(int) takes time proportional to the number of
    edges in the shortest path returned.
    """

    def __init__(self, G, s):
        """
        Computes a shortest paths tree from s to every other vertex in
        the directed acyclic graph G.
        :param G: the acyclic digraph
        :param s: the source vertex
        :raises ValueError: if the digraph is not acyclic
        :raises ValueError: unless 0 <= s < V
        """
        self._dist_to = [0] * G.V()         # _dist_to[v] = distance  of shortest s->v path
        self._edge_to = [None] * G.V()      # _edge_to[v] = last edge on shortest s->v path

        self._validate_vertex(s)

        for v in range(G.V()):
            self._dist_to[v] = math.inf
        self._dist_to[s] = 0.0

        # visit vertices in toplogical order
        topological = Topological(G)
        if not topological.has_order():
            raise ValueError("Digraph is not acyclic.")

        for v in topological.order():
            for e in G.adj(v):
                self._relax(e)
                
    def _relax(self, e):
        v = e.from_vertex()
        w = e.to_vertex()

        if self._dist_to[w] > self._dist_to[v] + e.weight():
            self._dist_to[w] = self._dist_to[v] + e.weight()
            self._edge_to[w] = e
        
    def dist_to(self, v):
        """
        Returns the length of a shortest path from the source vertex s to vertex v.
        :param v: the destination vertex
        :returns: the length of a shortest path from the source vertex s to vertex v
                math.inf if no such path
        :raises ValueError: unless 0 <= v < V
        """
        self._validate_vertex(v)
        return self._dist_to[v]
    
    
    def has_path_to(self, v):
        """
        Is there a path from the source vertex s to vertex v?
        :param v: the destination vertex
        :returns: true if there is a path from the source vertex
                s to vertex v, and false otherwise
        :raises ValueError: unless 0 <= v < V
        """
        self._validate_vertex(v)
        return self._dist_to[v] < math.inf
    
    def path_to(self, v):
        """
        Returns a shortest path from the source vertex s to vertex v.
        :param v: the destination vertex
        :returns: a shortest path from the source vertex s to vertex v
                as an iterable of edges, and None if no such path
        :raises ValueError: unless 0 <= v < V
        """
        self._validate_vertex(v)
        if not self.has_path_to(v): return None
        path =  Stack()
        e = self._edge_to[v]
        while e is not None:
            path.push(e)
            e = self._edge_to[e.from_vertex()]        
        return path
    
    def _validate_vertex(self, v):
        # raise an ValueError unless 0 <= v < V
        V = len(self._dist_to)
        if v < 0 or v >= V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, V-1))

if __name__ == "__main__":
    import sys
    from itu.algs4.stdlib.instream import InStream
    from itu.algs4.stdlib import stdio
    from itu.algs4.graphs.edge_weighted_digraph import EdgeWeightedDigraph

    In = InStream(sys.argv[1])
    s = int(sys.argv[2])
    G = EdgeWeightedDigraph.from_stream(In)

    # find shortest path from s to each other vertex in DAG
    sp = AcyclicSP(G, s)
    for v in range(G.V()):
        if sp.has_path_to(v):
            stdio.writef("%d to %d (%.2f)  ", s, v, sp.dist_to(v))
            for e in sp.path_to(v):
                stdio.writef("%s\t", e.__repr__())
            stdio.writeln()
        else:
            stdio.writef("%d to %d no path\n", s, v)
