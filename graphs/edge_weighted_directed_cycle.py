# Created for BADS 2018
# See README.md for details
# Python 3
import sys, os
def setpath():
    exe = sys.argv[0]
    p = os.path.split(exe)[0]
    sys.path.insert(0, os.path.join(p, '..', 'fundamentals'))
    sys.path.insert(0, os.path.join(p, '..', 'stdlib'))
    sys.path.insert(0, p)
setpath()
from edge_weighted_digraph import EdgeWeightedDigraph
from directed_edge import DirectedEdge
from stack import Stack
import stdrandom

# Execution:    python edge_weighted_directed_cycle V E F
# Finds a directed cycle in an edge-weighted digraph.
# Runs in O(E + V) time.

"""
    The {@code EdgeWeightedDirectedCycle} class represents a data type for 
    determining whether an edge-weighted digraph has a directed cycle.
    The <em>hasCycle</em> operation determines whether the edge-weighted
    digraph has a directed cycle and, if so, the <em>cycle</em> operation
    returns one.
    This implementation uses depth-first search.
    The constructor takes time proportional to <em>V</em> + <em>E</em>
    (in the worst case),
    where <em>V</em> is the number of vertices and <em>E</em> is the number of edges.
    Afterwards, the <em>hasCycle</em> operation takes constant time;
    the <em>cycle</em> operation takes time proportional
    to the length of the cycle.
"""
class EdgeWeightedDirectedCycle:
    """
     Determines whether the edge-weighted digraph {@code G} has a directed cycle and,
     if so, finds such a cycle.
     :param G the edge-weighted digraph
    """
    def __init__(self, G):
        self._marked = [False] * G.V()       # marked[v] = has vertex v been marked?
        self._edgeTo = [None] * G.V()        # edgeTo[v] = previous DirectedEdge on path to v
        self._onStack = [False] * G.V()      # onStack[v] = is vertex on the stack?
        self._cycle = None                   # directed cycle (or None if no such cycle)

        for v in range(G.V()):
            if not self._marked[v]: 
                self._dfs(G, v)

        # check that digraph has a cycle
        assert self._check()

    # check that algorithm computes either the topological order or finds a directed cycle
    def _dfs(self, G, v):
        self._onStack[v] = True;
        self._marked[v] = True;
        for e in G.adj(v):
            w = e.to_vertex()

            # short circuit if directed cycle found
            if self._cycle is not None: 
                return

            # found new vertex, so recur
            elif not self._marked[w]:
                self._edgeTo[w] = e
                self._dfs(G, w)
            
            # trace back directed cycle
            elif self._onStack[w]:
                self._cycle = Stack()
                f = e
                while f.from_vertex() != w:
                    self._cycle.push(f)
                    f = self._edgeTo[f.from_vertex()]
                
                self._cycle.push(f)
                return
        self._onStack[v] = False


    # Does the edge-weighted digraph have a directed cycle?
    # @return {@code True} if the edge-weighted digraph has a directed cycle,
    # {@code False} otherwise
    def has_cycle(self):
        return self._cycle is not None

    # Returns a directed cycle if the edge-weighted digraph has a directed cycle,
    # and {@code None} otherwise.
    # @return a directed cycle (as an iterable) if the edge-weighted digraph
    #    has a directed cycle, and {@code None} otherwise
    def cycle(self):
        return self._cycle

    # certify that digraph is either acyclic or has a directed cycle
    def _check(self):

        # edge-weighted digraph is cyclic
        if self.has_cycle():
            # verify cycle
            first = None
            last = None
            for e in self._cycle():
                if first is None: 
                    first = e
                if last is not None:
                    if last.to_vertex() != e.from_vertex():
                        print("cycle edges {} and {} not incident".format(last, e))
                        return False    
                last = e
            
            if last.to_vertex() != first.from_vertex():
                print("cycle edges {} and {} not incident".format(last, first))
                return False
        
        return True


def main(args):
    # create random DAG with V vertices and E edges; then add F random edges
    V = int(args[0])
    E = int(args[1])
    F = int(args[2])
    G = EdgeWeightedDigraph(V)
    vertices = [i for i in range(V)]
    stdrandom.shuffle(vertices)
    for i in range(E):
        while True:
            v = stdrandom.uniformInt(0,V)
            w = stdrandom.uniformInt(0,V)
            if v >= w:
                break
        weight = stdrandom.uniformFloat(0.0, 1.0)
        G.add_edge(DirectedEdge(v, w, weight))

    # add F extra edges
    for i in range(F):
        v = stdrandom.uniformInt(0,V)
        w = stdrandom.uniformInt(0,V)
        weight = stdrandom.uniformFloat(0.0, 1.0)
        G.add_edge(DirectedEdge(v, w, weight))
    
    print(G)

    # find a directed cycle
    finder = EdgeWeightedDirectedCycle(G)
    if finder.has_cycle():
        print("Cycle: ")
        for e in finder.cycle():
            print("{}  ".format(e), end='')    
        print()
    # or give topologial sort
    else: 
        print("No directed cycle")
    

if __name__ == '__main__':
    main(sys.argv[1:])
