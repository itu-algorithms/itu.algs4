# Created for BADS 2018
# see README.md for details
# This is python3 

class CC:
    """
    The CC class represents a data type for 
    determining the connected components in an undirected graph.
    The id operation determines in which connected component
    a given vertex lies the connected operation
    determines whether two vertices are in the same connected component
    the count operation determines the number of connected
    components and the size operation determines the number
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
        Computes the connected components of the undirected graph G.

        :param G: the undirected graph
        """
        self._marked = [False] * G.V()  # marked[v] = has vertex v been marked?
        self._id = [None] * G.V()       # id[v] = id of connected component containing v
        self._size = [0] * G.V()        # size[id] = number of vertices in given component
        self._count = 0                 # number of connected components

        for v in range(G.V()):
            if not self._marked[v]:
                self._dfs(G, v) 
                self._count += 1

    def _dfs(self, G, v):
        # depth-first search for a Graph
        self._marked[v] = True
        self._id[v] = self._count
        self._size[self._count] += 1
        for w in G.adj(v):
            if not self._marked[w]:
                self._dfs(G, w)
    
    def id(self, v):
        """
        Returns the component id of the connected component containing vertex v.
     
        :param v: the vertex
        :returns: the component id of the connected component containing vertex v
        :raises ValueError: unless 0 <= v < V
        """    
        self._validate_vertex(v)
        return self._id[v]

    def size(self, v):
        """
        Returns the number of vertices in the connected component containing vertex v.
     
        :param v: the vertex
        :returns: the number of vertices in the connected component containing vertex v
        :raises ValueError: unless 0 <= v < V
        """
        self._validate_vertex(v)
        return self._size[self._id[v]]

    def count(self):
        """
        Returns the number of connected components in the graph G.

        :returns: the number of connected components in the graph G
        """
        return self._count

    def connected(self, v, w):
        """
        Returns true if vertices v and w are in the same connected component.
     
        :param v: one vertex
        :param w: the other vertex
        :returns: True if vertices v and w are in the same connected component; 
                    False otherwise
        :raises ValueError: unless 0 <= v < V
        :raises ValueError: unless 0 <= w < V
        """
        self._validate_vertex(v)
        self._validate_vertex(w)
        return self.id(v) == self.id(w)

    def _validate_vertex(self, v):
        # Raises a ValueError n unless 0 <= v < V
        V = len(self._marked)
        if v < 0 or v >= V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, V-1))


class CCBook:
    def __init__(self, G):
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

if __name__ == "__main__":
    import sys
    from itu.algs4.fundamentals.queue import Queue
    from itu.algs4.stdlib.instream import InStream    
    from itu.algs4.stdlib import stdio    
    from itu.algs4.graphs.graph import Graph    

    In = InStream(sys.argv[1])
    G = Graph.from_stream(In)
    cc = CC(G)

    # number of connected components
    m = cc.count()
    stdio.writef("%i components\n", m)

    # compute list of vertices in each connected component
    components = [Queue() for _ in range(m)]
    for v in range(G.V()):
        components[cc.id(v)].enqueue(v)

    # print results
    for i in range(m):
        for v in components[i]:
            stdio.writef("%i ", v)
        stdio.writeln()
