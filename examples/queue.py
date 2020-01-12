#!/usr/bin/env python3
from itu.algs4.fundamentals.queue import Queue
from itu.algs4.stdlib import stdio

"""
Reads strings from an stdin and adds them to a queue.
When reading a '-' it removes the least recently added item and prints it.
Prints the amount of items left on the queue.
"""
queue = Queue()
while not stdio.isEmpty():
    input_item = stdio.readString()
    if input_item != "-":
        queue.enqueue(input_item)
    elif not queue.is_empty():
        print(queue.dequeue())
print("({} left on queue)".format(queue.size()))
