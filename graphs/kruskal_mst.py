import sys
from stdlib import stdio
from fundamentals.queue import Queue
from sorting.min_pq import MinPQ
from fundamentals.uf import WeightedQuickUnionUF
from graphs.edge import Edge
from graphs.edge_weighted_graph import EdgeWeightedGraph

# Created for BADS 2018
# See README.md for details
# Python 3


class KruskalMST:
    """
    The KruskalMST class represents a data type for computing a
    minimum spanning tree in an edge-weighted graph.
    The edge weights can be positive, zero, or negative and need not
    be distinct. If the graph is not connected, it computes a minimum
    spanning forest, which is the union of minimum spanning trees
    in each connected component. The weight method returns the
    weight of a minimum spanning tree and the edges method
    returns its edges.
    This implementation uses Kruskal's algorithm and the
    union-find data type.
    The constructor takes time proportional to E log E
    and extra space (not including the graph) proportional to V,
    where V is the number of vertices and E is the number of edges-
    Afterwards, the weight method takes constant time
    and the edges method takes time proportional to V.
    """
    def __init__(self, G):
        """
        Computes a minimum spanning tree (or forest) of an edge-weighted graph.
        :param G: the edge-weighted graph
        """
        self._weight = 0
        self._mst = Queue()
        pq = MinPQ()

        for e in G.edges():
            pq.insert(e)

        uf = WeightedQuickUnionUF(G.V())
        while not pq.is_empty() and self._mst.size() < G.V() - 1:
            e = pq.del_min()
            v = e.either()
            w = e.other(v)
            if not uf.connected(v, w):
                uf.union(v, w)
                self._mst.enqueue(e)
                self._weight += e.weight()

    def edges(self):
        """
        Returns the edges in a minimum spanning tree (or forest).
        :return: the edges in a minimum spanning tree (or forest)
        """
        return self._mst

    def weight(self):
        """
        Returns the sum of the edge weights in a minimum spanning tree (or forest).
        :return: the sum of the edge weights in a minimum spanning tree (or forest)
        """
        return self._weight


def main():
    """
    Creates an edge-weighted graph from an input file, runs Kruskal's algorithm on it,
    and prints the edges of the MST and the sum of the edge weights.
    :return:
    """
    if len(sys.argv) > 1:
        sys.stdin = open(sys.argv[1])
        G = EdgeWeightedGraph(stdio.readInt())
        E = stdio.readInt()
        for i in range(E):
            v = stdio.readInt()
            w = stdio.readInt()
            weight = stdio.readFloat()
            e = Edge(v, w, weight)
            G.add_edge(e)
        mst = KruskalMST(G)
        for e in mst.edges():
            print(e)
        print("{:.5f}".format(mst.weight()))


if __name__ == '__main__':
    main()
