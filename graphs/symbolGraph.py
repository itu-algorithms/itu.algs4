class SymbolGraph:
    """
    The SymbolGraph class represents an undirected graph, where the
    vertex names are arbitrary strings.
    By providing mappings between string vertex names and integers,
    it serves as a wrapper around the
    Graph data type, which assumes the vertex names are integers
    between 0 and V - 1.
    It also supports initializing a symbol graph from a file.
    
    This implementation uses an ST to map from strings to integers,
    an array to map from integers to strings, and a Graph to store
    the underlying graph.
    The indexOf and contains operations take time 
    proportional to log V, where V is the number of vertices.
    The nameOf operation takes constant time.
    """

    @staticmethod
    def from_file(filename, delimiter):
        pass

    # private ST<String, Integer> st;  # string -> index
    # private String[] keys;           # index  -> string
    # private Graph graph;             # the underlying graph

    # /**  
    #  * Initializes a graph from a file using the specified delimiter.
    #  * Each line in the file contains
    #  * the name of a vertex, followed by a list of the names
    #  * of the vertices adjacent to that vertex, separated by the delimiter.
    #  * @param filename the name of the file
    #  * @param delimiter the delimiter between fields
    #  */
    # SymbolGraph(String filename, String delimiter) {
    #     st = new ST<String, Integer>();

    #     # First pass builds the index by reading strings to associate
    #     # distinct strings with an index
    #     In in = new In(filename);
    #     # while (in.hasNextLine()) {
    #     while (!in.isEmpty()) {
    #         String[] a = in.readLine().split(delimiter);
    #         for (int i = 0; i < a.length; i++) {
    #             if (!st.contains(a[i]))
    #                 st.put(a[i], st.size());
    #         
    #     
    #     StdOut.println("Done reading " + filename);

    #     # inverted index to get string keys in an aray
    #     keys = new String[st.size()];
    #     for (String name : st.keys()) {
    #         keys[st.get(name)] = name;
    #     

    #     # second pass builds the graph by connecting first vertex on each
    #     # line to all others
    #     graph = new Graph(st.size());
    #     in = new In(filename);
    #     while (in.hasNextLine()) {
    #         String[] a = in.readLine().split(delimiter);
    #         int v = st.get(a[0]);
    #         for (int i = 1; i < a.length; i++) {
    #             int w = st.get(a[i]);
    #             graph.addEdge(v, w);
    
    def contains(self, s):
        """
        Does the graph contain the vertex named s?

        :param s: the name of a vertex
        :return:s true if s is the name of a vertex, and false otherwise        
        """
        return self._st.contains(s)

    def indexOf(self, s):
        """
        Returns the integer associated with the vertex named s.
        :param s: the name of a vertex
        :returns: the integer (between 0 and V - 1) associated with the vertex named s
        """
        return self._st.get(s)
    
    def nameOf(self, v):
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