# Created for BADS 2018
# See README.md for details
# Python 3

"""
 *  Execution:    python transitive_closure.py filename.txt
 *  Dependencies: Digraph DirectedDFS 
 *  Data files:   https:#algs4.cs.princeton.edu/42digraph/tinyDG.txt
 *
 *  Compute transitive closure of a digraph and support
 *  reachability queries.
 *
 *  Preprocessing time: O(V(E + V)) time.
 *  Query time: O(1).
 *  Space: O(V^2).
 *
 *  % python transitive_closure.py tinyDG.txt
 *         0  1  2  3  4  5  6  7  8  9 10 11 12
 *  --------------------------------------------
 *    0:   T  T  T  T  T  T                     
 *    1:      T                                 
 *    2:   T  T  T  T  T  T                     
 *    3:   T  T  T  T  T  T                     
 *    4:   T  T  T  T  T  T                     
 *    5:   T  T  T  T  T  T                     
 *    6:   T  T  T  T  T  T  T        T  T  T  T
 *    7:   T  T  T  T  T  T  T  T  T  T  T  T  T
 *    8:   T  T  T  T  T  T  T  T  T  T  T  T  T
 *    9:   T  T  T  T  T  T           T  T  T  T
 *   10:   T  T  T  T  T  T           T  T  T  T
 *   11:   T  T  T  T  T  T           T  T  T  T
 *   12:   T  T  T  T  T  T           T  T  T  T
 *
"""
import sys
from graphs.digraph import Digraph
from graphs.directed_dfs import DirectedDFS
from errors.errors import IllegalArgumentException
from stdlib.instream import InStream

class TransitiveClosure:
    """
     * Computes the transitive closure of the digraph {@code G}.
     * @param G the digraph
     """
    def __init__(self, G): 
        self._tc = [None] * G.V()  # tc[v] = reachable from v
        for v in range(G.V()):
            self._tc[v] = DirectedDFS(G, v)
    """
     * Is there a directed path from vertex {@code v} to vertex {@code w} in the digraph?
     * @param  v the source vertex
     * @param  w the target vertex
     * @return {@code true} if there is a directed path from {@code v} to {@code w},
     *         {@code false} otherwise
     * @throws IllegalArgumentException unless {@code 0 <= v < V}
     * @throws IllegalArgumentException unless {@code 0 <= w < V}
     """
    def reachable(self, v, w):
        self._validate_vertex(v)
        self._validate_vertex(w)
        return self._tc[v].is_marked(w)

    # throw an IllegalArgumentException unless {@code 0 <= v < V}
    def _validate_vertex(self, v):
        V = len(self._tc)
        if v < 0 or v >= V:
            raise IllegalArgumentException("vertex {} is not between 0 and {}".format(v,V-1))
    

def main(args):
    stream = InStream(args[0])
    G = Digraph.from_stream(stream)

    tc = TransitiveClosure(G)

    # print header
    print("     ", end='')
    for v in range(G.V()):
        print("{x:3d}".format(x=v), end='')
    print()
    print("--------------------------------------------")

    # print transitive closure
    for v in range(G.V()):
        print("{x:3d}: ".format(x=v), end='')
        for w in range(G.V()):
            if (tc.reachable(v, w)):
                print("  T", end='')
            else:
                print("   ", end='')
        print()
    

if __name__ == '__main__':
    main(sys.argv[1:])


