from .stack import Stack
from ..stdlib import stdio

import math

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