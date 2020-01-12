# Created for BADS 2018
# see README.md for details
# This is python3 

from itu.algs4.fundamentals.stack import Stack


class DepthFirstPaths:
    """
    The  DepthFirstPaths class represents a data type for finding
    paths from a source vertex s to every other vertex
    in an undirected graph.

    This implementation uses depth-first search.
    The constructor takes time proportional to V + E,
    where V is the number of vertices and E is the number of edges.
    Each call to hasPathTo(int) takes constant time
    each call to pathTo(int) takes time proportional to the length
    of the path.
    It uses extra space (not including the graph) proportional to V.
    """

    def __init__(self, G, s):
        """
        Computes a path between s and every other vertex in graph G.

        :param G: the graph
        :param s: the source vertex
        :raises ValueError: unless 0 <= s < V     
        """
        self._marked = [False] * G.V()  # Has dfs been called for this vertex?
        self._edgeTo = [0] * G.V()      # last vertex on known path to this vertex
        self._s = s                     # source        
        self._validateVertex(s)
        self._dfs(G, s)

    def _dfs(self, G, v):
        # depth first search from v
        self._marked[v] = True
        for w in G.adj(v):
            if not self._marked[w]:
                self._edgeTo[w] = v
                self._dfs(G, w)

    def has_path_to(self, v):
        """
        Is there a path between the source vertex s and vertex v?
        :param v: the vertex
        :returns: true if there is a path, false otherwise
        :raises ValueError: unless 0 <= v < V
        """
        self._validateVertex(v)
        return self._marked[v]

    def path_to(self, v):
        """
        Returns a path between the source vertex s and vertex v, or
        None if no such path.
        :param v: the vertex
        :returns: the sequence of vertices on a path between the source vertex
                   s and vertex v, as an Iterable
        :raises ValueError: unless 0 <= v < V
        """
        self._validateVertex(v)
        if not self.has_path_to(v): return None
        path = Stack()
        w = v
        while w != self._s:
            path.push(w)
            w = self._edgeTo[w]
        path.push(self._s)

        return path

    def _validateVertex(self, v):
        # throw an ValueError unless 0 <= v < V
        V = len(self._marked)
        if v < 0 or v >= V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, V-1))

if __name__ == "__main__":
    from itu.algs4.stdlib import stdio
    from itu.algs4.graphs.graph import Graph
    from itu.algs4.stdlib.instream import InStream
    import sys

    In = InStream(sys.argv[1])
    G = Graph.from_stream(In)
    s = int(sys.argv[2])
    dfs = DepthFirstPaths(G, s)

    for v in range(G.V()):
        if dfs.has_path_to(v):
            stdio.writef("%d to %d:  ", s, v)
            for x in dfs.path_to(v):
                if x == s: stdio.write(x)
                else:      stdio.writef("-%i", x)            
            stdio.writeln()
        else:
            stdio.writef("%d to %d:  not connected\n", s, v)            
