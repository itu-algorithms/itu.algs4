# Created for BADS 2018
# See README.md for details
# Python 3
import sys, os
def setpath():
    exe = sys.argv[0]
    p = os.path.split(exe)[0]
    sys.path.insert(0, os.path.join(p, '..', 'fundamentals'))
    sys.path.insert(0, os.path.join(p, '..', 'errors'))
    sys.path.insert(0, os.path.join(p, '..', 'stdlib'))
    sys.path.insert(0, p)
setpath()
from edge_weighted_digraph import EdgeWeightedDigraph
from directed_edge import DirectedEdge
from edge_weighted_directed_cycle import EdgeWeightedDirectedCycle
from queue import Queue
from errors import IllegalArgumentException, UnsupportedOperationException
import stdio
from instream import InStream

try:
    q = Queue()
    q.enqueue(1)
except AttributeError:
    print('ERROR - Could not import algs4 queue')
    sys.exit(1)

#  Execution:    python BellmanFordSP.py filename.txt s
#  Data files:   https://algs4.cs.princeton.edu/44sp/tinyEWDn.txt
#                https://algs4.cs.princeton.edu/44sp/mediumEWDnc.txt
#
#  Bellman-Ford shortest path algorithm. Computes the shortest path tree in
#  edge-weighted digraph G from vertex s, or finds a negative cost cycle
#  reachable from s.

"""
 The {@code BellmanFordSP} class represents a data type for solving the
 single-source shortest paths problem in edge-weighted digraphs with
 no negative cycles. 
 The edge weights can be positive, negative, or zero.
 This class finds either a shortest path from the source vertex <em>s</em>
 to every other vertex or a negative cycle reachable from the source vertex.
 This implementation uses the Bellman-Ford-Moore algorithm.
 The constructor takes time proportional to <em>V</em> (<em>V</em> + <em>E</em>)
 in the worst case, where <em>V</em> is the number of vertices and <em>E</em>
 is the number of edges.
 Each call to {@code distTo(int)} and {@code hasPathTo(int)},
 {@code hasNegativeCycle} takes constant time;
 each call to {@code pathTo(int)} and {@code negativeCycle()}
 takes time proportional to length of the path returned.
"""

class BellmanFordSP:
    # Computes a shortest paths tree from {@code s} to every other vertex in
    # the edge-weighted digraph {@code G}.
    # @param G the acyclic digraph
    # @param s the source vertex
    # @throws IllegalArgumentException unless {@code 0 <= s < V}
    def __init__(self, G, s):
        self.distTo = [sys.float_info.max] * G.V()  #distTo[v] = distance  of shortest s->v path
        self.edgeTo = [None] * G.V()                #edgeTo[v] = last edge on shortest s->v path
        self.onQueue = [False] * G.V()              #onQueue[v] = is v currently on the queue?
        self.queue = Queue()                        #queue of vertices to relax
        self.cost = 0                               #number of calls to relax()
        self.cycle = None                           #negative cycle (or None if no such cycle)
        
        #Bellman-Ford algorithm
        self.distTo[s] = 0.0
        self.queue.enqueue(s)
        self.onQueue[s] = True
        while not queue.is_empty() and not self.has_negative_cycle():
            v = queue.dequeue()
            self.onQueue[v] = False
            self._relax(G, v)
        assert self._check(G, s)

    #relax vertex v and put other endpoints on queue if changed
    def _relax(self, G, v):
        for e in G.adj(v):
            w = e.to_vertex()
            if self.distTo[w] > self.distTo[v] + e.weight():
                self.distTo[w] = self.distTo[v] + e.weight()
                self.edgeTo[w] = e
                if not self.onQueue[w]:
                    self.queue.enqueue(w)
                    self.onQueue[w] = True
            if self.cost % G.V() == 0:
                self._find_negative_cycle()
                if self.has_negative_cycle():
                    return  #found a negative cycle
            self.cost += 1
        
    # Is there a negative cycle reachable from the source vertex {@code s}?
    # @return {@code true} if there is a negative cycle reachable from the
    #    source vertex {@code s}, and {@code false} otherwise
    def has_negative_cycle(self):
        return self.cycle is not None

    # Returns a negative cycle reachable from the source vertex {@code s}, or {@code None}
    # if there is no such cycle.
    # @return a negative cycle reachable from the soruce vertex {@code s} 
    #    as an iterable of edges, and {@code None} if there is no such cycle
    def negative_cycle(self):
        return self.cycle

    #by finding a cycle in predecessor graph
    def _find_negative_cycle(self):
        V = len(self.edgeTo)
        spt = EdgeWeightedDigraph(V)
        for v in range(V):
            if self.edgeTo[v] is not None:
                spt.add_edge(self.edgeTo[v])

        finder = EdgeWeightedDirectedCycle(spt)
        self.cycle = finder.cycle()

    # Returns the length of a shortest path from the source vertex {@code s} to vertex {@code v}.
    # @param  v the destination vertex
    # @return the length of a shortest path from the source vertex {@code s} to vertex {@code v};
    #         {@code sys.float_info.max} if no such path
    # @throws UnsupportedOperationException if there is a negative cost cycle reachable
    #         from the source vertex {@code s}
    # @throws IllegalArgumentException unless {@code 0 <= v < V}
    def dist_to(self, v):
        self._validate_vertex(v);
        if self.has_negative_cycle():
            raise UnsupportedOperationException("Negative cost cycle exists")
        return self.distTo[v]
    
    # Is there a path from the source {@code s} to vertex {@code v}?
    # @param  v the destination vertex
    # @return {@code true} if there is a path from the source vertex
    #         {@code s} to vertex {@code v}, and {@code false} otherwise
    # @throws IllegalArgumentException unless {@code 0 <= v < V}
    def has_path_to(self, v):
        self._validate_vertex(v)
        return self.distTo[v] < sys.float_info.max

    # Returns a shortest path from the source {@code s} to vertex {@code v}.
    # @param  v the destination vertex
    # @return a shortest path from the source {@code s} to vertex {@code v}
    #         as an iterable of edges, and {@code None} if no such path
    # @throws UnsupportedOperationException if there is a negative cost cycle reachable
    #         from the source vertex {@code s}
    # @throws IllegalArgumentException unless {@code 0 <= v < V}
    def path_to(self, v):
        self.validate_vertex(v)
        if self.has_negative_cycle():
            raise UnsupportedOperationException("Negative cost cycle exists")
        if not self.has_path_to(v): return None
        path = Stack()
        e = self.edgeTo[v]
        while e is not None:
            path.push(e)
            e = self.edgeTo[e.from_vertex()]
        return path

    #check optimality conditions: either 
    #(i) there exists a negative cycle reacheable from s
    #    or 
    #(ii)  for all edges e = v->w:            distTo[w] <= distTo[v] + e.weight()
    #(ii') for all edges e = v->w on the SPT: distTo[w] == distTo[v] + e.weight()
    def _check(self, G, s):

        #has a negative cycle
        if self.has_negative_cycle():
            weight = 0.0
            for e in self.negative_cycle():
                weight += e.weight()
            if weight >= 0.0:
                print("error: weight of negative cycle = {}".format(weight))
                return False

        #no negative cycle reachable from source
        else:

            #check that distTo[v] and edgeTo[v] are consistent
            if self.distTo[s] != 0.0 or self.edgeTo[s] is not None:
                print("distanceTo[s] and edgeTo[s] inconsistent")
                return False;
            
            for v in range(G.V()):
                if v == s: continue
                if self.edgeTo[v] is None and self.distTo[v] != sys.float_info.max:
                    print("distTo[] and edgeTo[] inconsistent")
                    return False

            #check that all edges e = v->w satisfy distTo[w] <= distTo[v] + e.weight()
            for v in range(G.V()):
                for e in G.adj(v):
                    w = e.to_vertex()
                    if self.distTo[v] + e.weight() < self.distTo[w]:
                        print("edge {} not relaxed".format(e))
                        return False;

            #check that all edges e = v->w on SPT satisfy distTo[w] == distTo[v] + e.weight()
            for w in range(G.V()):
                if self.edgeTo[w] is None: continue
                e = self.edgeTo[w]
                v = e.from_vertex()
                if w != e.to_vertex(): return False
                if self.distTo[v] + e.weight() != self.distTo[w]:
                    print("edge {} on shortest path not tight".format(e))
                    return False

        print("Satisfies optimality conditions")
        print()
        return True

    #raise an IllegalArgumentException unless {@code 0 <= v < V}
    def _validate_vertex(self, v):
        V = len(self.distTo)
        if v < 0 or v >= V:
            raise IllegalArgumentException("vertex {} is not between 0 and {}".format(v, V-1))
    

def main(args):
    stream = InStream(args[0])
    s = int(args[1])
    G = EdgeWeightedDigraph.from_stream(stream)
    sp = BellmanFordSP(G, s)

    #print negative cycle
    if sp.has_negative_cycle():
        for e in sp.negative_cycle():
            print(e)
    #print shortest paths
    else:
        for v in range(G.V()):
            if sp.has_path_to(v):
                print("{} to {} ({})  ".format( s, v, sp.distTo(v)))
                for e in sp.path_to(v):
                    print("{}   ".format(e), end='')
                print()
            else:
                print("{} to {}           no path".format(s, v))

if __name__ == '__main__':
    main(sys.args[1:])

 # *  % python BellmanFordSP.py tinyEWDn.txt 0
 # *  0 to 0 ( 0.00)  
 # *  0 to 1 ( 0.93)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52   6->4 -1.25   4->5  0.35   5->1  0.32
 # *  0 to 2 ( 0.26)  0->2  0.26   
 # *  0 to 3 ( 0.99)  0->2  0.26   2->7  0.34   7->3  0.39   
 # *  0 to 4 ( 0.26)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52   6->4 -1.25   
 # *  0 to 5 ( 0.61)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52   6->4 -1.25   4->5  0.35
 # *  0 to 6 ( 1.51)  0->2  0.26   2->7  0.34   7->3  0.39   3->6  0.52   
 # *  0 to 7 ( 0.60)  0->2  0.26   2->7  0.34   
 # *
 # *  % python BellmanFordSP.py tinyEWDnc.txt 0
 # *  4->5  0.35
 # *  5->4 -0.66
 # *