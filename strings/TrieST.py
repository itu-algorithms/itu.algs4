import sys, os
def setpath():
    exe = sys.argv[0]
    p = os.path.split(exe)[0]
    sys.path.insert(0, os.path.join(p, '..', 'fundamentals'))
    sys.path.insert(0, os.path.join(p, '..', 'stdlib'))
    sys.path.insert(0, p)
    sys.path.insert(0, exe)
setpath()
from queue import Queue
import stdio
try:
    q = Queue()
    q.enqueue(1)
except AttributeError:
    print('ERROR - Could not import algs4 queue')
    sys.exit(1)


"""
 *  The TrieST class represents an symbol table of key-value
 *  pairs, with string keys and generic values.
 *  It supports the usual <em>put</em>, <em>get</em>, <em>contains</em>,
 *  <em>delete</em>, <em>size</em>, and <em>is-empty</em> methods.
 *  It also provides character-based methods for finding the string
 *  in the symbol table that is the <em>longest prefix</em> of a given prefix,
 *  finding all strings in the symbol table that <em>start with</em> a given prefix,
 *  and finding all strings in the symbol table that <em>match</em> a given pattern.
 *  A symbol table implements the <em>associative array</em> abstraction:
 *  when associating a value with a key that is already in the symbol table,
 *  the convention is to replace the old value with the new value.
 *  Unlike {@link java.util.Map}, this class uses the convention that
 *  values cannot be {@code null}â€”setting the
 *  value associated with a key to {@code null} is equivalent to deleting the key
 *  from the symbol table.
 *  <p>
 *  This implementation uses a 256-way trie.
 *  The <em>put</em>, <em>contains</em>, <em>delete</em>, and
 *  <em>longest prefix</em> operations take time proportional to the length
 *  of the key (in the worst case). Construction takes constant time.
 *  The <em>size</em>, and <em>is-empty</em> operations take constant time.
 *  Construction takes constant time.
 *  <p>
 *  For additional documentation, see <a href="http://algs4.cs.princeton.edu/52trie">Section 5.2</a> of
 *  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.
 */
 """

class TrieST(object):
    R = 256     # extended ASCII

    # R-way trie node
    class Node(object):
        def __init__(self):
            self._val = None
            self._next = [None] * R  # array of nodes of length R TODO java: new Node[R]
            # TODO if I instantiate R nodes here we get infinite recursion

    def __init__(self):
        self._root = self.Node()     # root of trie
        self._n;                # number of keys in trie


    # * Returns the value associated with the given key.
    # * @param key the key
    # * @return the value associated with the given key if the key is in the symbol table
    # *     and {@code null} if the key is not in the symbol table
    # * @throws NullPointerException if {@code key} is {@code null}
    
    def get(self, key):
        x = self._get(self._root, key, 0)
        return None if x is None else x.val

    # * Does this symbol table contain the given key?
    # * @param key the key
    # * @return {@code true} if this symbol table contains {@code key} and
    # *     {@code false} otherwise
    # * @throws NullPointerException if {@code key} is {@code null}
     
    def contains(self, key):
        return self.get(key) is not None
    
    def _get(self, x, key, d):
        if x is None:
            return None
        if d == len(key):
            return x
        c = key[d]
        return self._get(x.next[c], key, d+1)
        # TODO is char c being used as an index (int)? need to change 
        # TODO alternatives: convert single ASCII character into int for array index, or use dictionary char to node

    # * Inserts the key-value pair into the symbol table, overwriting the old value
    # * with the new value if the key is already in the symbol table.
    # * If the value is {@code null}, this effectively deletes the key from the symbol table.
    # * @param key the key
    # * @param val the value
    # * @throws NullPointerException if {@code key} is {@code null}
    
    def put(self, key, val):
        if val is None:
            self.delete(key)
        else:
            self._root = self._put(self._root, key, val, 0)

    def _put(self, x, key, val, d):
        if x is None:
            x = self.Node()
        if d == len(key):
            if x.val is None;
                self._n +=1
            x.val = val
            return x
        c = key[d]
        x.next[c] = self._put(x.next[c], key, val, d+1)
        return x
    # TODO same thing as before, c used as index for next
    
    # * Returns the number of key-value pairs in this symbol table.
    # * @return the number of key-value pairs in this symbol table
    def size(self):
        return self._n

    # * Is this symbol table empty?
    # * @return {@code true} if this symbol table is empty and {@code false} otherwise
     def is_empty(self):
         return self.size() == 0
    
    
    # * Returns all keys in the symbol table as an {@code Iterable}.
    # * To iterate over all of the keys in the symbol table named {@code st},
    # * use the foreach notation: {@code for (Key key : st.keys())}.
    # * @return all keys in the symbol table as an {@code Iterable}
    
    # TODO how to translate iterable/? is list ok?
    def keys(self):
        return self.keys_with_prefix('')

    #public Iterable<String> keys() {
    #    return keysWithPrefix("");
    #}

    # * Returns all of the keys in the set that start with {@code prefix}.
    # * @param prefix the prefix
    # * @return all of the keys in the set that start with {@code prefix},
    # *     as an iterable
    
    def keys_with_prefix(self, prefix):
        results = Queue()
        x = self._get(self._root, prefix, 0)
        self._collect(x, prefix, results)
        return results

    #public Iterable<String> keysWithPrefix(String prefix) {
    #    Queue<String> results = new Queue<String>();
    #    Node x = get(root, prefix, 0);
    #    collect(x, new StringBuilder(prefix), results);
    #    return results;
    #}
    
    def _collect(self, x, prefix, results):
        if x is None:
            return
        if x.val is not None:
            results.enqueue(prefix) # TODO assuming enqueue method
        # TODO c is int and also char for java
        for c in xrange(0, R):
            prefix = prefix + c # TODO this only works for c as char (string)
            self._collect(x.next[c], prefix, results)
            prefix = prefix[:-1]

    #private void collect(Node x, StringBuilder prefix, Queue<String> results) {
    #    if (x == null) return;
    #    if (x.val != null) results.enqueue(prefix.toString());
    #    for (char c = 0; c < R; c++) {
    #        prefix.append(c);
    #        collect(x.next[c], prefix, results);
    #        prefix.deleteCharAt(prefix.length() - 1);
    #    }
    #}

    # * Returns all of the keys in the symbol table that match {@code pattern},
    # * where . symbol is treated as a wildcard character.
    # * @param pattern the pattern
    # * @return all of the keys in the symbol table that match {@code pattern},
    # *     as an iterable, where . is treated as a wildcard character.
    
    def keys_that_match(self, pattern):
        results = Queue()
        self._collect_match(x, prefix, pattern, results) 
        return results

    #public Iterable<String> keysThatMatch(String pattern) {
    #    Queue<String> results = new Queue<String>();
    #    collect(root, new StringBuilder(), pattern, results);
    #    return results;
    #}
    
    def _collect_match(self, x, prefix, pattern, results):
        if x is None:
            return None
        d = len(prefix)
        if d == len(pattern) and x.val is not None:
            results.enqueue(prefix) # TODO assuming enqueue method
        elif d == len(pattern):
            return
        c = pattern[d]
        if c == '.':
            for c in xrange(0, R): # TODO c is int, in java also char, also, R might not be in scope
                prefix = prefix + c # TODO only works with string
                self._collect_match(x.next[c], prefix, pattern, results) # TODO c is int or char used for index
                prefix = prefix[:-1]
        else:
            prefix = prefix + c # TODO only works with string
            self._collect_match(x.next[c], prefix, pattern, results)
            prefix = prefix[:-1]

    #private void collect(Node x, StringBuilder prefix, String pattern, Queue<String> results) {
    #    if (x == null) return;
    #    int d = prefix.length();
    #    if (d == pattern.length() && x.val != null)
    #        results.enqueue(prefix.toString());
    #    if (d == pattern.length())
    #        return;
    #    char c = pattern.charAt(d);
    #    if (c == '.') {
    #        for (char ch = 0; ch < R; ch++) {
    #            prefix.append(ch);
    #            collect(x.next[ch], prefix, pattern, results);
    #            prefix.deleteCharAt(prefix.length() - 1);
    #        }
    #    }
    #    else {
    #        prefix.append(c);
    #        collect(x.next[c], prefix, pattern, results);
    #        prefix.deleteCharAt(prefix.length() - 1);
    #    }
    #}

    
    # * Returns the string in the symbol table that is the longest prefix of {@code query},
    # * or {@code null}, if no such string.
    # * @param query the query string
    # * @return the string in the symbol table that is the longest prefix of {@code query},
    # *  or {@code null} if no such string
    # * @throws NullPointerException if {@code query} is {@code null}
    
    def longest_prefix_of(self, query):
        length = self._logest_prefix_of(self._root, query, 0, -1)
        if length == -1:
            return None
        else:
            return query[:length]

    #public String longestPrefixOf(String query) {
    #    int length = longestPrefixOf(root, query, 0, -1);
    #    if (length == -1) return null;
    #    else return query.substring(0, length);
    #}

    #// returns the length of the longest string key in the subtrie
    #// rooted at x that is a prefix of the query string,
    #// assuming the first d character match and we have already
    #// found a prefix match of given length (-1 if no such match)
    def _longest_prefix_of(self, x, query, d, length):
        if x is None:
            return length
        if x.val is not None:
            length = d
        if d == len(query):
            return length
        c = query[d] # TODO char or int?
        return self._longest_prefix_of(x.next[c], query, d+1, length) # TODO c is index

    #private int longestPrefixOf(Node x, String query, int d, int length) {
    #    if (x == null) return length;
    #    if (x.val != null) length = d;
    #    if (d == query.length()) return length;
    #    char c = query.charAt(d);
    #    return longestPrefixOf(x.next[c], query, d+1, length);
    #}

    
    # * Removes the key from the set if the key is present.
    # * @param key the key
    # * @throws NullPointerException if {@code key} is {@code null}
    
    def delete(self, key):
        self._root = self._delete(self._root, key, 0)

    #public void delete(String key) {
    #    root = delete(root, key, 0);
    #}
    
    def _delete(self, x, key, d):
        if x is None:
            return None
        if d == len(key):
            if x.val is not None:
                self._n += -1
            x.val = None
        else:
            c = key[d]
            x.next[c] = self._delete(x,next[c], key, d+1) # TODO c is index and also char
        
        # remove subtrie rooted at x if it is completely empty
        if x.val is not None:
            return x
        for c in xrange(0,R): # TODO now c is integer
            if x.next[c] is not None:
                return x
        return None

    #private Node delete(Node x, String key, int d) {
    #    if (x == null) return null;
    #    if (d == key.length()) {
    #        if (x.val != null) n--;
    #        x.val = null;
    #    }
    #    else {
    #        char c = key.charAt(d);
    #        x.next[c] = delete(x.next[c], key, d+1);
    #    }
    #    // remove subtrie rooted at x if it is completely empty
    #    if (x.val != null) return x;
    #    for (int c = 0; c < R; c++)
    #        if (x.next[c] != null)
    #            return x;
    #    return null;
    #}

if __name__ == '__main__':
    st = TrieST()
    i = 0
    while not stdio.isEmpty(): # TODO import stdin, also assumuing is_empty method
        key = stdio.readString()
        st.put(key, i)
        i += 1
    # print results
    if st.size() < 100:
        print('keys(""):')
        for key in st.keys():
            print('{} {}'.format(key, st.get(key)))
        print()
    print('longest_prefix_of("shellsort"):')
    print(st.logest_prefix_of('shellsort'))
    print()
    print('longest_prefix_of("quicksort")')
    print(st.longest_prefix_of('quicksort'))
    print()
    print('keys_with_prefix("shor")')
    for s in st.keys_with_prefix('shor'):
        print(s)
    print()
    print('keys_that_match("he.l.")')
    for s in st.keys_that_match('he.l.'):
        print(s)

