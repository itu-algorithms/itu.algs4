# Created for BADS 2018
# See README.md for details
# Python 3
import sys
from stdlib import stdio
from fundamentals.queue import Queue
try:
    q = Queue()
    q.enqueue(1)
except AttributeError:
    print('ERROR - Could not import algs4 queue')
    sys.exit(1)

# Execution:    python lookup_index.py movies.txt "/"
# Dependencies: queue.py stdio.py
# % python lookup_index.py aminoI.csv ","
# Serine
#   TCT
#   TCA
#   TCG
#   AGT
#   AGC
# TCG
#   Serine
#
# % python lookup_index.py movies.txt "/"
# Bacon, Kevin
#   Animal House (1978)
#   Apollo 13 (1995)
#   Beauty Shop (2005)
#   Diner (1982)
#   Few Good Men, A (1992)
#   Flatliners (1990)
#   Footloose (1984)
#   Friday the 13th (1980)
#   ...
# Tin Men (1987)
#   DeBoy, David
#   Blumenfeld, Alan
#   ...

# The LookupIndex class provides a data-driven client for reading in a
# key-value pairs from a file; then, printing the values corresponding to the
# keys found on standard input. Keys are strings; values are lists of strings.
# The separating delimiter is taken as a command-line argument. This client
# is sometimes known as an inverted index.

args = sys.argv[1:]
filename  = args[0]
separator = args[1]
file = open(filename, 'r')
st = {}
ts = {}
        # TODO use ST instead? 
        # ST<String, Queue<String>> st = new ST<String, Queue<String>>();
        # ST<String, Queue<String>> ts = new ST<String, Queue<String>>();

line = file.readline()
while line:
    fields = line.split(separator)
    key = fields[0]
    for i in range(1, len(fields)):
        val = fields[i]
        if not key in st:       #not st.contains(key):
            st[key] = Queue()
        if not val in ts:       #not ts.contains(val):
            ts[val] = Queue()
        st.get(key).enqueue(val)
        ts.get(val).enqueue(key)
    line = file.readline()
print("Done indexing")

#read queries from standard input, one per line
while not stdio.isEmpty():
    query = stdio.readLine()
    if query in st:
        for vals in st.get(query):
            print("  " + vals)
    if query in ts:
        for keys in ts.get(query):
            print("  " + keys)

file.close()
