import sys

from itu.algs4.errors.errors import IllegalArgumentException
from itu.algs4.fundamentals.bag import Bag
from itu.algs4.fundamentals.stack import Stack
from itu.algs4.graphs.directed_edge import DirectedEdge
from itu.algs4.stdlib.instream import InStream

# Created for BADS 2018
# See README.md for details
# Python 3


class EdgeWeightedDigraph:
    """
    The EdgeWeightedDigraph class represents an edge-weighted
    digraph of vertices named 0 through V-1, where each
    directed edge is of type DirectedEdge and has a real-valued weight.
    It supports the following two primary operations: add a directed edge
    to the digraph and iterate over all edges incident from a given vertex.
    it also provides methods for returning the number of vertices V
    and the number of edges E. Parallel edges and self-loops are permitted.
    This implementation uses an adjacency-lists representation, which
    is a vertex-indexed array of Bag objects.
    All operations take constant time (in the worst case) except
    iterating over the edges incident from a given vertex, which takes
    time proportional to the number of such edges.
    """
    def __init__(self, V):
        """
        Initializes an empty edge-weighted digraph with V vertices and 0 edges.
        :param V: the number of vertices
        :raises IllegalArgumentException: if V < 0
        """
        if V < 0:
            raise IllegalArgumentException("Number of vertices in a Digraph must be nonnegative")
        self._V = V
        self._E = 0
        self._indegree = [0] * V
        self._adj = [None] * V
        for v in range(V):
            self._adj[v] = Bag()

    @staticmethod
    def from_graph(G):
        """
        Initializes a new edge-weighted digraph that is a deep copy of G.
        :param G: the edge-weighted digraph to copy
        :return: a copy of graph G
        :rtype: EdgeWeightedDigraph
        """
        g = EdgeWeightedDigraph(G.V())
        g._E = G.E()
        for v in range(G.V()):
            g._indegree[v] = G.indegree(v)
            reverse = Stack()
            for e in G.adj(v):
                reverse.push(e)
            for e in reverse:
                g._adj[v].add(e)
        return g

    @staticmethod
    def from_stream(stream):
        """
        Initializes an edge-weighted digraph from the specified input stream.
        The format is the number of vertices V,
        followed by the number of edges E,
        followed by E pairs of vertices and edge weights,
        with each entry seperated by whitespace
        :param stream: the input stream

        :raises IllegalArgumentException: if the endpoints of any edge are not in prescribed range
        :raises IllegalArgumentException: if the number of vertices or edges is negative
        :return: the edge-weighted digraph
        :rtype: EdgeWeightedDigraph
        """
        g = EdgeWeightedDigraph(stream.readInt())
        E = stream.readInt()
        if g._E < 0:
            raise IllegalArgumentException("Number of edges must be nonnegative")
        for i in range(E):
            v = stream.readInt()
            w = stream.readInt()
            g._validate_vertex(v)
            g._validate_vertex(w)
            weight = stream.readFloat()
            g.add_edge(DirectedEdge(v, w, weight))
        return g

    def V(self):
        """
        Returns the number of vertices in this edge-weighted digraph.
        :return: the number of vertices in this edge-weighted digraph
        :rtype: int
        """
        return self._V

    def E(self):
        """
        Returns the number of edges in this edge-weighted digraph.
        :return: the number of edges in this edge-weighted digraph
        :rtype: int
        """
        return self._E

    def _validate_vertex(self, v):
        """
        Raises an IllegalArgumentException unluess 0 <= v < V
        :param v: the vertex to validate
        """
        if v < 0 or v >= self._V:
            raise IllegalArgumentException("vertex {} is not between 0 and {}".format(v, self._V-1))

    def add_edge(self, e):
        """
        Adds the directed edge e to this edge-weighted digraph.
        :param e: the edge
        :raises IllegalArgumentException: unless endpoints of edge are between 0 and V-1
        """
        v = e.from_vertex()
        w = e.to_vertex()
        self._validate_vertex(v)
        self._validate_vertex(w)
        self._adj[v].add(e)
        self._indegree[w] += 1
        self._E += 1

    def adj(self, v):
        """
        Returns the directed edges incident from vertex v.
        :param v: the vertex
        :return: the directed edges incident from vertex v.
        :rtype: collections.iterable[DirectedEdge]
        :raises IllegalArgumentException: unless 0 <= v < V
        """
        self._validate_vertex(v)
        return self._adj[v]

    def outdegree(self, v):
        """
        Returns the number of directed edges incident from vertex v.
        This is known as the outdegree of vertex v.
        :param v: the vertex
        :return: the outdegree of vertex v
        :rtype: int
        :raises IllegalArgumentException: unless 0 <= v < V
        """
        self._validate_vertex(v)
        return self._adj[v].size()

    def indegree(self, v):
        """
        Returns the number of directed edges incident to vertex v.
        This is known as the indegree of vertex v.
        :param v: the vertex
        :return: the indegree of vertex v
        :rtype: int
        :raises IllegalArgumentException: unless 0 <= v < V
        """
        self._validate_vertex(v)
        return self._indegree[v]

    def edges(self):
        """
        Returns all directed edges in this edge-weighted digraph.
        :return: all edges in this edge-weighted digraph
        :rtype: collections.iterable[DirectedEdge]
        """
        edges = Bag()
        for v in range(self._V):
            for e in self._adj[v]:
                edges.add(e)
        return edges

    def __repr__(self):
        """
        Returns a string representation of this edge-weighted digraph.
        :return: the number of vertices V, followed by the number of edges E,
        followed by the V adjacency lists of edges.
        :rtype: str
        """
        s = ["{} {} \n".format(self._V, self._E)]
        for v in range(self._V):
            s.append("{}: ".format(v))
            for e in self._adj[v]:
                s.append("{}  ".format(e))
            s.append("\n")
        return ''.join(s)


def main():
    """
    Creates an edge-weighted digraph from the given input file and prints it.
    """
    if len(sys.argv) > 1:
        stream = InStream(sys.argv[1])
        G = EdgeWeightedDigraph.from_stream(stream)
        print(G)


if __name__ == '__main__':
    main()
