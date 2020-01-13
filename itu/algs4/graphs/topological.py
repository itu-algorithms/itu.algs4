# Created for BADS 2018
# See README.md for details
# Python 3
"""
This module implements the topological order algorithm described in 
Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne. For more
information, see chapter 4.2 of the book.
"""

from itu.algs4.graphs.depth_first_order import DepthFirstOrder
from itu.algs4.graphs.digraph import Digraph
from itu.algs4.graphs.directed_cycle import DirectedCycle
from itu.algs4.graphs.edge_weighted_directed_cycle import EdgeWeightedDirectedCycle


class Topological:
    """
    The Topological class represents a data type for determining a topological
    order of a directed acyclic graph (DAG). Recall, a digraph has a topological 
    order if and only if it is a DAG. The hasOrder operation determines whether 
    the digraph has a topological order, and if so, the order operation returns one.
    
    This implementation uses depth-first search. The constructor takes time 
    proportional to V + E (in the worst case), where V is the number of vertices 
    and E is the number of edges. Afterwards, the hasOrder and rank operations 
    takes constant time the order operation takes time proportional to V.

    See DirectedCycle, DirectedCycleX, and EdgeWeightedDirectedCycle to compute 
    a directed cycle if the digraph is not a DAG. See TopologicalX for a 
    nonrecursive queue-based algorithm to compute a topological order of a DAG.

    For additional documentation, see Section 4.2 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
    """
    
    def __init__(self, digraph):
        """
        Determines whether the digraph (or edge weighted digraph) 
        has a topological order and, if so, finds such a topological order.
        
        :param digraph: the Digraph or EdgeWeightedDigraph to check
        """
        self._order = None
        
        if isinstance(digraph, Digraph):
            finder = DirectedCycle(digraph)
        else:
            finder = EdgeWeightedDirectedCycle(digraph)

        if not finder.has_cycle():
            dfs = DepthFirstOrder(digraph)
            self._order = dfs.reverse_post()
            self._rank = [0]*digraph.V()
            i = 0
            for v in self._order:
                self._rank[v] = i
                i += 1
    
    def order(self):
        """
        Returns a topological order if the digraph has a topologial order, and None otherwise.
        
        :returns: a topological order of the vertices (as an interable) if the digraph has a 
                 topological order (or equivalently, if the digraph is a DAG), and None otherwise
        """
        return self._order
    
    def has_order(self):
        """
        Does the digraph have a topological order?
        
        :returns: True if the digraph has a topological order (or equivalently, if the digraph 
                 is a DAG), and False otherwise
        """
        return self._order != None
    
    def rank(self, v):
        """
        The the rank of vertex v in the topological order -1 if the digraph is not a DAG
        
        :param v: the vertex
        :returns: the position of vertex v in a topological order of the digraph -1 if the digraph is not a DAG
        """
        self._validate_vertex(v)
        if self.has_order():
            return self._rank[v]
        else:
            return -1
    
    def _validate_vertex(self, v):
        # throw an IllegalArgumentException unless 0 <= v < V        
        V = len(self._rank)
        if v < 0 or v >= V:
            raise ValueError("vertex {} is not between 0 and {}", v, (V-1))


if __name__ == '__main__':
    import sys
    from itu.algs4.stdio.instream import InStream
    from itu.algs4.stdlib import stdio
    from itu.algs4.graphs.symbol_digraph import SymbolDigraph

    filename  = sys.argv[1]
    delimiter = sys.argv[2]
    sg = SymbolDigraph(filename, delimiter)
    topological = Topological(sg.digraph())
    for v in topological.order():
        stdio.writeln(sg.name_of(v))
