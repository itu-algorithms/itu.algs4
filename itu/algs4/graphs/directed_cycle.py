# Created for BADS 2018
# See README.md for details
# Python 3

"""
This module implements the directed cycle algorithm described in 
Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne. This version
works for both weighted and unweighted directed graphs, due to Python's duck-typing.

For more
information, see chapter 4.2 of the book.
"""

import sys

from itu.algs4.fundamentals.stack import Stack
from itu.algs4.graphs.digraph import Digraph
from itu.algs4.stdlib.instream import InStream


class DirectedCycle:
    """
    The DirectedCycle class represents a data type for determining whether a 
    digraph has a directed cycle. The hasCycle operation determines whether the 
    digraph has a directed cycle and, and of so, the cycle operation returns one.

    This implementation uses depth-first search. The constructor takes time proportional 
    to V + E (in the worst case), where V is the number of vertices and E is the 
    number of edges. Afterwards, the hasCycle operation takes constant time; the 
    cycle operation takes time proportional to the length of the cycle.

    See Topological to compute a topological order if the digraph is acyclic.

    For additional documentation, see Section 4.2 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
    """    
    
    def __init__(self, digraph):
        """
        Determines whether the digraph has a directed cycle and, if so,
        finds such a cycle.
        
        :digraph: the digraph
        """
        self._cycle = None
        self._on_stack = [False]*digraph.V()
        self._edge_to  = [0]*digraph.V()
        self._marked = [False]*digraph.V()
        for v in range(digraph.V()):
            if not self._marked[v]:
                self._dfs(digraph, v) 
    
    # check that algorithm computes either the topological order or finds a directed cycle
    def _dfs(self, digraph, v):
        self._on_stack[v] = True
        self._marked[v] = True
        for w in digraph.adj(v):
            # short circuit if directed cycle found
            if self.has_cycle():
                return
            # found new vertex, so recur
            elif not self._marked[w]:
                self._edge_to[w] = v
                self._dfs(digraph, w)
            # trace back directed cycle
            elif self._on_stack[w]:
                self._cycle = Stack()
                x = v
                while x != w:
                    self._cycle.push(x)
                    x = self._edge_to[x]
                self._cycle.push(w)
                self._cycle.push(v)
                
        self._on_stack[v] = False
    
    def has_cycle(self):
        """
        Does the digraph have a directed cycle?
        
        :returns: true if there is a cycle, false otherwise
        """
        return self._cycle != None
    
    def cycle(self):
        """
        Returns a directed cycle if the digraph has a directed cycle, and null otherwise.
        
        :returns: a directed cycle (as an iterable) if the digraph has a directed cycle, and null otherwise
        """
        return self._cycle



if __name__ == '__main__':
    # Create stream from file or the standard input,
    # depending on whether a file name was passed.
    stream = sys.argv[1] if len(sys.argv) > 1 else None
    
    d = Digraph.from_stream(InStream(stream))
 
    cyc = DirectedCycle(d)
    print(cyc.cycle())
