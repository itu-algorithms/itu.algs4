import random
import unittest

from algs4.errors.errors import NoSuchElementException
from algs4.searching.red_black_bst import RedBlackBST


class TestRedBlackBSTMethods(unittest.TestCase):
    def setUp(self):
        self.st = RedBlackBST()

    def test_empty(self):
        self.assertTrue(self.st.is_empty())
        self.st.put("spam", 0)
        self.assertFalse(self.st.is_empty())

    def test_size(self):
        for i in range(10):
            self.assertEqual(i, self.st.size())
            self.st.put(str(i), i)

        for i in range(10):
            self.assertEqual(10, self.st.size())
            self.st.put(str(i), i + 1)  # key already there: no change in size

        for i in reversed(range(10)):
            self.assertEqual(i + 1, self.st.size())
            self.st.delete(str(i))

        self.assertEqual(0, self.st.size())

    def test_rank_select(self):
        for i in range(0, 2 ** 8 + 2, 2):
            self.st.put(i, i)
            self.assertEqual(0, self.st.min())
            self.assertEqual(i, self.st.max())
            self.assertEqual(i, self.st.select(i // 2))
            self.assertEqual(i // 2, self.st.rank(i))

    def test_floor_and_ceiling(self):
        self.st.put(0, 0)
        self.st.put(2, 2)
        self.assertEqual(0, self.st.floor(0))
        self.assertEqual(0, self.st.floor(1))
        self.assertEqual(2, self.st.floor(2))
        self.assertEqual(2, self.st.floor(3))
        self.assertEqual(0, self.st.ceiling(-1))
        self.assertEqual(0, self.st.ceiling(0))
        self.assertEqual(2, self.st.ceiling(1))
        self.assertEqual(2, self.st.ceiling(2))

    def test_exceptions(self):
        with self.assertRaises(NoSuchElementException):
            self.st.min()
        with self.assertRaises(NoSuchElementException):
            self.st.max()
        with self.assertRaises(NoSuchElementException):
            self.st.floor(0)
        with self.assertRaises(NoSuchElementException):
            self.st.ceiling(0)
        self.st.put(0, 0)
        with self.assertRaises(NoSuchElementException):
            self.st.floor(-1)
        with self.assertRaises(NoSuchElementException):
            self.st.ceiling(1)


class LargerRedBlackBSTMethods(unittest.TestCase):
    L = [1, 3, 6, 7, 10, 13, 16]

    def setUp(self):
        self.st = RedBlackBST()
        for x in self.L:
            self.st.put(x, x)

    def test_put_and_get(self):
        st = self.st
        for x in st.keys():
            self.assertEqual(st.get(x), x)
        for x in st.keys():
            st.put(x, st.get(x) - 1)
        for x in st.keys():
            self.assertEqual(st.get(x), x - 1)
        self.assertIsNone(st.get(2))
        st.put(2, 2)
        self.assertEqual(2, st.get(2))

    def test_keys(self):
        i = 0
        for k in self.st.keys():
            self.assertEqual(k, self.L[i])
            i += 1

    def test_min(self):
        self.assertEqual(self.st.min(), min(self.L))

    def test_max(self):
        self.assertEqual(self.st.max(), max(self.L))

    def test_delete_min(self):
        self.st.delete_min()
        self.assertEqual(self.st.min(), min(self.L[1:]))

    def test_delete_max(self):
        self.st.delete_max()
        self.assertEqual(self.st.max(), max(self.L[:-1]))

    def test_range(self):
        T = [6, 7, 10, 13]
        i = 0
        for k in self.st.keys_range(5, 13):
            self.assertEqual(k, T[i])
            i += 1


class HugeRedBlackBSTMethods(unittest.TestCase):
    def setUp(self):
        random.seed(0)

        self.L = random.sample(range(10 ** 6), 10 ** 4)
        self.S = sorted(self.L)
        self.st = RedBlackBST()
        for x in self.L:
            self.st.put(x, x)

    def test_put_and_get(self):
        st = self.st
        for x in st.keys():
            self.assertEqual(st.get(x), x)
        for x in st.keys():
            st.put(x, st.get(x) - 1)
        for x in st.keys():
            self.assertEqual(st.get(x), x - 1)

    def test_keys(self):
        i = 0
        for k in self.st.keys():
            self.assertEqual(k, self.S[i])
            i += 1

    def test_min(self):
        self.assertEqual(self.st.min(), min(self.L))

    def test_max(self):
        self.assertEqual(self.st.max(), max(self.L))

    def test_delete_min(self):
        self.st.delete_min()
        self.assertEqual(self.st.min(), min(self.S[1:]))

    def test_delete_max(self):
        self.st.delete_max()
        self.assertEqual(self.st.max(), max(self.S[:-1]))

    def test_min_priority_queue(self):
        i = 0
        while not self.st.is_empty():
            self.assertEqual(self.S[i], self.st.min())
            self.st.delete_min()
            i += 1

    def test_max_priority_queue(self):
        i = len(self.S) - 1
        while not self.st.is_empty():
            self.assertEqual(self.S[i], self.st.max())
            self.st.delete_max()
            i -= 1
