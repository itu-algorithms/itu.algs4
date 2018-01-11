from ..fundamentals.stack import Stack
from ..fundamentals.queue import Queue

class BreadthFirstPaths:
    """
    The BreadthFirstPaths class represents a data type for finding
    shortest paths (number of edges) from a source vertex s
    (or a set of source vertices)
    to every other vertex in an undirected graph.
    
    This implementation uses breadth-first search.
    The constructor takes time proportional to V + E,
    where V is the number of vertices and E is the number of edges.
    Each call to distTo(int) and hasPathTo(int) takes constant time;
    each call to pathTo(int) takes time proportional to the length
    of the path.
    It uses extra space (not including the graph) proportional to V.
    """
    def __init__(self, G, s):
        """
        Computes the shortest path between the source vertex s
        and every other vertex in the graph G.

        :param G: the graph
        :param s: the source vertex
        :raises ValueError: unless 0 <= s < V
        """
        self._marked = [False] * G.V()  # Is a shortest path to this vertex known?
        self._edgeTo = [0] * G.V()      # last vertex on known path to this vertex
        self._s = s                     # source
        self._bfs(G, s)

    @staticmethod
    def from_multiple_sources(G, sources):
        """
        Computes the shortest path between any one of the source vertices in sources
        and every other vertex in graph G.

        :param G the graph
        :param sources the source vertices
        :raises ValueError: unless 0 <= s < V for each vertex
                            s in sources
        """
        pass

    def _bfs(self, G, s):
        # breadth-first search from a single source
        queue = Queue()
        self._marked[s] = True              # Mark the source
        queue.enqueue(s)                    #   and put it on the queue.
        while not queue.is_empty():
            v = queue.dequeue()             # Remove next vertex from the queue.
            for w in G.adj(v):
                if not self._marked[w]:
                    self._edgeTo[w] = v     # For every unmarked adjacent vertex,
                    self._marked[w] = True  # mark it because path is known,
                    queue.enqueue(w)        # and add it to the queue.

    def _bfs_multiple_sources(self, G, sources):
        # breadth-first search from multiple sources
        pass

    def has_path_to(self, v):
        """
        Is there a path between the source vertex s (or sources) and vertex v?

        :param v: the vertex
        :returns: true if there is a path, and false otherwise
        :raises ValueError: unless 0 <= v < V
        """
        return self._marked[v]

    def dist_to(self, v):
        """
        Returns the number of edges in a shortest path between the source vertex s
        (or sources) and vertex v?

        :param v: the vertex
        :returns: the number of edges in a shortest path
        :raises ValueError: unless 0 <= v < V
        """
        pass

    def path_to(self, v):
        """
        Returns a shortest path between the source vertex s (or sources)
        and v, or null if no such path.

        :param v: the vertex
        :returns: the sequence of vertices on a shortest path, as an Iterable
        :raises ValueError: unless 0 <= v < V
        """
        if not self.has_path_to(v): return None
        path = Stack()
        x = v
        while x != self._s:
            path.push(x)
            x = self._edgeTo[x]
        path.push(self._s)

        return path

    def _check(self, G, s):
        # check optimality conditions for singe source
        pass

    def _validateVertex(self, v):
        # throw an ValueError unless 0 <= v < V
        V = len(self._marked)
        if v < 0 or v >= V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, V-1))

    def _validateVertices(self, vertices):
        # throw an ValueError unless 0 <= v < V
        pass