import sys

from itu.algs4.errors.errors import IllegalArgumentException
from itu.algs4.fundamentals.stack import Stack
from itu.algs4.graphs.edge_weighted_digraph import EdgeWeightedDigraph
from itu.algs4.sorting.index_min_pq import IndexMinPQ
from itu.algs4.stdlib.instream import InStream

# Created for BADS 2018
# See README.md for details
# Python 3


class DijkstraSP:
    """
    The DijkstraSP class represents a data type for solving the
    single-source shortest paths problem in edge-weighted digraphs
    where the edge weights are nonnegative.
    This implementation uses Dijkstra's algorithm with a binary heap.
    The constructor takes time proportional to E log V,
    where V is the number of vertices and E is the number of edges.
    Each call to dist_to() and has_path_to() takes constant time.
    Each call to path_to() takes time proportional to the number of
    edges in the shortest path returned.
    """
    def __init__(self, G, s):
        """
        Computes a shortest-paths tree from the source vertex s to every other
        vertex in the edge-weighted digraph G.
        :param G: The edge-weighted digraph
        :param s: The source vertex
        :raises IllegalArgumentException: if an edge weight is negative
        :raises IllegalArgumentException: unless 0 <= s < V
        """
        for e in G.edges():
            if e.weight() < 0:
                raise IllegalArgumentException("edge {} has negative weight".format(e))
        self._dist_to = [float('inf')] * G.V()
        self._edge_to = [None] * G.V()
        self._validate_vertex(s)
        self._dist_to[s] = 0.0
        self._pq = IndexMinPQ(G.V())
        self._pq.insert(s, 0.0)
        while not self._pq.is_empty():
            v = self._pq.del_min()
            for e in G.adj(v):
                self._relax(e)

    def dist_to(self, v):
        """
        Returns the length of a shortest path from the source vertex s to vertex v.
        :param v: the destination vertex
        :return: the length of a shortest path from the source vertex s to vertex v
        :rtype: float
        :raises IllegalArgumentException: unless 0 <= v < V
        """
        self._validate_vertex(v)
        return self._dist_to[v]

    def has_path_to(self, v):
        """
        Returns True if there is a ath from the source vertex s to vertex v.
        :param v: the destination vertex
        :return: True if there is a path from the source vertex
        s to vertex v. Otherwise returns False
        :rtype: bool
        :raises IllegalArgumentException: unless 0 <= v < V
        """
        self._validate_vertex(v)
        return self._dist_to[v] < float('inf')

    def path_to(self, v):
        """
        Returns a shortest path from the source vertex s to vertex v.
        :param v: the destination vertex
        :return: a shortest path from the source vertex s to vertex v
        :rtype: collections.iterable[DirectedEdge]
        :raises IllegalArgumentException: unless 0 <= v < V
        """
        self._validate_vertex(v)
        if not self.has_path_to(v):
            return None
        path = Stack()
        e = self._edge_to[v]
        while e is not None:
            path.push(e)
            e = self._edge_to[e.from_vertex()]
        return path

    def _relax(self, e):
        """
        Relaxes the edge e and updates the pq if changed.
        :param e: the edge to relax
        """
        v = e.from_vertex()
        w = e.to_vertex()
        if self._dist_to[w] > self._dist_to[v] + e.weight():
            self._dist_to[w] = self._dist_to[v] + e.weight()
            self._edge_to[w] = e
            if self._pq.contains(w):
                self._pq.decrease_key(w, self._dist_to[w])
            else:
                self._pq.insert(w, self._dist_to[w])

    def _validate_vertex(self, v):
        """
        Raises an IllegalArgumentException unless 0 <= v < V
        :param v: the vertex to be validated
        """
        V = len(self._dist_to)
        if v < 0 or v >= V:
            raise IllegalArgumentException("vertex {} is not between 0 and {}".format(v, V-1))


def main():
    """
    Creates an EdgeWeightedDigraph from input file.
    Runs DijkstraSP on the graph with the given source vertex.
    Prints the shortest path from the source vertex to all other vertices.
    """
    if len(sys.argv) == 3:
        stream = InStream(sys.argv[1])
        G = EdgeWeightedDigraph.from_stream(stream)
        s = int(sys.argv[2])
        sp = DijkstraSP(G, s)
        for t in range(G.V()):
            if sp.has_path_to(t):
                print("{} to {} ({:.2f})  ".format(s, t, sp.dist_to(t)), end='')
                for e in sp.path_to(t):
                    print(e, end='   ')
                print()
            else:
                print("{} to {}         no path\n".format(s, t))


if __name__ == '__main__':
    main()
