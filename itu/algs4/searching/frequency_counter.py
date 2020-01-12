# Created for BADS 2018
# See README.md for details
# Python 3
import sys

from itu.algs4.stdlib import stdio

#  Execution:    python frequency_counter.py L < input.txt
#
#  Read in a list of words from standard input and print out
#  the most frequently occurring word that has length greater than
#  a given threshold.
#
#  % python frequency_counter.py 1 < tinyTale.txt
#  it 10
#
#  % python frequency_counter.py 8 < tale.txt
#  business 122
#
#  % python frequency_counter.py 10 < leipzig1M.txt
#  government 24763


""" 
  The FrequencyCounter class provides a client for 
  reading in a sequence of words and printing a word (exceeding
  a given length) that occurs most frequently. It is useful as
  a test client for various symbol table implementations.

  Reads in a command-line integer and sequence of words from
  standard input and prints out a word (whose length exceeds
  the threshold) that occurs most frequently to standard output.
  It also prints out the number of words whose length exceeds
  the threshold and the number of distinct such words.
"""

if __name__ == '__main__':
    args = sys.argv[1:]
    distinct = 0
    words = 0
    minlen = int(args[0])
    st = {}

    #compute frequency counts
    while not stdio.isEmpty():
        key = stdio.readString()
        if len(key) < minlen: 
            continue
        words+=1
        if key in st:                   
           st[key] = st.get(key) + 1    
        else:
            st[key] = 1                 
            distinct+=1

    # find a key with the highest frequency count
    max = ""
    st[max] = 0                         
    for word in st.keys():
        if st.get(word) > st.get(max):
            max = word


    print(max + " " + str(st.get(max)))
    print("distinct = " + str(distinct))
    print("words    = " + str(words))
