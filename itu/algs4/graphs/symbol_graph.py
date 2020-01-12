# Created for BADS 2018
# see README.md for details
# This is python3 

from itu.algs4.graphs.graph import Graph
from itu.algs4.searching.binary_search_st import BinarySearchST
from itu.algs4.stdlib import stdio
from itu.algs4.stdlib.instream import InStream


class SymbolGraph:
    """
    The SymbolGraph class represents an undirected graph, where the
    vertex names are arbitrary strings.
    By providing mappings between vertex names and integers,
    it serves as a wrapper around the
    Graph data type, which assumes the vertex names are integers
    between 0 and V - 1.
    It also supports initializing a symbol graph from a file.
    
    This implementation uses an ST to map from strings to integers,
    an array to map from integers to strings, and a Graph to store
    the underlying graph.
    The index_of and contains operations take time 
    proportional to log V, where V is the number of vertices.
    The name_of operation takes constant time.
    """

    def __init__(self, filename, delimiter):
        """
        Initializes a graph from a file using the specified delimiter.
        Each line in the file contains
        the name of a vertex, followed by a list of the names
        of the vertices adjacent to that vertex, separated by the delimiter.

        :param filename: the name of the file
        :param delimiter: the delimiter between fields
        """
        self._st = BinarySearchST()             # string -> index

        # First pass builds the index by reading strings to associate
        # distinct strings with an index
        stream = InStream(filename)
        while not stream.isEmpty():
            a = stream.readLine().split(delimiter)
            for i in range(len(a)):
                if not self._st.contains(a[i]):
                    self._st.put(a[i], self._st.size())

        stdio.writef("Done reading %s\n", filename)

        # inverted index to get keys in an array
        self._keys = [None] * self._st.size()   # index  -> string
        for name in self._st.keys():
            self._keys[self._st.get(name)] = name
    
        # second pass builds the graph by connecting first vertex on each
        # line to all others
        self._graph = Graph(self._st.size())    # the underlying graph
        stream = InStream(filename)
        while stream.hasNextLine():
            a = stream.readLine().split(delimiter)
            v = self._st.get(a[0])
            for i in range(1, len(a)):
                w = self._st.get(a[i])
                self._graph.add_edge(v, w)

    def contains(self, s):
        """
        Does the graph contain the vertex named s?

        :param s: the name of a vertex
        :return:s true if s is the name of a vertex, and false otherwise        
        """
        return self._st.contains(s)

    def index_of(self, s):
        """
        Returns the integer associated with the vertex named s.
        :param s: the name of a vertex
        :returns: the integer (between 0 and V - 1) associated with the vertex named s
        """
        return self._st.get(s)
    
    def name_of(self, v):
        """
        Returns the name of the vertex associated with the integer v.
        @param  v the integer corresponding to a vertex (between 0 and V - 1) 
        @throws IllegalArgumentException unless 0 <= v < V
        @return the name of the vertex associated with the integer v
        """
        self._validateVertex(v)
        return self._keys[v]

    def graph(self):
        return self._graph


    def _validateVertex(self, v):
        # throw an IllegalArgumentException unless 0 <= v < V
        V = self._graph.V()
        if v < 0 or v >= V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, V-1))

if __name__ == "__main__":
    import sys

    filename  = sys.argv[1]    
    delimiter = sys.argv[2]
    sg = SymbolGraph(filename, delimiter)
    graph = sg.graph()
    while stdio.hasNextLine():
        source = stdio.readLine()
        if sg.contains(source):
            s = sg.index_of(source)
            for v in graph.adj(s):
                stdio.writef("\t%s\n",sg.name_of(v))
        else:
            stdio.writef("input not contain '%i'", source)
