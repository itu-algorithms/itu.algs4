# import random
#
import pytest

from itu.algs4.searching.binary_search_st import BinarySearchST
from itu.algs4.searching.bst import BST
from itu.algs4.searching.linear_probing_hst import LinearProbingHashST
from itu.algs4.searching.red_black_bst import RedBlackBST
from itu.algs4.searching.seperate_chaining_hst import SeparateChainingHashST
from itu.algs4.searching.sequential_search_st import SequentialSearchST
from itu.algs4.searching.st import ST

ST_IMPLEMENTATIONS = [
    BinarySearchST,
    BST,
    LinearProbingHashST,
    RedBlackBST,
    SeparateChainingHashST,
    SequentialSearchST,
    ST,
]


@pytest.mark.parametrize(
    "st", [constructor() for constructor in ST_IMPLEMENTATIONS],
)
def test_is_empty(st):
    assert st.is_empty()


@pytest.mark.parametrize(
    "st", [constructor() for constructor in ST_IMPLEMENTATIONS],
)
def test_delete(st):
    st.put("key1", "val1")
    st.put("key2", "val2")
    st.put("key3", "val3")
    st.delete("key3")
    st.delete("key2")
    st.delete("key1")
    assert st.is_empty()


@pytest.mark.parametrize(
    "st", [constructor() for constructor in ST_IMPLEMENTATIONS],
)
def old_tests(st):
    st.put("one", 1)
    assert ["one"] == list(st.keys())
    assert st.get("one") == 1
    assert st.contains("one")
    st.delete("one")
    assert st.is_empty()
    st.put("aaa", 1)
    st.put("bbb", 2)
    st.put("ccc", 3)
    st.put("ddd", 4)
    st.put("eee", 5)
    if st.ceiling:
        assert st.ceiling("ccc") == "ccc"
        assert st.ceiling("dad") == "ddd"
        assert st.floor("ccc") == "ccc"
        assert st.floor("dad") == "ccc"
    for k in st:
        assert k in st.keys()
    assert st.min() == "aaa"
    assert st.max() == "eee"
