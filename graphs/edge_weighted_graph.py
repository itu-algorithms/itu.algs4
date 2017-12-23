import sys
from stdlib import stdio
from fundamentals.bag import Bag
from fundamentals.stack import Stack
from graphs.edge import Edge

# Created for BADS 2018
# See README.md for details
# Python 3

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


class EdgeWeightedGraph:
    def __init__(self, V):
        """
        Initializes an empty edge-weighted graph with V vertices and 0 edges.
        :param V: the number of vertices
        :raises ValueError: if V < 0
        """
        if V < 0:
            raise ValueError("Number of vertices must be nonnegative")
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
        """
        self._validate_vertex(v)
        return self._adj[v]

    def V(self):
        """
        Returns the number of vertices in this edge-weighted graph.
        :return: the number of vertices in this edge-weighted graph
        """
        return self._V

    def E(self):
        """
        Returns the number of edges in this edge-weighted graph.
        :return: the number of edges in this edge-weighted graph
        """
        return self._E

    def degree(self, v):
        """
        Returns the degree of vertex v.
        :param v: the vertex
        :return: the degree of vertex v
        :raises ValueError: unless 0 <= v < V
        """
        self._validate_vertex(v)
        return self._adj[v].size()

    def edges(self):
        """
        Returns all edges in this edge-weighted graph.
        :return: all edges in this edge-weighted graph
        """
        _list = Bag()
        for v in range(self._V):
            self_loops = 0
            for e in self.adj(v):
                if e.other(v) > v:
                    _list.add(e)
                elif e.other(v) is v:
                    if self_loops % 2 is 0:
                        _list.add(e)
                    self_loops += 1
        return _list

    def _validate_vertex(self, v):
        """
        Throws a ValueError unless 0 <= v < V.
        :param v: the vertex to be validated
        """
        if v < 0 or v >= self._V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, self._V-1))

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
        sys.stdin = open(sys.argv[1])
        g = EdgeWeightedGraph(stdio.readInt())
        E = stdio.readInt()
        for i in range(E):
            v = stdio.readInt()
            w = stdio.readInt()
            weight = stdio.readFloat()
            e = Edge(v, w, weight)
            g.add_edge(e)
        print(g)


if __name__ == '__main__':
    main()
