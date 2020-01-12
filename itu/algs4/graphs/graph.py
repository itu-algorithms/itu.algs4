# Created for BADS 2018
# see README.md for details
# This is python3 

from itu.algs4.fundamentals.bag import Bag
from itu.algs4.fundamentals.stack import Stack


class Graph:
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
        g = Graph(V)                # construct this graph
        E = stream.readInt()        # read E    
        if E < 0: raise ValueError("Number of edges in a Graph must be nonnegative")
        for _ in range(E):
            # Add an edge
            v = stream.readInt()    # read a vertex,
            w = stream.readInt()        # read another vertex,
            g._validateVertex(v)
            g._validateVertex(w)
            g.add_edge(v, w)             # and add edge connecting them.
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

    def add_edge(self, v, w):
        """
        Adds the undirected edge v-w to this graph.

        :param v: one vertex in the edge
        :param w: the other vertex in the edge
        :raises ValueError: unless both 0 <= v < V and 0 <= w < V
        """
        self._adj[v].add(w)         # add w to v's list
        self._adj[w].add(v)         # add v to w's list
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

if __name__ == "__main__":
    from itu.algs4.stdlib.instream import InStream
    from itu.algs4.stdlib import stdio
    import sys

    In = InStream(sys.argv[1])
    G = Graph.from_stream(In)
    stdio.writeln(G)
