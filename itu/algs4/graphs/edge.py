import math

from itu.algs4.errors.errors import IllegalArgumentException

# Created for BADS 2018
# See README.md for details
# Python 3


class Edge:
    """
    The Edge class represents a weighted edge in an
    EdgeWeightedGraph. Each edge consists of two integers
    (naming the two vertices) and a real-value weight. The data type
    provides methods for accessing the two endpoints of the edge and
    the weight. The natural order for this data type is by
    ascending order of weight.
    """
    def __init__(self, v, w, weight):
        """
        Initializes an edge between vertices v and w of
        the given weight.
        :param v: one vertex
        :param w: the other vertex
        :param weight: the weight of this edge
        :raises IllegalArgumentException: if either v or w is a negative integer
        :raises IllegalArgumentException: if weight is NaN
        """
        if v < 0:
            raise IllegalArgumentException("vertex index must be a nonnegative integer")
        if w < 0:
            raise IllegalArgumentException("vertex index must be a nonnegative integer")
        if math.isnan(weight):
            raise IllegalArgumentException("Weight is NaN")
        self._v = v
        self._w = w
        self._weight = weight

    def weight(self):
        """
        Returns the weight of this edge.
        :return: the weight of this edge
        :rtype: float
        """
        return self._weight

    def either(self):
        """
        Returns either endpoint of this edge.
        :return: either endpoint of this edge
        :rtype: int
        """
        return self._v

    def other(self, vertex):
        """
        Returns the endpoint of this edge that is different from the given vertex.
        :param vertex: one endpoint of this edge
        :return: the other endpoint of this edge
        :rtype: int
        :raises IllegalArgumentException: if the vertex is not one of the endpoints of this edge
        """
        if vertex == self._v:
            return self._w
        elif vertex == self._w:
            return self._v
        else:
            raise IllegalArgumentException("Illegal endpoint")

    def __lt__(self, other):
        """
        Checks if this edge has smaller weight than other edge
        :param other: the edge to compare with
        :return: True if weight of this edge is less than weight of other edge otherwise returns False
        """
        return self.weight() < other.weight()

    def __gt__(self, other):
        """
        Checks if this edge has greater weight than other edge
        :param other: the edge to compare with
        :return: True if weight of this edge is greater than weight of other edge otherwise returns False
        """
        return self.weight() > other.weight()

    def __repr__(self):
        """
        Returns a string representation of this edge.
        :return: a string representation of this edge
        """
        return "{}-{} {:.5f}".format(self._v, self._w, self._weight)


def main():
    """
    Creates an edge and prints it.
    """
    e = Edge(12, 34, 5.67)
    print(e)


if __name__ == '__main__':
    main()
