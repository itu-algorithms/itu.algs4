# Created for BADS 2018
# See README.md for details
# Python 3

import sys

import itu.algs4.graphs.directed_edge
from itu.algs4.graphs.acyclic_lp import AcyclicLp
from itu.algs4.graphs.directed_edge import DirectedEdge
from itu.algs4.graphs.edge_weighted_digraph import EdgeWeightedDigraph
from itu.algs4.stdlib import instream

"""
The cpm module is an example of using graphs to solve the parallel precedence-constrained 
job scheduling problem via the critical path method. It reduces the problem to the longest-paths 
problem in edge-weighted DAGs. It builds an edge-weighted digraph (which must be a DAG) from the 
job-scheduling problem specification, finds the longest-paths tree, and computes the longest-paths 
lengths (which are precisely the start times for each job).

This implementation uses AcyclicLP to find a longest path in a DAG. The running time is proportional 
to V + E, where V is the number of jobs and E is the number of precedence constraints.

For additional documentation, see Section 4.4 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
"""



# Try this with the jobsPC.txt data file
if __name__ == '__main__':
    # Create stream from file or the standard input,
    # depending on whether a file name was passed.    
    file = sys.argv[1] if len(sys.argv) > 1 else None
    stream = instream.InStream(file)
    
    # Number of jobs
    N = stream.readInt()

    # Source and sink
    source, sink = 2*N, 2*N+1
    
    # Construct the network
    G = EdgeWeightedDigraph(2*N+2)
    for i in range(N):
        duration = stream.readFloat()
        G.add_edge(DirectedEdge(i, i+N, duration))
        G.add_edge(DirectedEdge(source, i, 0.0))
        G.add_edge(DirectedEdge(i+N, sink, 0.0))
        
        # Precedence constraints
        m = stream.readInt()
        for _ in range (m):
            successor = stream.readInt()
            G.add_edge(DirectedEdge(i+N, successor, 0.0))
    
    # Compute longest path
    lp = AcyclicLp(G, source)
    
    # Print results
    print('Start times:')
    for i in range(N):
        print('{:4d}: {:5.1f}'.format(i, lp.dist_to(i)))
    print('Finish time: {:5.1f}'.format(lp.dist_to(i)))
