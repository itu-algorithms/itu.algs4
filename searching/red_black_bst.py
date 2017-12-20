class RedBlackBST:

    RED = True
    BLACK = False

    class Node:
        def __init__(self, key, val, size):
            self.key = key
            self.val = val
            self.left = None
            self.right = None
            self.size = size
            self.color = RedBlackBST.RED

    def __init__(self):
        self.root = None

    def put(self, key, val):
        self.root = self._put(self.root, key, val)

    def _put(self, h, key, val):
        if h is None:
            return self.Node(key, val, 1)
        if key < h.key:
            h.left = self._put(h.left, key, val)
        elif key > h.key:
            h.right = self._put(h.right, key, val)
        else:
            h.val = val

        if RedBlackBST._is_red(h.right) and RedBlackBST._is_red(h.left):
            h = RedBlackBST._rotate_left(h)
        if RedBlackBST._is_red(h.left) and RedBlackBST._is_red(h.left.left):
            h = RedBlackBST._rotate_right(h)
        if RedBlackBST._is_red(h.left) and RedBlackBST._is_red(h.right):
            RedBlackBST._flip_colors(h)

        h.size = self._size(h.left) + self._size(h.right) + 1

        return h

    def get(self, key):
        curr = self.root
        while curr is not None:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return None

    def size(self):
        return red_black_bst._size(self.root)

    def contains(self, key):
        return self.get(key) is not None

    @staticmethod
    def _size(x):
        if x is None:
            return 0
        return x.size

    @staticmethod
    def _is_red(h):
        if h is None:
            return RedBlackBST.BLACK
        return h.color

    @staticmethod
    def _rotate_left(h):
        x = h.right
        h.right = x.left
        x.left = h
        x.color = h.color
        h.color = RedBlackBST.RED
        return x

    @staticmethod
    def _rotate_right(h):
        x = h.left
        h.left = x.right
        x.right = h
        x.color = h.color
        h.color = RedBlackBST.RED
        return x

    @staticmethod
    def _flip_colors(h):
        h.color = RedBlackBST.RED
        h.left.color = RedBlackBST.BLACK
        h.right.color = RedBlackBST.BLACK


if __name__ == '__main__':
    red_black_bst = RedBlackBST()

    for i in range(65, 91):
        red_black_bst.put(i, chr(i))

    for i in range(65, 91):
        print (red_black_bst.get(i))
