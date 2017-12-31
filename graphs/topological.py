# Created for BADS 2018
# See README.md for details
# Python 3
"""
This module implements the topological order algorithm described in 
Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne. For more
information, see chapter 4.2 of the book.
"""

from graphs.directed_cycle import DirectedCycle
from graphs.depth_first_order import DepthFirstOrder

class Topological:
    """
    The Topological class represents a data type for determining a topological
    order of a directed acyclic graph (DAG). Recall, a digraph has a topological 
    order if and only if it is a DAG. The hasOrder operation determines whether 
    the digraph has a topological order, and if so, the order operation returns one.
    
    This implementation uses depth-first search. The constructor takes time 
    proportional to V + E (in the worst case), where V is the number of vertices 
    and E is the number of edges. Afterwards, the hasOrder and rank operations 
    takes constant time; the order operation takes time proportional to V.

    See DirectedCycle, DirectedCycleX, and EdgeWeightedDirectedCycle to compute 
    a directed cycle if the digraph is not a DAG. See TopologicalX for a 
    nonrecursive queue-based algorithm to compute a topological order of a DAG.

    For additional documentation, see Section 4.2 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
    """
    
    def __init__(self, digraph):
        """
        Determines whether the digraph has a topological order and, if so, finds such a topological order.
        
        :param digraph: the Digraph or EdgeWeightedDigraph to check
        """
        self._order = None
        
        finder = DirectedCycle(digraph)

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
    
    def rank(selv, v):
        """
        The the rank of vertex v in the topological order; -1 if the digraph is not a DAG
        
        :param v: the vertex
        :returns: the position of vertex v in a topological order of the digraph; -1 if the digraph is not a DAG
        """
        self._validate_vertex(v)
        if self.has_order():
            return self._rank[v]
        else:
            return -1
    
    # throw an IllegalArgumentException unless {@code 0 <= v < V}
    def _validate_vertex(self, v):
        V = rank.length;
        if v < 0 or v >= V:
            raise ValueError("vertex {} is not between 0 and {}", v, (V-1))

import sys
import instream

from graphs.digraph import Digraph

if __name__ == '__main__':
    # Create stream from file or the standard input,
    # depending on whether a file name was passed.
    stream = sys.argv[1] if len(sys.argv) > 1 else None
    
    d = Digraph.from_stream(instream.InStream(stream))
    top = Topological(d)
    if top.has_order():
        print(list(top.order()))
    else:
        print("Graph is not a DAG")