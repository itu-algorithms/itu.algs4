import sys

from itu.algs4.errors.errors import IllegalArgumentException
from itu.algs4.fundamentals.bag import Bag
from itu.algs4.fundamentals.stack import Stack
from itu.algs4.graphs.edge import Edge
from itu.algs4.stdlib.instream import InStream

# Created for BADS 2018
# See README.md for details
# Python 3


class EdgeWeightedGraph:
    """
    The EdgeWeightedGraph class represents an edge-weighted
    graph of vertices named 0 through V-1, where each
    undirected edge is of type Edge and has a real-valued weight.
    It supports the following two primary operations: add an edge to the graph,
    iterate over all of the edges incident to a vertex. It also provides
    methods for returning the number of vertices V and the number
    of edges E. Parallel edges and self-loops are permitted.
    By convention, a self-loop v-v appears in the adjacency list of v twice and contributes two to the degree
    of v.
    This implementation uses an adjacency-list representation, which
    is a vertex-indexed array of Bag objects.
    All operations take constant time (in the worst case) except
    iterating over the edges incident to a given vertex, which takes
    time proportional to the number of such edges.
    """
    def __init__(self, V):
        """
        Initializes an empty edge-weighted graph with V vertices and 0 edges.
        :param V: the number of vertices
        :raises IllegalArgumentException: if V < 0
        """
        if V < 0:
            raise IllegalArgumentException("Number of vertices must be nonnegative")
        self._V = V
        self._E = 0
        self._adj = [None] * V
        for v in range(V):
            self._adj[v] = Bag()

    @staticmethod
    def from_graph(G):
        """
        Initializes a new edge-weighted graph that is a deep copy of G.
        :param G: the edge-weighted graph to copy
        :return: the copy of the graph edge-weighted graph G
        :rtype: EdgeWeightedGraph
        """
        g = EdgeWeightedGraph(G.V())
        g._E = G.E()
        for v in range(G.V()):
            reverse = Stack()
            for e in G.adj(v):
                reverse.push(e)
            for e in reverse:
                g._adj[v].add(e)
        return g

    @staticmethod
    def from_stream(stream):
        """
        Initializes an edge-weighted graph from an input stream.
        The format is the number of vertices V,
        followed by the number of edges E,
        followed by E pairs of vertices and edge weights,
        with each entry separated by whitespace.
        :param stream: the input stream
        :raises IllegalArgumentException: if the endpoints of any edge are not in prescribed range
        :raises IllegalArgumentException: if the number of vertices or edges is negative
        :return: the edge-weighted graph
        :rtype: EdgeWeightedGraph
        """
        g = EdgeWeightedGraph(stream.readInt())
        E = stream.readInt()
        if E < 0:
            raise IllegalArgumentException("Number of edges must be nonnegative")
        for i in range(E):
            v = stream.readInt()
            w = stream.readInt()
            g._validate_vertex(v)
            g._validate_vertex(w)
            weight = stream.readFloat()
            e = Edge(v, w, weight)
            g.add_edge(e)
        return g

    def add_edge(self, e):
        """
        Adds the undirected edge e to this edge-weighted graph.
        :param e: the edge
        """
        v = e.either()
        w = e.other(v)
        self._validate_vertex(v)
        self._validate_vertex(w)
        self._adj[v].add(e)
        self._adj[w].add(e)
        self._E += 1

    def adj(self, v):
        """
        Returns the edges incident on vertex v.
        :param v: the vertex
        :return: the edges incident on vertex v
        :rtype: collections.iterable[Edge]
        """
        self._validate_vertex(v)
        return self._adj[v]

    def V(self):
        """
        Returns the number of vertices in this edge-weighted graph.
        :return: the number of vertices in this edge-weighted graph
        :rtype: int
        """
        return self._V

    def E(self):
        """
        Returns the number of edges in this edge-weighted graph.
        :return: the number of edges in this edge-weighted graph
        :rtype: int
        """
        return self._E

    def degree(self, v):
        """
        Returns the degree of vertex v.
        :param v: the vertex
        :return: the degree of vertex v
        :rtype: int
        :raises IllegalArgumentException: unless 0 <= v < V
        """
        self._validate_vertex(v)
        return self._adj[v].size()

    def edges(self):
        """
        Returns all edges in this edge-weighted graph.
        :return: all edges in this edge-weighted graph
        """
        edges = Bag()
        for v in range(self._V):
            self_loops = 0
            for e in self.adj(v):
                if e.other(v) > v:
                    edges.add(e)
                elif e.other(v) is v:
                    if self_loops % 2 is 0:
                        edges.add(e)
                    self_loops += 1
        return edges

    def _validate_vertex(self, v):
        """
        Raises an IllegalArgumentException unless 0 <= v < V.
        :param v: the vertex to be validated
        """
        if v < 0 or v >= self._V:
            raise IllegalArgumentException("vertex {} is not between 0 and {}".format(v, self._V-1))

    def __repr__(self):
        """
        Returns a string representation of the edge-weighted graph.
        This method takes time proportional to E + V.
        :return: the number of vertices, followed by the number of edges,
        followed by the V adjacency lists of edges
        """
        s = ["{} {} \n".format(self._V, self._E)]
        for v in range(self._V):
            s.append("{}: ".format(v))
            for e in self._adj[v]:
                s.append("{}: ".format(e))
            s.append("\n")
        return ''.join(s)


def main():
    """
    Creates an edge-weighted graph from the given input file and prints it.
    """
    if len(sys.argv) > 1:
        stream = InStream(sys.argv[1])
        G = EdgeWeightedGraph.from_stream(stream)
        print(G)


if __name__ == '__main__':
    main()
