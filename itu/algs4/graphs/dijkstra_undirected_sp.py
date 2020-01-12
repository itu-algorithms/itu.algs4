import sys

from itu.algs4.errors.errors import IllegalArgumentException
from itu.algs4.fundamentals.stack import Stack
from itu.algs4.graphs.edge_weighted_graph import EdgeWeightedGraph
from itu.algs4.sorting.index_min_pq import IndexMinPQ
from itu.algs4.stdlib.instream import InStream

# Created for BADS 2018
# See README.md for details
# Python 3


class DijkstraUndirectedSP:
    """
    The DijkstraSP class represents a data type for solving the
    single-source shortest paths problem in edge-weighted diagraphs
    where the edge weights are nonnegative.
    This implementation uses Dijkstra's algorithm with a binary heap.
    The constructor takes time proportional to E log V,
    where V is the number of vertices and E is the number of edges.
    Each call to dist_to() and has_path_to() takes constant time
    each call to path_to() takes time proportional to the number of
    edges in the shortest path returned.
    """
    def __init__(self, G, s):
        """
        Computes a shortest-paths tree from the source vertex s to every
        other vertex in the edge-weighted graph G.
        :param G: the edge-weighted graph
        :param s: the source vertex
        :raises IllegalArgumentException: if an edge weight is negative
        :raises IllegalArgumentException: unless 0 <= s < V
        """
        for e in G.edges():
            if e.weight() < 0:
                raise IllegalArgumentException("edge {} has negative weight".format(e))

        self._dist_to = [float('inf')] * G.V()
        self._edge_to = [None] * G.V()
        self._dist_to[s] = 0.0
        self._validate_vertex(s)
        self._pq = IndexMinPQ(G.V())
        self._pq.insert(s, 0)

        while not self._pq.is_empty():
            v = self._pq.del_min()
            for e in G.adj(v):
                self._relax(e, v)

    def dist_to(self, v):
        """
        Returns the length of a shortest path between the source vertex s and
        vertex v.
        :param v: the destination vertex
        :return: the length of a shortest path between the source vertex s and
        the vertex v. float('inf') is not such path
        :rtype: float
        :raises IllegalArgumentException: unless 0 <= v < V
        """
        return self._dist_to[v]

    def has_path_to(self, v):
        """
        Returns true if there is a path between the source vertex s and
        vertex v.
        :param v: the destination vertex
        :return: True if there is a path between the source vertex
        s to vertex v. False otherwise
        :rtype: bool
        """
        return self._dist_to[v] < float('inf')

    def path_to(self, v):
        """
        Returns a shortest path between the source vertex s and vertex v.
        :param v: the destination vertex
        :return: a shortest path between the source vertex s and vertex v.
        None if no such path
        :rtype: collections.iterable[Edge]
        :raises IllegalArgumentException: unless 0 <= v < V
        """
        self._validate_vertex(v)
        if not self.has_path_to(v):
            return None
        path = Stack()
        x = v
        e = self._edge_to[v]
        while e is not None:
            edge = self._edge_to[x]
            path.push(edge)
            x = e.other(x)
            e = self._edge_to[x]
        return path

    def _validate_vertex(self, v):
        """
        Raises an IllegalArgumentException unless 0 <= v < V
        :param v: the vertex to validate
        """
        V = len(self._dist_to)
        if v < 0 or v >= V:
            raise IllegalArgumentException("vertex {} is not between 0 and {}".format(v, V-1))

    def _relax(self, e, v):
        """
        Relax edge e and update pq if changed
        :param e: the edge to relax
        :param v: the vertex e goes out from
        """
        w = e.other(v)
        if self._dist_to[v] + e.weight() < self._dist_to[w]:
            self._dist_to[w] = self._dist_to[v] + e.weight()
            self._edge_to[w] = e
            if self._pq.contains(w):
                self._pq.decrease_key(w, self._dist_to[w])
            else:
                self._pq.insert(w, self._dist_to[w])


def main():
    if len(sys.argv) == 3:
        stream = InStream(sys.argv[1])
        G = EdgeWeightedGraph.from_stream(stream)
        s = int(sys.argv[2])
        sp = DijkstraUndirectedSP(G, s)

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
