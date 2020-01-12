# Created for BADS 2018
# see README.md for details
# This is python3 

from itu.algs4.fundamentals.stack import Stack
from itu.algs4.graphs.graph import Graph


class Bipartite:
    """
    The Bipartite class represents a data type for 
    determining whether an undirected graph is bipartite or whether
    it has an odd-length cycle.
    The isBipartite operation determines whether the graph is
    bipartite. If so, the color operation determines a
    bipartition if not, the oddCycle operation determines a
    cycle with an odd number of edges.
    
    This implementation uses depth-first search.
    The constructor takes time proportional to V + E
    (in the worst case),
    where V is the number of vertices and E is the number of edges.
    Afterwards, the isBipartite and color operations
    take constant time the oddCycle operation takes time proportional
    to the length of the cycle.
    See BipartiteX for a nonrecursive version that uses breadth-first
    search.
    """

    class UnsupportedOperationException(Exception):
        pass

    def __init__(self, G):
        """
        Determines whether an undirected graph is bipartite and finds either a
        bipartition or an odd-length cycle.

        :param G: the graph
        """
        self._is_bipartite = True       # is the graph bipartite?
        self._color = [False] * G.V()   # color[v] gives vertices on one side of bipartition
        self._marked = [False] * G.V()  # marked[v] = True if v has been visited in DFS
        self._edge_to = [0] * G.V()      # edgeTo[v] = last edge on path to v
        self._cycle = None              # odd-length cycle
        
        for v in range(G.V()):
            if not self._marked[v]:
                self._dfs(G, v)

        assert self._check(G)
    
    def _dfs(self, G, v):
        self._marked[v] = True

        for w in G.adj(v):
            # short circuit if odd-length cycle found
            if self._cycle is not None: return

            # found uncolored vertex, so recur
            if not self._marked[w]:
                self._edge_to[w] = v
                self._color[w] = not self._color[v]
                self._dfs(G, w)             

            # if v-w create an odd-length cycle, find it
            elif self._color[w] == self._color[v]:
                self._is_bipartite = False
                self._cycle = Stack()
                self._cycle.push(w)  # don't need this unless you want to include start vertex twice
                x = v
                while x != w:
                    self._cycle.push(x)
                    x = self._edge_to[x]

                self._cycle.push(w)
            
    def is_bipartite(self):
        """
        Returns True if the graph is bipartite.
        
        :returns: True if the graph is bipartite False otherwise
        """
        return self._is_bipartite

    def color(self, v):
        """
        Returns the side of the bipartite that vertex v is on.

        :param v: the vertex
        :returns: the side of the bipartition that vertex v is on two vertices
                are in the same side of the bipartition if and only if they have the
                same color
        :raises IllegalArgumentException: unless 0 <= v < V 
        :raises UnsupportedOperationException: if this method is called when the graph
                is not bipartite
        """
        self._validateVertex(v)
        if not self._is_bipartite:
            raise Bipartite.UnsupportedOperationException("graph is not bipartite")
        return self._color[v]

    def odd_cycle(self):
        """
        Returns an odd-length cycle if the graph is not bipartite, and
        None otherwise.
        
        :returns: an odd-length cycle if the graph is not bipartite
                (and hence has an odd-length cycle), and None otherwise
        """
        return self._cycle

    def _check(self, G):
        # graph is bipartite
        if self._is_bipartite: 
            for v in range(G.V()):
                for w in G.adj(v):
                    if self._color[v] == self._color[w]:
                        error = "edge {}-{} with {} and {} in same side of bipartition\n".format(v, w, v, w)
                        print(error, file=sys.stderr)
                        return False
        # graph has an odd-length cycle
        else:
            # verify cycle
            first = -1
            last = -1
            for v in self.odd_cycle():
                if first == -1:
                    first = v
                last = v
            
            if first != last:
                error = "cycle begins with {} and ends with {}\n".format(first, last)
                print(error, file=sys.stderr)
                return False
        return True
    
    def _validateVertex(self, v):
        # raise an ValueError unless 0 <= v < V    
        V = len(self._marked)
        if v < 0 or v >= V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, V-1))


if __name__ == "__main__":
    from itu.algs4.stdlib.instream import InStream
    from itu.algs4.stdlib import stdio
    import sys
    
    In = InStream(sys.argv[1])
    G = Graph.from_stream(In)
    stdio.writeln(G)

    b = Bipartite(G)
    if b.is_bipartite():
        stdio.writeln("Graph is bipartite")
        for v in range(G.V()):
            stdio.writef("%i: %i\n", v, b.color(v))
    else:
        stdio.writeln("Graph has an odd-length cycle: ")
        for x in b.odd_cycle():
            stdio.writef("%i ", x)
        stdio.writeln()
