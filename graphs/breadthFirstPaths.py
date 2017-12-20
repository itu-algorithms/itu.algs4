from fundamentals.stack import Stack
from fundamentals.queue import Queue

class BreadthFirstPaths:
    def __init__(self, G, s):
        self._marked = [False] * G.V()  # Is a shortest path to this vertex known?
        self._edgeTo = [0] * G.V()      # last vertex on known path to this vertex
        self._s = s                     # source
        self._bfs(G, s)

    def _bfs(self, G, s):
        queue = Queue()
        self._marked[s] = True              # Mark the source
        queue.enqueue(s)                    #   and put it on the queue.
        while not queue.is_empty():
            v = queue.dequeue()             # Remove next vertex from the queue.
            for w in G.adj(v):
                if not self._marked[w]:
                    self._edgeTo[w] = v     # For every unmarked adjacent vertex,
                    self._marked[w] = True  # mark it because path is known,
                    queue.enqueue(w)        # and add it to the queue.

    def has_path_to_point(self, v):
        return self._marked[v]

    def path_to_point(self, v):
        if not self.has_path_to_point(v): return None
        path = Stack()
        x = v
        while x != self._s:
            path.push(x)
            x = self._edgeTo[x]
        path.push(self._s)

        return path