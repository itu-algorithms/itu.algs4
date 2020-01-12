# Created for BADS 2018
# see README.md for details
# This is python3 

import math

from itu.algs4.fundamentals.queue import Queue
from itu.algs4.fundamentals.stack import Stack
from itu.algs4.stdlib import stdio


class BreadthFirstPaths:
    """
    The BreadthFirstPaths class represents a data type for finding
    shortest paths (number of edges) from a source vertex s
    (or a set of source vertices)
    to every other vertex in a directed or undirected graph.
    
    This implementation uses breadth-first search.
    The constructor takes time proportional to V + E,
    where V is the number of vertices and E is the number of edges.
    Each call to distTo(int) and hasPathTo(int) takes constant time
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
        self._marked = [False] * G.V()      # Is a shortest path to this vertex known?
        self._dist_to = [math.inf] * G.V()
        self._edgeTo = [0] * G.V()          # last vertex on known path to this vertex        
        self._validateVertex(s)
        self._bfs(G, s)

        assert self._check(G, s)

    # @staticmethod
    # def from_multiple_sources(G, sources):
    #     """
    #     Computes the shortest path between any one of the source vertices in sources
    #     and every other vertex in graph G.

    #     :param G the graph
    #     :param sources the source vertices
    #     :raises ValueError: unless 0 <= s < V for each vertex
    #                         s in sources
    #     """
    #     pass

    def _bfs(self, G, s):
        # breadth-first search from a single source
        queue = Queue()
        self._dist_to[s] = 0
        self._marked[s] = True              # Mark the source
        queue.enqueue(s)                    #   and put it on the queue.

        while not queue.is_empty():
            v = queue.dequeue()             # Remove next vertex from the queue.
            for w in G.adj(v):
                if not self._marked[w]:
                    self._edgeTo[w] = v     # For every unmarked adjacent vertex,
                    self._dist_to[w] = self._dist_to[v] + 1
                    self._marked[w] = True  # mark it because path is known,
                    queue.enqueue(w)        # and add it to the queue.

    # def _bfs_multiple_sources(self, G, sources):
    #     # breadth-first search from multiple sources
    #     pass

    def has_path_to(self, v):
        """
        Is there a path between the source vertex s (or sources) and vertex v?

        :param v: the vertex
        :returns: true if there is a path, and False otherwise
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
        self._validateVertex(v)
        return self._dist_to[v]

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
        while self._dist_to[x] != 0:
            path.push(x)
            x = self._edgeTo[x]
        path.push(x)
        return path

    def _check(self, G, s):
        # check optimality conditions for singe source
        # check that the distance of s = 0
        if (self._dist_to[s] != 0):
            stdio.writef("distance of source %i to itself = %i\n", s, self._dist_to[s])
            return False

        # check that for each edge v-w dist[w] <= dist[v] + 1
        # provided v is reachable from s
        for v in range(G.V()):
            for w in G.adj(v):
                #if self.has_path_to(v) != self.has_path_to(w):
                # modified for directed graphs
                if self.has_path_to(v) and not self.has_path_to(w):
                    stdio.writef("edge %i-%i\n", v, w)
                    stdio.writef("has_path_to(%i) = %s\n", v, self.has_path_to(v))
                    stdio.writef("has_path_to(%i) = %s\n", w, self.has_path_to(w))
                    return False
                if self.has_path_to(v) and (self._dist_to[w] > self._dist_to[v] + 1):
                    stdio.writef("edge %i-%i\n", v, w)
                    stdio.writef("dist_to[%i] = %i\n", v, self._dist_to[v])
                    stdio.writef("dist_to[%i] = %i\n", v, self._dist_to[w])
                    return False

        # check that v = edgeTo[w] satisfies distTo[w] = distTo[v] + 1
        # provided v is reachable from s
        for w in range(G.V()):
            if not self.has_path_to(w) or w == s: continue
            v = self._edgeTo[w]
            if self._dist_to[w] != self._dist_to[v] + 1:
                stdio.writef("shortest path edge %i-%i\n", v, w)
                stdio.writef("dist_to[%i] = %i\n", v, self._dist_to[v])
                stdio.writef("dist_to[%i] = %i\n", w, self._dist_to[w])
                return False

        return True

    def _validateVertex(self, v):
        # throw an ValueError unless 0 <= v < V
        V = len(self._marked)
        if v < 0 or v >= V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, V-1))

    # def _validateVertices(self, vertices):
    #     # throw an ValueError unless 0 <= v < V
    #     pass

class BreadthFirstPathsBook:
    def __init__(self, G, s):
        self._marked = [False] * G.V()  # Is a shortest path to this vertex known?
        self._edgeTo = [0] * G.V()      # last vertex on known path to this vertex
        self._s = s                     # source
        self._bfs(G, s)

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

    def has_path_to(self, v):
        return self._marked[v]

    def path_to(self, v):
        if not self.has_path_to(v): return None
        path = Stack()
        x = v
        while x != self._s:
            path.push(x)
            x = self._edgeTo[x]
        path.push(self._s)
        return path

if __name__ == "__main__":
    import sys
    from itu.algs4.stdlib import stdio
    from itu.algs4.graphs.graph import Graph
    from itu.algs4.stdlib.instream import InStream

    In = InStream(sys.argv[1])
    G = Graph.from_stream(In)
    s = int(sys.argv[2])
    bfs  = BreadthFirstPaths(G, s)

    for v in range(G.V()):
        if bfs.has_path_to(v):
            stdio.writef("%d to %d (%d):  ", s, v, bfs.dist_to(v))
            for x in bfs.path_to(v):
                if x == s: stdio.write(x)
                else:      stdio.writef("-%i", x)            
            stdio.writeln()
        else:
            stdio.writef("%d to %d (-):  not connected\n", s, v)
