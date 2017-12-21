class CC:
    """
    The CC class represents a data type for 
    determining the connected components in an undirected graph.
    The id operation determines in which connected component
    a given vertex lies; the connected operation
    determines whether two vertices are in the same connected component;
    the count operation determines the number of connected
    components; and the size operation determines the number
    of vertices in the connect component containing a given vertex.

    The component identifier of a connected component is one of the
    vertices in the connected component: two vertices have the same component
    identifier if and only if they are in the same connected component.

    This implementation uses depth-first search.
    The constructor takes time proportional to V + E
    (in the worst case),
    where V is the number of vertices and E is the number of edges.
    Afterwards, the id, count, connected,
    and size operations take constant time.
    """
    def __init__(self, G):
        """
        Computes the connected components of the undirected graph {@code G}.

        :param G: the undirected graph
        """
        self._marked = [False] * G.V()  # marked[v] = has vertex v been marked?
        self._id = [None] * G.V()       # id[v] = id of connected component containing v
        self._count = 0                 # number of connected components
        for s in range(G.V()):
            if not self._marked[s]:
                self._dfs(G, s) 
                self._count += 1
    
    def _dfs(self, G, v):
        self._marked[v] = True
        self._id[v] = self._count
        for w in G.adj(v):
            if not self._marked[w]:
                self._dfs(G, w)
    
    def connected(self, v, w):
        return self._id[v] == self._id[w]

    def id(self, v):
        return self._id[v]

    def count(self):
        return self._count