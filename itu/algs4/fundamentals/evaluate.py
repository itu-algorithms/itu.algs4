# Created for BADS 2018
# See README.md for details
# Python 3

import math
import sys

from itu.algs4.fundamentals.stack import Stack
from itu.algs4.stdlib import stdio


def evaluate():
    ops = Stack()
    vals = Stack()

    while not stdio.isEmpty():
        # Read token, push if operator
        s = stdio.readString()
        if   s == "(": pass
        elif s == "+":      ops.push(s)
        elif s == "-":      ops.push(s)
        elif s == "*":      ops.push(s)
        elif s == "/":      ops.push(s)
        elif s == "sqrt":   ops.push(s)
        elif s == ")":
            # Pop, evaluate and push result if token is ")"
            op = ops.pop()
            v = vals.pop()
            if   op == "+":     v = vals.pop() + v
            elif op == "-":     v = vals.pop() - v
            elif op == "*":     v = vals.pop() * v
            elif op == "/":     v = vals.pop() / v
            elif op == "sqrt":  v = math.sqrt(v)
            vals.push(v)
        else:   
            vals.push(float(s))
    stdio.writeln(vals.pop())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            sys.stdin = open(sys.argv[1])
        except IOError:
            print("File not found, using standard input instead")
            
    evaluate()
