# Created for BADS 2018
# See README.md for details
# Python 3


"""
This module implements a data type for solving the all-pairs shortest 
paths problem in edge-weighted digraphs where the edge weights are nonnegative.
"""

import sys

from itu.algs4.graphs.dijkstra_sp import DijkstraSP
from itu.algs4.graphs.edge_weighted_digraph import EdgeWeightedDigraph
from itu.algs4.stdlib import instream


class DijkstraAllPairsSP:
    """
    This implementation runs Dijkstra's algorithm from each vertex. The constructor 
    takes time proportional to V (E log V) and uses space proprtional to V2, where 
    V is the number of vertices and E is the number of edges. Afterwards, the dist() 
    and hasPath() methods take constant time and the path() method takes time 
    proportional to the number of edges in the shortest path returned.

    For additional documentation, see Section 4.4 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
    """
    
    def __init__(self, edge_weighted_digraph):
        """
        Computes a shortest paths tree from each vertex to to every other vertex in the edge-weighted digraph G.
        
        :param edge_weighted_digraph: the edge-weighted digraph
        """
        self._all = []
        for v in range(edge_weighted_digraph.V()):
            self._all.append(DijkstraSP(edge_weighted_digraph, v))
        
    def path(self, source, target):
        """
        Returns a shortest path from source vertex to the target vertex.
        
        :param source: the source vertex
        :param target: the destination vertex
        
        :returns: a shortest path from the source vertex to the target vertex as an iterable of edges, 
                  and None if no such path
        """
        self._validateVertex(source)
        self._validateVertex(target)
        
        return self._all[source].path_to(target)
    
    def has_path(self, source, target):
        """
        Is there a path from the source vertex to the target vertex?
        
        :param source: the source vertex
        :param target: the target vertex
        
        :returns: True if there is a path from the source to the target, and False otherwise
        """
        return self.dist(source, target) < float('inf')
    
    def dist(self, source, target):
        """
        Returns the length of a shortest path from the source vertex to the target vertex.
        
        :param source: the source vertex
        :param target: the target vertex
        
        :returns: the length of a shortest path from the source vertex to the target vertex; 
                  float('inf') if no such path
        """
        self._validateVertex(source)
        self._validateVertex(target)   
        
        return self._all[source].dist_to(target)
    
    # throw a ValueError unless 0 <= v < V
    def _validateVertex(self, v):
        V = len(self._all)
        if v < 0 or v >= V:
            raise ValueError('vertex {} is not between 0 and {}'.format(v, (V-1)))


if __name__ == '__main__':
    # Create stream from file or the standard input,
    # depending on whether a file name was passed.
    stream = sys.argv[1] if len(sys.argv) > 1 else None
    
    # Create a DijkstraAllPairsSP data structure
    g = EdgeWeightedDigraph.from_stream(instream.InStream(stream))
    dijkstra_all = DijkstraAllPairsSP(g)
    
    # Print the shortest path distances between all possible pairs of vertices.
    for source in range(g.V()):
        for target in range(g.V()):
            print(dijkstra_all.dist(source, target))
