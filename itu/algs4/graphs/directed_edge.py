import math

from itu.algs4.errors.errors import IllegalArgumentException

# Created for BADS 2018
# See README.md for details
# Python 3


class DirectedEdge:
    """
    The DirectedEdge class represents a weighted edge in an
    EdgeWeightedDigraph. Each edge consists of two integers
    (naming the two vertices) and a real-value weight. The data type
    provides methods for accessing the two endpoints of the directed edge and
    the weight.
    """
    def __init__(self, v, w, weight):
        """
        Initializes a directed edge from vertex v to vertex w with
        the given weight.
        :param v: the tail vertex
        :param w: the head vertex
        :param weight: the weight of the directed edge
        :raises IllegalArgumentException: if either v or w is a negative integer
        :raises IllegalArgumentException: if weight is NaN
        """
        if v < 0:
            raise IllegalArgumentException("Vertex names must be nonnegative integers")
        if w < 0:
            raise IllegalArgumentException("Vertex names must be nonnegative integers")
        if math.isnan(weight):
            raise IllegalArgumentException("Weight is NaN")
        self._v = v
        self._w = w
        self._weight = weight

    def from_vertex(self):
        """
        Returns the tail vertex of the directed edge.
        :return: the tail vertex of the directed edge
        :rtype: int
        """
        return self._v

    def to_vertex(self):
        """
        Returns the head vertex of the directed edge.
        :return: the head vertex of the directed edge
        :rtype: int
        """
        return self._w

    def weight(self):
        """
        Returns the weight of the directed edge.
        :return: the weight of the directed edge
        :rtype: float
        """
        return self._weight

    def __repr__(self):
        """
        Returns a string representation of the directed edge.
        :return: a string representation of the directed edge
        :rtype: str
        """
        return "{}->{} {:5.2f}".format(self._v, self._w, self._weight)


def main():
    """
    Creates a directed edge and prints it.
    :return:
    """
    e = DirectedEdge(12, 34, 5.67)
    print(e)


if __name__ == '__main__':
    main()
