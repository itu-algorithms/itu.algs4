from fundamentals.stack import Stack

class DepthFirstPaths:
    def __init__(self, G, s):
        self._marked = [False] * G.V() # Has dfs been called for this vertex?
        self._edgeTo = [0] * G.V() # last vertex on known path to this vertex
        self._s = s # sourcepublic DepthFirstPathsGraph G, int s
        self._dfs(G, s)

    def _dfs(self, G, v):
        self._marked[v] = True
        for w in G.adj(v):
            if not self._marked[w]:
                self._edgeTo[w] = v
                self._dfs(G, w)

    def has_path_to_point(self, v):
        return self._marked[v]

    def path_to_point(self, v):
        if not self.has_path_to_point(v): return None
        path = Stack()
        w = v
        while w != self._s:
            path.push(w)
            w = self._edgeTo[w]
        path.push(v)

        return path