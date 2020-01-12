from itu.algs4.fundamentals.queue import Queue
from itu.algs4.fundamentals.stack import Stack
from itu.algs4.graphs.digraph import Digraph


class DepthFirstOrder:
    """
    The DepthFirstOrder class represents a data type for determining depth-first 
    search ordering of the vertices in a digraph or edge-weighted digraph, including 
    preorder, postorder, and reverse postorder.
    
    This implementation uses depth-first search. The constructor takes time proportional 
    to V + E (in the worst case), where V is the number of vertices and E is the number 
    of edges. Afterwards, the preorder, postorder, and reverse postorder operation takes 
    take time proportional to V.

    For additional documentation, see Section 4.2 of Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.
    """
    
    def __init__(self, digraph):
        """
        Determines a depth-first order for the digraph.
        
        :param digraph: the digraph to check
        """
        self._pre  = [0]*digraph.V()
        self._post = [0]*digraph.V()
        self._preorder  = Queue()
        self._postorder = Queue()
        self._marked = [False]*digraph.V()
        
        self._pre_counter  = 0
        self._post_counter = 0
        
        if isinstance(digraph, Digraph):
            dfs = self._dfs
        else:
            dfs = self._dfs_edge_weighted
        
        for v in range(digraph.V()):
            if (not self._marked[v]):
                dfs(digraph, v)
    
    def post(self, v=None):
        """
        Either returns the postorder number of vertex v or, if v is None, 
        returns the vertices in postorder.
        
        :param v: None, or the vertex to return the postorder number of
        :return: if v is None, the vertices in postorder, otherwise the postorder
        number of v
        """
        if v is None:
            return self._postorder
        else:
            self._validate_vertex(v)
            return self._post[v]
    
    def pre(self, v=None):
        """
        Either returns the preorder number of vertex v or, if v is None, 
        returns the vertices in preorder.
        
        :param v: None, or the vertex to return the preorder number of
        :return: if v is None, the vertices in preorder, otherwise the preorder
                number of v
        """
        if v is None:
            return self._preorder
        else:
            self._validate_vertex(v)
            return self._pre[v]    
        
    def reverse_post(self):
        """
        Returns the vertices in reverse postorder.
        
        :return: the vertices in reverse postorder, as an iterable of vertices
        """
        reverse = Stack()
        for v in self._postorder:
            reverse.push(v)
        return reverse
    
    # run DFS in digraph G from vertex v and compute preorder/postorder
    def _dfs(self, digraph, v):
        self._marked[v] = True
        self._pre[v] = self._pre_counter
        self._pre_counter += 1
        self._preorder.enqueue(v)
        for w in digraph.adj(v):
            if not self._marked[w]:
                self._dfs(digraph, w)
        self._postorder.enqueue(v)
        self._post[v] = self._post_counter
        self._post_counter += 1
    
    # run DFS in edge-weighted digraph G from vertex v and compute preorder/postorder
    def _dfs_edge_weighted(self, graph, v):
        self._marked[v] = True
        self._pre[v] = self._pre_counter
        self._pre_counter += 1
        self._preorder.enqueue(v)
        for edge in graph.adj(v):
            w = edge.to_vertex()
            if not self._marked[w]:
                self._dfs_edge_weighted(graph, w)
        self._postorder.enqueue(v)
        self._post[v] = self._post_counter
        self._post_counter += 1    
    
    # throw an IllegalArgumentException unless 0 <= v < V
    def _validate_vertex(self, v):
        V = len(self._marked)
        if v < 0 or v >= V:
            raise ValueError("vertex {} is not between 0 and {}", v, V-1)
    
    # check that pre() and post() are consistent with pre(v) and post(v)
    def _check(self):
        # check that post(v) is consistent with post()
        r = 0
        for v in self.post():
            if self.post(v) != r:
                print("post(v) and post() inconsistent")
                return False
            r += 1

        # check that pre(v) is consistent with pre()
        r = 0
        for v in self.pre():
            if self.pre(v) != r:
                print("pre(v) and pre() inconsistent")
                return False
            r += 1

        return True
