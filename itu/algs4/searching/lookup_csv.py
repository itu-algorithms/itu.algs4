# Created for BADS 2018
# See README.md for details
# Python 3
import sys

from itu.algs4.stdlib import stdio

# data files:
# https://algs4.cs.princeton.edu/35applications/amino.csv
#  Data files:   https://algs4.cs.princeton.edu/35applications/DJIA.csv
#                https://algs4.cs.princeton.edu/35applications/UPC.csv
#                https://algs4.cs.princeton.edu/35applications/amino.csv
#                https://algs4.cs.princeton.edu/35applications/elements.csv
#                https://algs4.cs.princeton.edu/35applications/ip.csv
#                https://algs4.cs.princeton.edu/35applications/morse.csv
 

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

if __name__ == '__main__':
  args = sys.argv[1:]
  keyField = int(args[1])
  valField = int(args[2])

  # symbol table
  st = {}

  # read in the data from csv file
  file = open(args[0], 'r')
  line = file.readline()
  while line:
      tokens = line.split(",")
      key = tokens[keyField]
      val = tokens[valField]
      st[key] = val        
      line = file.readline()

  while not stdio.isEmpty():
      s = stdio.readString()
      if s in st:   
          print(st.get(s))
      else: 
          print("Not found") 
  file.close()
