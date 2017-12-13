from bag import Bag

class Graph:
    def __init__(self, V):
        self._V = V
        self._E = 0
        self._adj = []

        for _ in range(V):
            self._adj.append(Bag())

    def V(self):
        return self._V

    def E(self):
        return self._E

    def _validateVertex(self, v):
        if v < 0 or v >= self._V:
            raise ValueError("vertex %d is not between 0 and %d" % (v, self._V))

    def addEdge(self, v, w):
        self._validateVertex(v)
        self._validateVertex(w)
        self._E += 1
        self._adj[v].add(w)
        self._adj[w].add(v)

    def adj(self, v):
        self._validateVertex(v)
        return self._adj[v]

    def degree(self, v):
        self._validateVertex(v)
        return self._adj[v].size()

    def __repr__(self):
        s = ["%d vertices, %d edges\n"%(self._V, self._E)]
        for v in range(self._V):
            s.append("%d : " % (v))
            for w in self._adj[v]:
                s.append("%d " % (w))
            s.append("\n")

        return ''.join(s)
