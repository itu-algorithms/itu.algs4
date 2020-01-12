# Created for BADS 2018
# See README.md for details
# This is python3 

import sys

from itu.algs4.fundamentals.bag import Bag
from itu.algs4.fundamentals.stack import Stack
from itu.algs4.graphs.digraph import Digraph
from itu.algs4.graphs.directed_dfs import DirectedDFS


class NFA:
	"""
	The NFA class provides a data type for creating a
	nondeterministic finite state automaton (NFA) from a regular
	expression and testing whether a given string is matched by that regular
	expression.
	It supports the following operations: concatenation, closure, binary or,
	and parentheses, metacharacters (either in the text or pattern),
	capturing capabilities, greedy or reluctant/lazy modifiers,
	and other features in industrial-strength implementations
	such as Java's Pattern and Matcher.

	This implementation builds the NFA using a digraph and a stack
	and simulates the NFA using digraph search (see the textbook for details).
	The constructor takes time proportional to m, where m is the
	number of characters in the regular expression.
	The recognizes() method takes time proportional to m*n, where n
	is the number of characters in the text.

	For additional documentation, see section 5.4 of Algorithms, 4th Edition
	by Robert Sedgewick and Kevin Wayne.
	"""
	def __init__(self, regex):
		"""
		Initializes the NFA from the specified regular expression.

		:param regex: the regular expression
		"""
		self.regex = regex
		m = len(regex)
		self.m = m
		ops = Stack()
		graph = Digraph(m+1)
		for i in range(0,m):
			lp = i
			if(regex[i] == '(' or regex[i] == '|'):
				ops.push(i)
			elif(regex[i] == ')'):
				or_ = ops.pop()

				# 2-way or operator
				if(regex[or_] == '|'):
					lp = ops.pop()
					graph.add_edge(lp, or_+1)
					graph.add_edge(or_, i)
				elif(regex[or_] == '('):
					lp = or_
				else:
					assert False
			if(i < m-1 and regex[i+1] == '*'):
				graph.add_edge(lp, i+1)
				graph.add_edge(i+1, lp)
			if(regex[i] == '(' or regex[i] == '*' or regex[i] == ')'):
				graph.add_edge(i, i+1)
		if(ops.size() != 0):
			raise ValueError("Invalid regular expression")
		self.graph = graph

	def recognizes(self, txt):
		"""
		Returns True if the text is matched by the regular expression.

		:param txt: the text
		:returns: True if the text is matched by the regular expression;
					False otherwise
		"""
		regex = self.regex
		graph = self.graph
		m = self.m
		dfs = DirectedDFS(graph, 0)
		pc = Bag()
		for v in range(0, graph.V()):
			if(dfs.is_marked(v)):
				pc.add(v)

		#Compute possible NFA states for txt[i+1]
		for i in range(0, len(txt)):
			if(txt[i] == '*' or txt[i] == '|' or txt[i] == '(' or txt[i] == ')'):
				raise ValueError("text contains the metacharacter '{}'".format(txt[i]))
			match = Bag()
			for v in pc:
				if(v == m):
					continue
				if(regex[v] == txt[i] or regex[i] == '.'):
					match.add(v+1)
			dfs = DirectedDFS(graph, *match)
			pc = Bag()
			for v in range(0, graph.V()):
				if(dfs.is_marked(v)):
					pc.add(v)
			# Optimization if no states reachable
			if(pc.size() == 0):
				return False
		for v in pc:
			if(v == m):
				return True
			return False
def main():
	"""
	Unit tests the NFA data type
	"""
	regex = "({})".format(sys.argv[1])
	txt = sys.argv[2]
	nfa = NFA(regex)
	print(nfa.recognizes(txt))
if __name__ == '__main__':
	main()
