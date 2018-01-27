# Created for BADS 2018
# see README.md for details
# Python 3


"""
The BST class represents an ordered symbol table of generic
key-value pairs.

This implementation uses an unbalanced, binary search tree.

For additional details and documentation, see Section 3.2 of Algorithms,
4th Edition by Robert Sedgewick and Kevin Wayne.

:original author: Robert Sedgewick and Kevin Wayne
:original java code: https://algs4.cs.princeton.edu/32bst/BST.java.html

"""

# Missing methods:
# ceiling, select, rank, size (or rather, range_size)

class BST:
    def __init__(self):
        """
        Initialises empty symbol table
        """
        self._root = None           # root of BST

    class Node:
        def __init__(self, key, value, size):
            self.left = None       # root of left subtree
            self.right = None      # root of right subtree
            self.key = key         # sorted by key
            self.value = value     # associated data
            self.size = size       # number of nodes in subtree

    def is_empty(self):
        """
        Returns true if this symbol table is empty
        """
        return self.size() == 0

    def contains(self, key):
        """
        Does this symbol table contain the given key?
        :param key: the key to search for
        :return boolean: true if symbol table contains key, false otherwise
        """
        return self.get(key) != None

    def size(self):
        """
        Returns the number of key-value pairs in this symbol table
        """
        return self._size(self._root)
        
    def __len__(self):
        return self.size()

    def _size(self, node):
        """
        Returns the number of key-value pairs in BST rooted at node

        :param node: The node which act as root
        """
        if node == None:
            return 0
        return node.size

    def get(self, key):
        """
        Returns the value associated with the given key

        :param key: The key whose value is returned
        :return: the value associated with the given key if the key
        is in the symbol table, None otherwise
        """
        return self._get(self._root, key)

    def _get(self, node, key):
        if node == None:
            return None
        if key < (node.key):
            return self._get(node.left, key)
        elif key > (node.key):
            return self._get(node.right, key)
        else:
            return node.value

    def put(self, key, value):
        """
        Inserts the specified key-value pair into the symbol table,
        overwriting the old value with the new value if the symbol table
        already contains the specified key. Deletes the specified key (and
        its associated value) from this symbol table if the specified value
        is None.

        :param key, value: the key-value pair to be inserted
        """
        if value == None:
            self.delete(key)
            return
        self._root = self._put(self._root, key, value)

    def _put(self, node, key, value):
        if node == None:
            return self.Node(key, value, 1)
        if key < (node.key):
            node.left = self._put(node.left, key, value)
        elif key > (node.key):
            node.right = self._put(node.right, key, value)
        else:
            node.value = value
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def delete_min(self):
        """
        Removes the smalles key and associated value from the symbol table
        """
        self._root = self._delete_min(self._root)

    def _delete_min(self, node):
        if node.left == None:
            return node.right
        node.left = self._delete_min(node.left)
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def delete_max(self):
        """
        Removes the largest key and associated value from the symbol table
        """
        self._root = delete_max(self._root)

    def _delete_max(self, node):
        if node.right == None:
            return node.left
        node.right = self._delete_max(node.right)
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node


    def delete(self, key):
        """
        Removes the specified key and its associated value from this symbol table
        (if the key is in this symbol table)
        """
        self._root = self._delete(self._root, key)

    def _delete(self, node, key):
        if node == None:
            return None
        if key.__lt__(node.key):
            node.left = self._delete(node.left, key)
        elif key.__gt__(nodet.key):
            node.right = self._delete(node.right, key)
        else:
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right
            temp_node = node
            node = self._min(temp_node.right)
            node.right = self._delete_min(temp_node.right)
            node.left = temp_node.left

        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def min(self):
        """
        Returns the smallest key in the BST
        """
        return self._min(self._root).key

    def _min(self, node):
        if node.left == None:
            return node
        return self._min(node.left)

    def max(self):
        """
        Returns the larget key in the symbol table
        """
        return self._max(self._root).key

    def _max(self, node):
        if node.right == None:
            return node
        return self._max(node.right)

    def floor(self, key):
        """
        Returns the largest key in the symbol table less than or equal to key
        """
        node = self._floor(self._root, key)
        if node == None:
            return None
        return none.key

    def _floor(self, node, key):
        if node == None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return self._floor(node.left, key)
        temp_node = self._floor(node.right, key)
        if not temp_node == None:
            return temp_node
        return node

    def keys(self):
        """
        Returns all keys in the symbol table as a list.
        """
        if self.is_empty():
            return []
        return self.range_keys(self.min(), self.max())

    def range_keys(self, lo, hi):
        """
        Returns all keys in the symbol table in the given range as a list

        :param lo: minimum endpoint
        :param hi: maximum endpoint
        :return: all keys in symbol table between lo (inclusive) and hi (inclusive)
        """
        queue = []
        self._range_keys(self._root, queue, lo, hi)
        return queue

    def _range_keys(self, node, queue, lo, hi):
        if node == None:
            return
        if lo < node.key:
            self._range_keys(node.left, queue, lo, hi)
        if lo <= node.key and hi >= node.key:
            queue.append(node.key)
        if hi > node.key:
            self._range_keys(node.right, queue, lo, hi)



    def height(self):
        """
        Returns the height of the BST (for debugging)
        """
        return self._height(self._root)

    def _height(self, node):
        if node == None:
            return -1
        return 1 + max(self._height(node.left), self._height(node.right))

    def level_order(self):
        """
        Returns the keys in the BST in level order (for debugging)
        """
        queue, keys = [], []
        queue.append(self._root)
        while len(queue) > 0:
            node = queue.pop(0)
            if node == None:
                continue
            keys.append(node.key)
            queue.append(node.left)
            queue.append(node.right)
        return keys


# This is ugly but necessary to use stdlib
# Need to find a better way of doing it
import sys
sys.path.append("..")
from algs4.stdlib import stdio

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            sys.stdin = open(sys.argv[1])
        except IOError:
            print("File not found, using standard input instead")

    data = stdio.readAllStrings()
    st = BST()
    i = 0
    for key in data:
        st.put(key, i)
        i += 1

    print("LEVELORDER:")
    for key in st.level_order():
        print(str(key) + " " + str(st.get(key)))

    print()

    print("KEYS:")
    for key in st.keys():
        print(str(key) + " " + str(st.get(key)))






