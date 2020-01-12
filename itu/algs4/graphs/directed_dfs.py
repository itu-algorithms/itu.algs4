# Created for BADS 2018
# See README.md for details
# This is python3 
import sys

from itu.algs4.fundamentals.bag import Bag
from itu.algs4.graphs.digraph import Digraph
from itu.algs4.stdlib.instream import InStream


class DirectedDFS:
	"""
	The DirectedDFS class represents a data type for
	determining the vertices reachable from a given source vertex s
	(or a set of source vertices) in a digraph. For versions that find the paths,
	see DepthFirstDirectedPaths and BreadthFirstDirectedPaths.

	This implementation uses depth-first search.
	The constructor takes time proportional to V + E (in the worst case),
	where V is the number of vertices and E is the number of edges.

	For additional documentation, see Section 4.2 of Algorithms,
	4th Edition by Robert Sedgewick and Kevin Wayne.
	"""
	def __init__(self, G, *s):
		"""
		Computes the vertices in digraph G that are
		reachable from the source vertex s.

		:param G: the digraph
		:param s: the source vertex/vertices
		:raises ValueError: unless 0 <= s_ < V for every s_ in s
		"""
		self.marked = [False for i in range(0,G.V())]
		self.reachables = 0
		for s_ in s:
			self._validate_vertex(s_)
			self._dfs(G, s_)

	def _dfs(self, G, v):
		self.reachables += 1
		self.marked[v] = True
		for w in G.adj(v):
			if(not self.marked[w]):
				self._dfs(G, w)

	def is_marked(self, v):
		"""
		Is there a directed path from the source vertex
		and vertex v?

		:param v: the vertex
		:returns: True if there is a directed
		"""
		self._validate_vertex(v)
		return self.marked[v]

	def count(self):
		"""
		Returns the number of vertices reachable from the source vertex
		(or source vertices)
		:returns: the number of vertices reachable from the source vertex
		(or source vertices)
		"""
		return self.reachables

	def _validate_vertex(self, v):
		# Raise a ValueError unless 0 <= v < V
		V = len(self.marked)
		if(v < 0 or v >= V):
			raise ValueError("vertex {} is not between 0 and {}".format(v, V-1))

def main():
	"""
	Unit tests the DirectedDFS data type.
	"""
	G = Digraph.from_stream(InStream(None))
	sources = Bag()
	for i in range(1,len(sys.argv)):
		s = int(sys.argv[i])
		sources.add(s)

	dfs = DirectedDFS(G, *sources)
	print("Reachable vertices:")
	for v in range(0, G.V()):
		if(dfs.is_marked(v)):
			print(v,end=" ")
	print()
if __name__ == '__main__':
	main()
