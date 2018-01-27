import sys
from algs4.stdlib import stdio
from algs4.fundamentals.queue import Queue
from algs4.errors.errors import NoSuchElementException, IllegalArgumentException

# Created for BADS 2018
# See README.md for details
# Python 3


class RedBlackBST:
    """
    The RedBlackBST class represents an ordered symbol table of generic
    key-value pairs.
    It supports the usual put, get, contains,
    delete, size, and is-empty methods.
    It also provides ordered methods for finding the minimum,
    maximum, floor, and ceiling.
    It also provides a keys method for iterating over all the keys.
    A symbol table implements the associative array abstraction:
    when associating a value with a key that is already in the symbol table,
    the convention is to replace the old value with the new value.
    This class uses the convention that values cannot be None-setting the
    value associated with a key to None is equivalent to deleting the key from the symbol table.
    This implementation uses a left-leaning red-black BST. It requires that
    the keys are all of the same type and that they can be compared.
    The put, contains, remove, minimum, maximum, ceiling, and floor operations each take
    logarithmic time in the worst case, if the tree becomes unbalanced.
    The size, and is-empty operations take constant time.
    Construction takes constant time.
    """

    RED = True
    BLACK = False

    class Node:
        """
        RedBlackBST helper node data type.
        """
        def __init__(self, key, val, color, size):
            """
            Initializes a new node.
            :param key: the key of the node
            :param val: the value of the node
            :param size: the subtree count
            """
            self.key = key
            self.val = val
            self.left = None
            self.right = None
            self.size = size
            self.color = color

    def __init__(self):
        """
        Initializes an empty symbol table.
        """
        self._root = None

    def put(self, key, val):
        """
        Inserts the specified key-value pair into the symbol table, overwriting the old
        value with the new value if the symbol table already contains the specified key.
        Deletes the specified key (and its associated value) from this symbol table
        if the specified value is None.
        :param key: the key
        :param val: the value
        :raises IllegalArgumentException: if key is None
        """
        if key is None:
            raise IllegalArgumentException("first argument to put() is None")
        if val is None:
            self.delete(key)
            return

        self._root = self._put(self._root, key, val)
        self._root.color = self.BLACK

    def _put(self, h, key, val):
        """
        Inserts the key-value pair in the subtree rooted at h.
        :param h: root of currently inspected subtree
        :param key: the key
        :param val: the value
        """
        if h is None:
            return self.Node(key, val, self.RED, 1)
        if key < h.key:
            h.left = self._put(h.left, key, val)
        elif key > h.key:
            h.right = self._put(h.right, key, val)
        else:
            h.val = val

        if self._is_red(h.right) and not self._is_red(h.left):
            h = self._rotate_left(h)
        if self._is_red(h.left) and self._is_red(h.left.left):
            h = self._rotate_right(h)
        if self._is_red(h.left) and self._is_red(h.right):
            self._flip_colors(h)

        h.size = self._size(h.left) + self._size(h.right) + 1

        return h

    def get(self, key):
        """
        Returns the value associated with the given key.
        :param key: the key
        :return: the value associated with the given key if the key is in the symbol table
        and None if the key is not in the symbol table
        :raises IllegalArgumentException: if key is None
        """
        if key is None:
            raise IllegalArgumentException("argument to get() is None")

        return self._get(self._root, key)

    def _get(self, x, key):
        """
        Returns value with the given key in subtree rooted at x.
        None if no such key.
        :param x: root of currently inspected subtree.
        :param key: the key
        :return: value associated with given key. None if no such key
        """
        while x is not None:
            if key < x.key:
                x = x.left
            elif key > x.key:
                x = x.right
            else:
                return x.val
        return None

    def delete_min(self):
        """
        Removes the smallest key and associated value from the symbol table.
        :raises NoSuchElementException: if the symbol table is empty
        """
        if self.is_empty():
            raise NoSuchElementException("RedBlackBST underflow")
        if not self._is_red(self._root.left) and not self._is_red(self._root.right):
            self._root.color = self.RED
        self._root = self._delete_min(self._root)
        if not self.is_empty():
            self._root.color = self.BLACK

    def _delete_min(self, h):
        """
        Deletes the node with the minimum key rooted at h.
        :rtype: Node
        """
        if h.left is None:
            return None
        if not self._is_red(h.left) and not self._is_red(h.left.left):
            h = self._move_red_left(h)
        h.left = self._delete_min(h.left)
        return self._balance(h)

    def delete_max(self):
        """
        Removes the largest key and associated value from the symbol table.
        :raises NoSuchElementException: if the symbol table is empty
        """
        if self.is_empty():
            raise NoSuchElementException("RedBlackBST underflow")
        if not self._is_red(self._root.left) and not self._is_red(self._root.right):
            self._root.color = self.RED
        self._root = self._delete_max(self._root)
        if not self.is_empty():
            self._root.color = self.BLACK

    def _delete_max(self, h):
        """
        Deletes the key-value pair with the maximum key rooted at h
        :rtype: Node
        """
        if self._is_red(h.left):
            h = self._rotate_right(h)
        if h.right is None:
            return None
        if not self._is_red(h.right) and not self._is_red(h.right.left):
            h = self._move_red_right(h)
        h.right = self._delete_max(h.right)
        return self._balance(h)

    def delete(self, key):
        """
        Removes the specified key and its associated value from this symbol table
        (if the key is in this symbol table).
        :param key: the key
        :raises IllegalArgumentException: if key is None
        """
        if key is None:
            raise IllegalArgumentException("argument to delete() is None")
        if not self.contains(key):
            return
        if not self._is_red(self._root.left) and not self._is_red(self._root.right):
            self._root.color = self.RED
        self._root = self._delete(self._root, key)
        if not self.is_empty():
            self._root.color = self.BLACK

    def _delete(self, h, key):
        """
        Deletes the key-value pair with the given key rooted at h.
        :rtype: Node
        """
        if key < h.key:
            if not self._is_red(h.left) and not self._is_red(h.left.left):
                h = self._move_red_left(h)
            h.left = self._delete(h.left, key)
        else:
            if self._is_red(h.left):
                h = self._rotate_right(h)
            if key == h.key and h.right is None:
                return None
            if not self._is_red(h.right) and not self._is_red(h.right.left):
                h = self._move_red_right(h)
            if key == h.key:
                x = self._min(h.right)
                h.key = x.key
                h.val = x.val
                h.right = self._delete_min(h.right)
            else:
                h.right = self._delete(h.right, key)
        return self._balance(h)

    def size(self):
        """
        Return the number of key-value pairs in this symbol table.
        :return: the number of key-value pairs in this symbol table
        :rtype: int
        """
        return self._size(self._root)

    def __len__(self):
        return self.size()

    def _size(self, x):
        """
        Number of nodes in subtree rooted at x. 0 if x is None
        :param x: root node of subtree
        :return: number of nodes in subtree
        :rtype: int
        """
        if x is None:
            return 0
        return x.size

    def contains(self, key):
        """
        Does this symbol table contain the given key?
        :param key: the key
        :return: True if this symbol table contains key and False otherwise
        :rtype: bool
        """
        return self.get(key) is not None

    def is_empty(self):
        """
        Is this symbol table empty?
        :return: True if this symbol table is empty and False otherwise
        :rtype: bool
        """
        return self._root is None

    def _is_red(self, x):
        """
        Is node x red?
        :param x: the node to check
        :return: True if node is red False otherwise
        :rtype: bool
        """
        if x is None:
            return self.BLACK
        return x.color

    def _rotate_left(self, h):
        """
        Make a right-leaning link lean to the left
        :param h:
        :return: The node that has taken h's position
        :rtype: Node
        """
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = self.RED
        x.size = h.size
        h.size = self._size(h.left) + self._size(h.right) + 1
        return x

    def _rotate_right(self, h):
        """
        Make a left-leaning link lean to the right.
        :param h:
        :return: The node that has taken h's position
        :rtype: Node
        """
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = self.RED
        x.size = h.size
        h.size = self._size(h.left) + self._size(h.right) + 1
        return x

    def _flip_colors(self, h):
        """
        Flip the colors of a node and its two children.
        :param h: the node
        """
        h.color = not h.color
        h.left.color = not h.left.color
        h.right.color = not h.right.color

    def _move_red_left(self, h):
        """
        Assuming that h is red and both h.left and h.left.left
        are black, make h.left or one of its children red.
        :rtype: Node
        """
        self._flip_colors(h)
        if self._is_red(h.right.left):
            h.right = self._rotate_right(h.right)
            h = self._rotate_left(h)
            self._flip_colors(h)
        return h

    def _move_red_right(self, h):
        """
        Assuming that h is red and both h.right and h.right.left
        are black, make h.right or one of its children red.
        :rtype: Node
        """
        self._flip_colors(h)
        if self._is_red(h.left.left):
            h = self._rotate_right(h)
            self._flip_colors(h)
        return h

    def _balance(self, h):
        """
        Restore red-black tree invariant
        :rtype: Node
        """
        if self._is_red(h.right):
            h = self._rotate_left(h)
        if self._is_red(h.left) and self._is_red(h.left.left):
            h = self._rotate_right(h)
        if self._is_red(h.left) and self._is_red(h.right):
            self._flip_colors(h)
        h.size = self._size(h.left) + self._size(h.right) + 1
        return h

    def height(self):
        """
        Returns the height of the RedBlackBST
        :return: the height of the RedBlackBST (a 1-node tree has height 0)
        :rtype: int
        """
        return self._height(self._root)

    def _height(self, x):
        """
        Returns height of subtree rooted at x.
        :rtype: int
        """
        if x is None:
            return -1
        return 1 + max(self._height(x.left), self._height(x.right))

    def min(self):
        """
        Returns the smallest key in the symbol table.
        :return: the smallest key in the symbol table
        :raises NoSuchElementException: if the symbol table is empty
        """
        if self.is_empty():
            raise NoSuchElementException("calls min() with empty symbol table")
        return self._min(self._root).key

    def _min(self, x):
        """
        Returns the smallest key in subtree rooted at x. None if no such key
        :rtype: Node
        """
        if x.left is None:
            return x
        else:
            return self._min(x.left)

    def max(self):
        """
        Returns the largest key in the symbol table.
        :return: the largest key in the symbol table
        :raises NoSuchElementException: if the symbol table is empty
        """
        if self.is_empty():
            raise NoSuchElementException("calls max() with empty symbol table")
        return self._max(self._root).key

    def _max(self, x):
        """
        Returns the largest key in subtree rooted at x. None if no such key.
        :rtype: Node
        """
        if x.right is None:
            return x
        return self._max(x.right)

    def keys(self):
        """
        Returns all keys in the symbol table.
        :return: all keys in the symbol table
        """
        if self.is_empty():
            return Queue()
        return self.keys_range(self.min(), self.max())

    def keys_range(self, lo, hi):
        """
        Returns all keys in the symbol table in the given range.
        :param lo: minimum endpoint
        :param hi: maximum endpoint
        :return: all keys in the symbol table between lo (inclusive) and hi (inclusive)
        :raises IllegalArgumentException: if either lo or hi is None
        """
        if lo is None:
            raise IllegalArgumentException("first argument to keys() is None")
        if hi is None:
            raise IllegalArgumentException("second argument to keys() is None")
        queue = Queue()
        self._keys(self._root, queue, lo, hi)
        return queue

    def _keys(self, x, queue, lo, hi):
        """
        Adds the keys between lo and hi in the subtree rooted at x
        to the queue.
        """
        if x is None:
            return
        if lo < x.key:
            self._keys(x.left, queue, lo, hi)
        if lo <= x.key <= hi:
            queue.enqueue(x.key)
        if hi > x.key:
            self._keys(x.right, queue, lo, hi)

    def select(self, k):
        """
        Return the kth smallest key in the symbol table.
        :param k: the order statistic
        :return: the kth smallest key in the symbol table
        :raises IllegalArgumentException: unless k is between 0 and n-1
        """
        if k < 0 or k >= self.size():
            raise IllegalArgumentException("argument to select() is invalid: {}".format(k))
        x = self._select(self._root, k)
        return x.key

    def _select(self, x, k):
        """
        Returns the node with key of rank k in the subtree rooted at x
        :rtype: Node
        """
        t = self._size(x.left)
        if t > k:
            return self._select(x.left, k)
        elif t < k:
            return self._select(x.right, k-t-1)
        else:
            return x

    def rank(self, key):
        """
        Returns the number of keys in the symbol table strictly less than key.
        :param key: the key
        :return: the number of keys in the symbol table strictly less than key
        :rtype: int
        :raises IllegalArgumentException: if key is None
        """
        if key is None:
            raise IllegalArgumentException("argument to rank() is None")
        return self._rank(key, self._root)

    def _rank(self, key, x):
        """
        Returns the number of keys less than key in the subtree rooted at x.
        :rtype: int
        """
        if x is None:
            return 0
        if key < x.key:
            return self._rank(key, x.left)
        if key > x.key:
            return 1 + self._size(x.left) + self._rank(key, x.right)
        else:
            return self._size(x.left)

    def size_range(self, lo, hi):
        """
        Returns the number of keys in the symbol table in the given range.
        :param lo: minimum endpoint
        :param hi: maximum endpoint
        :return: the number of keys in the symbol table between lo
        (inclusive) and hi (inclusive)
        :rtype: int
        :raises IllegalArgumentException: if either lo or hi is None
        """
        if lo is None:
            return IllegalArgumentException("first argument to size() is None")
        if hi is None:
            return IllegalArgumentException("second argument to size() is None")
        if lo > hi:
            return 0
        if self.contains(hi):
            return self.rank(hi) - self.rank(lo) + 1
        else:
            return self.rank(hi) - self.rank(lo)

    def floor(self, key):
        """
        Returns the largest key in the symbol table less than or equal to key.
        :param key: the key
        :return: the largest key in the symbol table less than er equal to key
        :raises IllegalArgumentException: if key is None
        :raises NoSuchElementException: if there is no such key
        """
        if key is None:
            raise IllegalArgumentException("argument to floor() is None")
        if self.is_empty():
            raise NoSuchElementException("calls floor() with empty symbol table")
        x = self._floor(self._root, key)
        if x is None:
            return None
        return x.key

    def _floor(self, x, key):
        """
        Returns the largest key in the subtree rooted at x less than or equal to the given key.
        """
        if x is None:
            return None
        if key == x.key:
            return x
        if key < x.key:
            return self._floor(x.left, key)
        t = self._floor(x.right, key)
        if t is not None:
            return t
        return x

    def ceiling(self, key):
        """
        Returns the smallest key in the symbol table greater than or equal to key.
        :param key: the key
        :return: the smallest key in the symbol table greater than or equal to key
        :raises IllegalArgumentException: if key is None
        :raises NoSuchElementException: if there is no such key
        """
        if key is None:
            raise IllegalArgumentException("argument to ceiling is None")
        if self.is_empty():
            raise NoSuchElementException("calls ceiling() with empty symbol table")
        x = self._ceiling(self._root, key)
        if x is None:
            return None
        return x.key

    def _ceiling(self, x, key):
        """
        Returns the node with the smallest key in the subtree rooted at x greater than or equal to the given key
        :rtype: Node
        """
        if x is None:
            return None
        if key == x.key:
            return x
        if key > x.key:
            return self._ceiling(x.right, key)
        t = self._ceiling(x.left, key)
        if t is not None:
            return t
        return x


def main():
    """
    Reads strings from stdin, adds them to a red-black BST with values 0..n,
    prints all key value pairs to stdout.
    """
    st = RedBlackBST()
    i = 0
    while not stdio.isEmpty():
        key = stdio.readString()
        st.put(key, i)
        i += 1
    for s in st.keys():
        print("{} {}".format(s, st.get(s)))
    print()


if __name__ == '__main__':
    main()
