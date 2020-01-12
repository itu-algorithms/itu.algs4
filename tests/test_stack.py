import random

import pytest

from itu.algs4.fundamentals.stack import FixedCapacityStack, ResizingArrayStack, Stack


@pytest.mark.parametrize(
    "stack",
    [
        FixedCapacityStack(0),
        FixedCapacityStack(1),
        FixedCapacityStack(7),
        ResizingArrayStack(),
        Stack(),
    ],
)
def test_is_empty(stack):
    assert stack.is_empty()


@pytest.mark.parametrize(
    "stack",
    [FixedCapacityStack(1), FixedCapacityStack(7), ResizingArrayStack(), Stack()],
)
def test_push_pop_once(stack):
    stack.push(83)
    assert not stack.is_empty()
    assert stack.pop() == 83
    assert stack.is_empty()


@pytest.mark.parametrize("capacity", list(range(10)))
def test_error_beyond_capacity(capacity):
    stack = FixedCapacityStack(capacity)
    for i in range(capacity):
        stack.push(i)
    try:
        stack.push(99)
        assert False
    except IndexError:
        pass


@pytest.mark.parametrize(
    "stack", [FixedCapacityStack(100), ResizingArrayStack(), Stack()]
)
@pytest.mark.parametrize("seed", [3928, 1928, 39211, 419901])
def test_random_pushpop_sequence(stack, seed):
    random.seed(seed)
    L = list(range(100))
    random.shuffle(L)
    for i in L:
        stack.push(i)
    L.reverse()
    for i in L:
        assert stack.pop() == i
    assert stack.is_empty()
