class DepthFirstPaths:
    def __init__(self, G, s):
        self._marked = [False] * G.V() # Has dfs been called for this vertex?
        self._edgeTo = [0] * G.V() # last vertex on known path to this vertex
        self.s = s # sourcepublic DepthFirstPathsGraph G, int s
        self._dfs(G, s)

    def _dfs(self, G, v):
        self._marked[v] = True
        for w in G.adj(v):
            if not self._marked[w]:
                self._edgeTo[w] = v
                self._dfs(G, w)

    def hasPathToPoint(self, v):
        return self._marked[v]

    def pathToPoint(self, v):
        w = v
        while w != self.s:
            w = self._edgeTo[w]
            yield w 