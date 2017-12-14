

class BST:
    def __init__(self):
        """
        Initializes empty tree with a root node of value None
        """
        self.root = None

    class Node:
        def __init__(self, key, value, size):
            self.left = None
            self.right = None
            self.key = key
            self.value = value
            self.size = size

    def is_empty(self):
        """
        Returns True iff the BST contains no Nodes (and thus no key-value pairs)
        """
        return self.size() == 0

    def contains(self, key):
        """
        Check if BST contains key
        """
        return self.get(key) != None

    def size(self):
        """
        Returns the size of the entire BST
        """
        return self._size(self.root)

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
        Get the value of key (if the key-value pair exists)

        :param key: The key whose value is returned
        """
        return self._get(self.root, key)

    def _get(self, node, key):
        if node == None:
            return None
        if key.__lt__(node.key):
            return self._get(node.left, key)
        elif key.__gt__(node.key):
            return self._get(node.right, key)
        else:
            return node.value

    def put(self, key, value):
        """
        Inserts a key-value pair into the BST. If value is None and key exists
        then the key and associated value is deleted
        """
        if value == None:
            self.delete(key)
            return
        self.root = self._put(self.root, key, value)

    def _put(self, node, key, value):
        if node == None:
            return self.Node(key, value, 1)
        if key.__lt__(node.key):
            node.left = self._put(node.left, key, value)
        elif key.__gt__(node.key):
            node.right = self._put(node.right, key, value)
        else:
            node.value = value
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def delete(self, key):
        """
        Removes the specified key and its associated value from the BST
        """
        self.root = self._delete(self.root, key)

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
            node = self._min_key(temp_node.right)
            node.right = self._deleteMin(temp_node.right)
            node.left = temp_node.left

        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def deleteMin(self):
        """
        Removes the smalles key and associated value from BST
        """
        self.root = self._deleteMin(self.root)

    def _deleteMin(self, node):
        if node.left == None:
            return node.right
        node.left = self._deleteMin(node.left)
        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

    def min_key(self):
        """
        Returns the smallest key in the BST
        """
        return self._min_key(self.root).key

    def _min_key(self, node):
        if node.left == None:
            return node
        return self._min_key(node.left)






