# Created for BADS 2018
# see README.md for details
# This is python3 

from itu.algs4.fundamentals.stack import Stack


class Cycle:
    """
    The Cycle class represents a data type for 
    determining whether an undirected graph has a cycle.
    The hasCycle operation determines whether the graph has
    a cycle and, if so, the cycle operation returns one.

    This implementation uses depth-first search.
    The constructor takes time proportional to V + E
    (in the worst case),
    where V is the number of vertices and E is the number of edges.
    Afterwards, the hasCycle operation takes constant time
    the cycle operation takes time proportional
    to the length of the cycle.
    """

    def __init__(self, G):
        """
        Determines whether the undirected graph G has a cycle and,
        if so, finds such a cycle.
     
        :param G: the undirected graph
        """
        if self._has_self_loop(G): return
        if self._has_parallel_edges(G): return
        self._marked = [False] * G.V()
        self._edgeTo = [0] * G.V()
        self._cycle = None
        for v in range(G.V()):
            if not self._marked[v]:
                self._dfs(G, -1, v)

    def _has_self_loop(self, G):
        # does this graph have a self loop?
        # side effect: initialize cycle to be self loop
        for v in range(G.V()):
            for w in G.adj(v):
                if v == w:
                    self._cycle = Stack()
                    self._cycle.push(v)
                    self._cycle.push(w)
                    return True
        return False

    def _has_parallel_edges(self, G):
        # does this graph have two parallel edges?
        # side effect: initialize cycle to be two parallel edges
        self._marked = [False] * G.V()
        for v in range(G.V()):
            # check for parallel edges incident to v
            for w in G.adj(v):
                if self._marked[w]:
                    self._cycle = Stack()
                    self._cycle.push(v)
                    self._cycle.push(w)
                    self._cycle.push(v)
                    return True
                self._marked[w] = True

            for w in G.adj(v):
                self._marked[w] = False
        return False

    def has_cycle(self):
        """
        Returns true if the graph G has a cycle.

        :returns: true if the graph has a cycle false otherwise
        """
        return self._cycle is not None   
    
    def cycle(self):
        """
        Returns a cycle in the graph G.
        
        :returns: a cycle if the graph G has a cycle,
            and null otherwise
        """
        return self._cycle
    
    def _dfs(self, G, u, v):
        self._marked[v] = True
        for w in G.adj(v):
            # short circuit if cycle already found
            if self._cycle is not None: return
            if not self._marked[w]:
                self._edgeTo[w] = v
                self._dfs(G, v, w)
            elif w != u:
                self._cycle = Stack()
                x = v
                while x != w:
                    self._cycle.push(x)
                    x = self._edgeTo[x]
                self._cycle.push(w)
                self._cycle.push(v)

if __name__ == "__main__":
    import sys
    from itu.algs4.stdlib.instream import InStream
    from itu.algs4.stdlib import stdio
    from itu.algs4.graphs.graph import Graph    

    In = InStream(sys.argv[1])
    G = Graph.from_stream(In)
    finder = Cycle(G)
    if finder.has_cycle():
        for v in finder.cycle():
            stdio.writef("%i ", v)
        stdio.writeln()
    else:
        stdio.writeln("Graph is acyclic")
