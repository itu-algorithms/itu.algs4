# Created for BADS 2018
# See README.md for details
# Python 3

import sys

from itu.algs4.fundamentals.stack import Stack
from itu.algs4.graphs.directed_edge import DirectedEdge
from itu.algs4.graphs.edge_weighted_digraph import EdgeWeightedDigraph
from itu.algs4.graphs.topological import Topological
from itu.algs4.stdlib import instream


"""
This module implements a class for solving the single-source Longest
paths problem in edge-weighted directed acyclic graphs (DAGs), described in 
Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne. 

For more information, see chapter 4.2 of the book.
"""

class AcyclicLp:
    """
    The AcyclicLP class represents a data type for solving the single-source longest 
    paths problem in edge-weighted directed acyclic graphs (DAGs). The edge weights 
    can be positive, negative, or zero.
    
    This implementation uses a topological-sort based algorithm. The constructor takes 
    time proportional to V + E, where V is the number of vertices and E is the number of edges. 
    Each call to distTo(int) and hasPathTo(int) takes constant time; each call to pathTo(int) 
    takes time proportional to the number of edges in the shortest path returned.

    For additional documentation, see Section 4.4 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
    """
    
    def __init__(self, edge_weighted_digraph, s):
        """
        Computes a longest paths tree from s to every other vertex in the directed acyclic graph G.
        
        :param edge_weighted_digraph: the acyclic digraph
        :param s: the source vertex
        """
        graph = edge_weighted_digraph
        self._dist_to = [float("-inf")]*graph.V()
        self._edge_to = [None]*graph.V()
        
        self._validate_vertex(s)
        
        self._dist_to[s] = 0.
        
        # relax vertices in topological order
        topological = Topological(graph)
        if not topological.has_order():
            print(graph)
            raise ValueError('Digraph is not acyclic.')
        
        for v in topological.order():
            for edge in graph.adj(v):
                self._relax(edge)
                
    def dist_to(self, v):
        """
        Returns the length of a longest path from the source vertex s to vertex v.
        
        :param v: the destination vertex
        
        :returns: the length of a longest path from the source vertex s to vertex v; 
                  negative infinity if no such path exists
        """
        self._validate_vertex(v)
        return self._dist_to[v]
    
    def has_path_to(self, v):
        """
        Is there a path from the source vertex s to vertex v?
        """
        return self.dist_to(v) > float("-inf")
    
    def path_to(self, v):
        """
        Returns a longest path from the source vertex s to vertex v.
        
        :param: the destination vertex
        :returns: a longest path from the source vertex s to vertex v as an iterable of edges, and None if no such path
        """
        self._validate_vertex(v)
        if not self.has_path_to(v):
            return None
        path = Stack()
        edge = self._edge_to[v]
        while not edge is None:
            path.push(edge)
            edge = self._edge_to[edge.from_vertex()]
        return path
        
                
    # relax edge e, but update if you find a *longer* path 
    def _relax(self, edge):
        v, w = edge.from_vertex(), edge.to_vertex()
        if self._dist_to[w] < self._dist_to[v] + edge.weight():
            self._dist_to[w] = self._dist_to[v] + edge.weight()
            self._edge_to[w] = edge
        
    # throw an IllegalArgumentException unless 0 <= v < V
    def _validate_vertex(self, v):
        V = len(self._dist_to)
        if not (0 <= v < V):
            raise ValueError('vertex {} is not between 0 and {}'.format(v, V-1))



if __name__ == '__main__':
    # Create stream from file or the standard input,
    # depending on whether a file name was passed.
    stream = sys.argv[1] if len(sys.argv) > 1 else None
    d = EdgeWeightedDigraph.from_stream(instream.InStream(stream))
    a = AcyclicLp(d, 3)
    
    # print longest paths to all other vertices
    for i in range(d.V()):
        print('{} to {}'.format(i, a.path_to(i)))
