# Created for BADS 2018
# See README.md for details
# Python 3

"""
This module implements the digraph related algorithms described in 
Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne. For more
information, see chapter 4.2 of the book.
"""

import instream

from fundamentals.bag import Bag
from fundamentals.stack import Stack
from fundamentals.queue import Queue

class Digraph:
    """
    The Graph class represents an undirected graph of vertices
    named 0 through V - 1.
    It supports the following two primary operations: add an edge to the graph,
    iterate over all of the vertices adjacent to a vertex. It also provides
    methods for returning the number of vertices V and the number
    of edges E. Parallel edges and self-loops are permitted.
    By convention, a self-loop v-v appears in the
    adjacency list of v twice and contributes two to the degree
    of v.

    This implementation uses an adjacency-lists representation, which 
    is a vertex-indexed array of Bag objects.
    All operations take constant time (in the worst case) except
    iterating over the vertices adjacent to a given vertex, which takes
    time proportional to the number of such vertices.
    """
    def __init__(self, V):
        """
        Initializes an empty graph with V vertices and 0 edges.
        param V the number of vertices

        :param V: number of vertices
        :raises: ValueError if V < 0
        """
        if V < 0: raise ValueError("Number of vertices must be nonnegative")
        self._V = V     # number of vertices
        self._E = 0     # number of edges
        self._adj = []  # adjacency lists

        for _ in range(V):
            self._adj.append(Bag()) # Initialize all lists to empty bags.

    @staticmethod
    def from_stream(stream):
        """
        Initializes a graph from the specified input stream.
        The format is the number of vertices V,
        followed by the number of edges E,
        followed by E pairs of vertices, with each entry separated by whitespace.
      
        :param stream: the input stream
        :returns: new graph from stream
        :raises ValueError: if the endpoints of any edge are not in prescribed range
        :raises ValueError: if the number of vertices or edges is negative
        :raises ValueError: if the input stream is in the wrong format 
        """
        V = stream.readInt()        # read V
        if V < 0: raise ValueError("Number of vertices must be nonnegative")
        g = Digraph(V)                # construct this graph
        E = stream.readInt()        # read E    
        if E < 0: raise ValueError("Number of edges in a Graph must be nonnegative")
        for _ in range(E):
            # Add an edge
            v = stream.readInt()    # read a vertex,
            w = stream.readInt()        # read another vertex,
            g._validateVertex(v)
            g._validateVertex(w)
            g.addEdge(v, w)             # and add edge connecting them.
        return g

    @staticmethod
    def from_graph(G):
        """
        Initializes a new graph that is a deep copy of G

        :param G: the graph to copy
        :returns: copy of G 
        """
        g = Graph(G.V())
        g._E = G.E()
        for v in range(G.V()):
            # reverse so that adjacency list is in same order as original
            reverse = Stack()
            for w in G._adj[v]:
                reverse.push(w)
            for w in reverse:
                g._adj[v].add(w)

    def V(self):
        """
        Returns the number of vertices in this graph.

        :returns: the number of vertices in this graph.
        """
        return self._V

    def E(self):
        """
        Returns the number of edges in this graph.

        :returns: the number of edges in this graph.
        """
        return self._E

    def _validateVertex(self, v):
        # throw a ValueError unless 0 <= v < V
        if v < 0 or v >= self._V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, self._V))

    def addEdge(self, v, w):
        """
        Adds the undirected edge v-w to this graph.

        :param v: one vertex in the edge
        :param w: the other vertex in the edge
        :raises ValueError: unless both 0 <= v < V and 0 <= w < V
        """
        self._adj[v].add(w)         # add w to v's list
        self._E += 1

    def adj(self, v):
        """
        Returns the vertices adjacent to vertex v.
     
        :param v: the vertex
        :returns: the vertices adjacent to vertex v, as an iterable
        :raises ValueError: unless  0 <= v < V
        """
        self._validateVertex(v)        
        return self._adj[v]

    def degree(self, v):
        """
        Returns the degree of vertex v.
     
        :param v: the vertex
        :returns: the degree of vertex v
        :raises ValueError:  unless 0 <= v < V
        """
        self._validateVertex(v)
        return self._adj[v].size()
    
    def reverse(self):
        """
        Returns the reverse of the digraph.
        
        :returns: the reverse of the digraph
        """
        rev = Digraph(self._V)
        for v in range(selv._V):
            for w in adj(v):
                rev.addEdge(w, v)
        return rev

    def __repr__(self):
        """
        Returns a string representation of this graph.
     
        :returns: the number of vertices V, followed by the number of edges E,
                    followed by the V adjacency lists
        """
        s = ["{} vertices, {} edges\n".format(self._V, self._E)]
        for v in range(self._V):
            s.append("%d : " % (v))
            for w in self._adj[v]:
                s.append("%d " % (w))
            s.append("\n")

        return ''.join(s)


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
        Determines whether the digraph G has a topological order and, if so, finds such a topological order.
        
        :param digraph: the digraph to check
        """
        finder = DirectedCycle(digraph)
        
    
    
import sys

if __name__ == '__main__':
    # Create stream from file or the standard input,
    # depending on whether a file name was passed.
    stream = sys.argv[1] if len(sys.argv) > 1 else None
    
    d = Digraph.from_stream(instream.InStream(stream))
    print(d)
    cyc = DirectedCycle(d)
    print(list(cyc.cycle()))
    