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

#  Execution:    python FrequencyCounter L < input.txt
#
#  Read in a list of words from standard input and print out
#  the most frequently occurring word that has length greater than
#  a given threshold.
#
#  % python FrequencyCounter 1 < tinyTale.txt
#  it 10
#
#  % python FrequencyCounter 8 < tale.txt
#  business 122
#
#  % python FrequencyCounter 10 < leipzig1M.txt
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
args = sys.argv[1:]
distinct = 0
words = 0
minlen = int(args[0])
st = {}
    # TODO use ST instead? ST<String, Integer> st = new ST<String, Integer>();

#compute frequency counts
while not stdio.isEmpty():
    key = stdio.readString()
    if len(key) < minlen: 
        continue
    words+=1
    if key in st:                   #TODO in case ST st.contains(key)
       st[key] = st.get(key) + 1    #st.put(key, st.get(key) + 1)
    else:
        st[key] = 1                 #st.put(key, 1)
        distinct+=1

# find a key with the highest frequency count
max = ""
st[max] = 0                         #st.put(max, 0)
for word in st.keys():
    if st.get(word) > st.get(max):
        max = word


print(max + " " + str(st.get(max)))
print("distinct = " + str(distinct))
print("words    = " + str(words))
