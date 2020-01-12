# Created for BADS 2018
# see README.md for details
# This is python3 
 
class DepthFirstSearch:
    """
    The DepthFirstSearch class represents a data type for 
    determining the vertices connected to a given source vertex s
    in an undirected graph. For versions that find the paths, see
    DepthFirstPaths and BreadthFirstPaths.

    This implementation uses depth-first search.
    The constructor takes time proportional to V + E
    (in the worst case),
    where V is the number of vertices and E is the number of edges.
    It uses extra space (not including the graph) proportional to V.
    """
    def __init__(self, G, s):
        """
        Computes the vertices in graph G that are
        connected to the source vertex s.
        :param G: the graph
        :param s: the source vertex
        :throws ValueError: unless 0 <= s < V
        """
        self._marked = [False] * G.V()  # marked[v] = is there an s-v path?        
        self._count = 0                 # number of vertices connected to s
        self._validateVertex(s)
        self._dfs(G, s)
    
    def _dfs(self, G, v):
        # depth first search from v        
        self._marked[v] = True
        self._count += 1
        for w in G.adj(v):
            if not self._marked[w]:
                self._dfs(G, w)

    def marked(self, v):
        """
        Is there a path between the source vertex s and vertex v?
     
        :param v: the vertex
        :returns: true if there is a path, false otherwise
        :raises ValueError: unless 0 <= v < V
        """
        self._validateVertex(v)
        return self._marked[v]

    def count(self):
        """
        Returns the number of vertices connected to the source vertex s.

        :returns: the number of vertices connected to the source vertex s
        """
        return self._count
    
    def _validateVertex(self, v):
        # throw an ValueError unless 0 <= v < V
        V = len(self._marked)
        if v < 0 or v >= V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, V-1))

    
if __name__ == "__main__":
    from itu.algs4.graphs.graph import Graph
    from itu.algs4.stdlib.instream import InStream
    from itu.algs4.stdlib import stdio
    import sys

    In = InStream(sys.argv[1])
    G = Graph.from_stream(In)
    s = int(sys.argv[2])
    search = DepthFirstSearch(G, s)
    for v in range(G.V()):
        if search.marked(v):
            stdio.writef("%i ", v)
    stdio.writeln()

    if search.count() != G.V(): stdio.writeln("NOT connected")
    else:                       stdio.writeln("connected")
