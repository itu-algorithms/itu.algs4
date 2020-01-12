#!/usr/bin/env python3
import sys

from itu.algs4.fundamentals.stack import Stack
from itu.algs4.stdlib import stdio

if len(sys.argv) > 1:
    try:
        sys.stdin = open(sys.argv[1])
    except IOError:
        print("File not found, using standard input instead")

stack: Stack[str] = Stack()
while not stdio.isEmpty():
    item = stdio.readString()
    if not item == "-":
        stack.push(item)
    elif not stack.is_empty():
        stdio.write(stack.pop() + " ")

stdio.writef("(%i left on stack)\n", stack.size())
