#!/usr/bin/env python3
from itu.algs4.sorting import merge
from itu.algs4.stdlib import stdio

"""
Reads a list of integers from standard input.
Then prints it in sorted order.
"""
L = stdio.readAllInts()

merge.sort(L)

if len(L) > 0:
    stdio.write(L[0])
for i in range(1, len(L)):
    stdio.write(" ")
    stdio.write(L[i])
stdio.writeln()
