class DepthFirstSearch:
    def __init__(self, G, s):
        self._marked = [False] * G.V()
        self._count = 0
        self._dfs(G, s)
    
    def _dfs(self, G, v):
        self._marked[v] = True
        self._count += 1
        for w in G.adj(v):
            if not self._marked[w]:
                self._dfs(G, w)

    def marked(self, w):
        return self._marked[w]

    def count(self):
        return self._count

        