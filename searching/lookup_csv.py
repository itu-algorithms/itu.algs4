# Created for BADS 2018
# See README.md for details
# Python 3
import sys, os
def setpath():
    exe = sys.argv[0]
    p = os.path.split(exe)[0]
    sys.path.insert(0, os.path.join(p, '..', 'stdlib'))
    sys.path.insert(0, p)
setpath()
import stdio

#  Execution:    python lookup_csv.py file.csv keyField valField
#  
#  Reads in a set of key-value pairs from a two-column CSV file
#  specified on the command line; then, reads in keys from standard
#  input and prints out corresponding values.
# 
#  % python lookup_csv.py amino.csv 0 3     % python lookup_csv.py ip.csv 0 1 
#  TTA                                  www.google.com 
#  Leucine                              216.239.41.99 
#  ABC                               
#  Not found                            % python lookup_csv.py ip.csv 1 0 
#  TCT                                  216.239.41.99 
#  Serine                               www.google.com 
#                                 
#  % python lookup_csv.py amino.csv 3 0     % python lookup_csv.py DJIA.csv 0 1 
#  Glycine                              29-Oct-29 
#  GGG                                  252.38 
#                                       20-Oct-87 
#                                       1738.74

"""
The LookupCSV class provides a data-driven client for reading in a
key-value pairs from a file; then, printing the values corresponding to the
keys found on standard input. Both keys and values are strings.
The fields to serve as the key and value are taken as command-line arguments.
"""

args = sys.argv[1:]
keyField = int(args[1])
valField = int(args[2])

# symbol table
st = {}
        #TODO use ST?  ST<String, String> st = new ST<String, String>();

# read in the data from csv file
file = open(args[0], 'r')
line = file.readline()
while line:
    tokens = line.split(",")
    key = tokens[keyField]
    val = tokens[valField]
    st[key] = val        # st.put(key, val) TODO in case ST
    line = file.readline()

while not stdio.isEmpty():
    s = stdio.readString()
    if s in st:   # st.contains(s)  TODO in case ST 
        print(st.get(s))
    else: 
        print("Not found") 
file.close()
