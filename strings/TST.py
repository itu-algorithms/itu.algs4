
import sys, os
def setpath():
    exe = sys.argv[0]
    p = os.path.split(exe)[0]
    sys.path.insert(0, os.path.join(p, '..', 'fundamentals'))
    sys.path.insert(0, p)
    sys.path.insert(0, exe)
setpath()

from queue import Queue
try:
    q = Queue()
    q.enqueue(1)
except AttributeError:
    print('WARNING - unable to import python algs4 Queue class')
    sys.exit(1)

 # *  Symbol table with string keys, implemented using a ternary search
 # *  trie (TST).
 

# *  The {@code TST} class represents an symbol table of key-value
# *  pairs, with string keys and generic values.
# *  It supports the usual <em>put</em>, <em>get</em>, <em>contains</em>,
# *  <em>delete</em>, <em>size</em>, and <em>is-empty</em> methods.
# *  It also provides character-based methods for finding the string
# *  in the symbol table that is the <em>longest prefix</em> of a given prefix,
# *  finding all strings in the symbol table that <em>start with</em> a given prefix,
# *  and finding all strings in the symbol table that <em>match</em> a given pattern.
# *  A symbol table implements the <em>associative array</em> abstraction:
# *  when associating a value with a key that is already in the symbol table,
# *  the convention is to replace the old value with the new value.
# *  Unlike {@link java.util.Map}, this class uses the convention that
# *  values cannot be {@code null}â€”setting the
# *  value associated with a key to {@code null} is equivalent to deleting the key
# *  from the symbol table.
# *  <p>
# *  This implementation uses a ternary search trie.
# *  <p>
# *  For additional documentation, see <a href="http://algs4.cs.princeton.edu/52trie">Section 5.2</a> of
# *  <i>Algorithms, 4th Edition</i> by Robert Sedgewick and Kevin Wayne.

class TST(object):
    class Node():
        def __init__(self):
            self.c = None       # character
            self.left = None    # left, middle and right subtries
            self.mid = None
            self.right = None
            self.val = None     # value associated with string

    def __init__(self):
        self.n = 0         # size
        self.root = None   # root of TST

    
    # * Returns the number of key-value pairs in this symbol table.
    # * @return the number of key-value pairs in this symbol table
    def size(self):
        return self.n

    # * Does this symbol table contain the given key?
    # * @param key the key
    # * @return {@code true} if this symbol table contains {@code key} and
    # *     {@code false} otherwise
    # * @throws IllegalArgumentException if {@code key} is {@code null}
    def contains(self, key):
        if key is None:
            raise Exception("argument of contains is None") # TODO maybe get a specific exception, lilke IllegalArgumentException in Java
        return self.get(key) is not None

    # * Returns the value associated with the given key.
    # * @param key the key
    # * @return the value associated with the given key if the key is in the symbol table
    # *     and {@code null} if the key is not in the symbol table
    # * @throws IllegalArgumentException if {@code key} is {@code null}
    def get(self, key):
        if key is None:
            raise Exception("calls get() with null argument" ) # TODO IllegalArgumentException?
        if len(key) == 0:
            raise Exception("key must have length >=1") # TODO IllegalArgumentException?
        x = self._get(self.root, key, 0)
        if x is None:
            return None
        return x.val

    # return subtrie corresponding to given key
    def _get(self, x, key, d):
        if x is None:
            return None
        if len(key) == 0:
            raise Exception("key nust have length >= 1")
        c = key[d] # TODO check for indexError? (d exceeding?) or is it covered in the cases?
        if c < x.c: # TODO check ordening of chars (strings)
            return self._get(x.left, key, d)
        elif x > x.c:
            return self._get(x.right, key, d)
        elif d < len(key) -1:
            return self._get(x.mid, key, d+1)
        else:
            return x

    #private Node<Value> get(Node<Value> x, String key, int d) {
    #    if (x == null) return null;
    #    if (key.length() == 0) throw new IllegalArgumentException("key must have length >= 1");
    #    char c = key.charAt(d);
    #    if      (c < x.c)              return get(x.left,  key, d);
    #    else if (c > x.c)              return get(x.right, key, d);
    #    else if (d < key.length() - 1) return get(x.mid,   key, d+1);
    #    else                           return x;
    #}

    # * Inserts the key-value pair into the symbol table, overwriting the old value
    # * with the new value if the key is already in the symbol table.
    # * If the value is {@code null}, this effectively deletes the key from the symbol table.
    # * @param key the key
    # * @param val the value
    # * @throws IllegalArgumentException if {@code key} is {@code null}
    
    def put(self, key, val):
        if key is None:
            raise Exception("calls put() with null key") # TODO IllegalArgumentException 
        if not self.contains(key):
            self.n += 1
        self.root = self._put(self.root, key, val)

   # public void put(String key, Value val) {
   #     if (key == null) {
   #         throw new IllegalArgumentException("calls put() with null key");
   #     }
   #     if (!contains(key)) n++;
   #     root = put(root, key, val, 0);
   # }
    def _put(self, x, key, val, d):
        c = key[d] # TODO check IndexError
        if x is None:
            x = Node() # TODO check scopoe for class node
            x.c = c
        if c < x.c:
            x.left = self._put(x.left, key, val, d)
        elif c > x.c:
            x.right = self._put(x.right, key, val, d)
        elif d < len(key) -1:
            x.mid = self._put(x.mid, key, val, d+1)
        else:
            x.val = val

        return x

    #private Node<Value> put(Node<Value> x, String key, Value val, int d) {
    #    char c = key.charAt(d);
    #    if (x == null) {
    #        x = new Node<Value>();
    #        x.c = c;
    #    }
    #    if      (c < x.c)               x.left  = put(x.left,  key, val, d);
    #    else if (c > x.c)               x.right = put(x.right, key, val, d);
    #    else if (d < key.length() - 1)  x.mid   = put(x.mid,   key, val, d+1);
    #    else                            x.val   = val;
    #    return x;
    #}

    # * Returns the string in the symbol table that is the longest prefix of {@code query},
    # * or {@code null}, if no such string.
    # * @param query the query string
    # * @return the string in the symbol table that is the longest prefix of {@code query},
    # *     or {@code null} if no such string
    # * @throws IllegalArgumentException if {@code query} is {@code null}
    
    def longest_prefix_of(self, query):
        if query is None:
            raise Exception("calls longest_path_of() with None argument")
        if len(query) == 0:
            return None
        length = 0
        x = self.root
        i = 0
        while (x is not None and i < len(query)):
            c = query[i]
            if c < x.c:
                x = x.left
            elif c > x.c:
                x = x.right
            else:
                i += 1
                if x.val is not None:
                    length = i
                x = x.mid
        return query[0:length]  # TODO control that is not length + 1, what does java's substring do?

    #public String longestPrefixOf(String query) {
    #    if (query == null) {
    #        throw new IllegalArgumentException("calls longestPrefixOf() with null argument");
    #    }
    #    if (query.length() == 0) return null;
    #    int length = 0;
    #    Node<Value> x = root;
    #    int i = 0;
    #    while (x != null && i < query.length()) {
    #        char c = query.charAt(i);
    #        if      (c < x.c) x = x.left;
    #        else if (c > x.c) x = x.right;
    #        else {
    #            i++;
    #            if (x.val != null) length = i;
    #            x = x.mid;
    #        }
    #    }
    #    return query.substring(0, length);
    #}

    
    # * Returns all keys in the symbol table as an {@code Iterable}.
    # * To iterate over all of the keys in the symbol table named {@code st},
    # * use the foreach notation: {@code for (Key key : st.keys())}.
    # * @return all keys in the symbol table as an {@code Iterable}
    
    def keys(self):
        queue = Queue()
        self._collect(self.root, "", queue)
        return queue
    #public Iterable<String> keys() {
    #    Queue<String> queue = new Queue<String>();
    #    collect(root, new StringBuilder(), queue);
    #    return queue;
    #}

    
    # * Returns all of the keys in the set that start with {@code prefix}.
    # * @param prefix the prefix
    # * @return all of the keys in the set that start with {@code prefix},
    # *     as an iterable
    # * @throws IllegalArgumentException if {@code prefix} is {@code null}
    
    def keys_with_prefix(self, prefix):
        if prefix is None:
            raise Exception("calls keys_with_prefix with null argument") # TODO IllegalArgumentException
        queue = Queue()
        x = self._get(self.root, prefix, 0)
        if x is None:
            return queue
        if x.val is not None:
            queue.enqueue(prefix)
        self._collect(x.mid, prefix, queue)
        return queue
    #public Iterable<String> keysWithPrefix(String prefix) {
    #    if (prefix == null) {
    #        throw new IllegalArgumentException("calls keysWithPrefix() with null argument");
    #    }
    #    Queue<String> queue = new Queue<String>();
    #    Node<Value> x = get(root, prefix, 0);
    #    if (x == null) return queue;
    #    if (x.val != null) queue.enqueue(prefix);
    #    collect(x.mid, new StringBuilder(prefix), queue);
    #    return queue;
    #}

    #// all keys in subtrie rooted at x with given prefix
    def _collect(self, x, prefix, queue):
        if x is None:
            return
        self._collect(x.left, prefix, queue)
        if x.val is not None:
            queue.enqueue(prefix + str(x.c))
        self._collect(x.mid, prefix + str(x.c), queue)
        #prefix = prefix[:-1] #TODO is this necessary? was this for append of before, or a step of the search?
        self._collect(x.right, prefix, queue)
    
    #private void collect(Node<Value> x, StringBuilder prefix, Queue<String> queue) {
    #    if (x == null) return;
    #    collect(x.left,  prefix, queue);
    #    if (x.val != null) queue.enqueue(prefix.toString() + x.c);
    #    collect(x.mid,   prefix.append(x.c), queue);
    #    prefix.deleteCharAt(prefix.length() - 1);
    #    collect(x.right, prefix, queue);
    #}


    # * Returns all of the keys in the symbol table that match {@code pattern},
    # * where . symbol is treated as a wildcard character.
    # * @param pattern the pattern
    # * @return all of the keys in the symbol table that match {@code pattern},
    # *     as an iterable, where . is treated as a wildcard character.
    
    def keys_that_match(self, pattern):
        queue = Queue()
        self._collect_match(self.root, "", 0, pattern, queue)
        return queue
    #public Iterable<String> keysThatMatch(String pattern) {
    #    Queue<String> queue = new Queue<String>();
    #    collect(root, new StringBuilder(), 0, pattern, queue);
    #    return queue;
    #}
    
    def _collect_match(self, x, prefix, i, pattern, queue):
        if x is None:
            return
        c = pattern[i] # TODO IndexError
        if c == '.' or c <x.c:
            self._collect_match(x.left, prefix, i, pattern, queue)
        if c == '.' or c == x.c:
            if i == len(pattern) -1 and x.val is not None:
                queue.enqueue(prefix + str(x.c)) # TODO can x.c be something other than a character?
            if i < len(pattern) -1:
                self._collect_match(x.mid, prefix + x.c, i+1, pattern, queue)
                prefix = prefix[:-1] # TODO is this necessary or only because of append?
        if c == '.' or c > x.c:
            self._collect_match(x.right, prefix, i, pattern, queue)

    #private void collect(Node<Value> x, StringBuilder prefix, int i, String pattern, Queue<String> queue) {
    #    if (x == null) return;
    #    char c = pattern.charAt(i);
    #    if (c == '.' || c < x.c) collect(x.left, prefix, i, pattern, queue);
    #    if (c == '.' || c == x.c) {
    #        if (i == pattern.length() - 1 && x.val != null) queue.enqueue(prefix.toString() + x.c);
    #        if (i < pattern.length() - 1) {
    #            collect(x.mid, prefix.append(x.c), i+1, pattern, queue);
    #            prefix.deleteCharAt(prefix.length() - 1);
    #        }
    #    }
    #    if (c == '.' || c > x.c) collect(x.right, prefix, i, pattern, queue);
    #}


# * Unit tests the {@code TST} data type.
# * @param args the command-line arguments
if __name__ == '__main__':
    st = TST()
    i = 0
    # build symbol table from stdin
    while not stdio.isEmpty():
        key = stdio.readString()
        st.put(key, i)
        i += 1
    # print results
    if st.size() < 100:
        print('keys(""):')
        for key in st.keys():
            print("{} {}".format(key, st.get(key)))
        print()
            
        print("longestPrefixOf(\"shellsort\"):")
        print(st.longest_prefix_of("shellsort"))
        print()

        print("longestPrefixOf(\"shell\"):")
        print(st.longest_prefix_of("shell"))
        print()

        print("keysWithPrefix(\"shor\"):")
        for s in st.keys_with_prefix("shor"):
            print(s)
        print()

        print("keysThatMatch(\".he.l.\"):")
        for s in st.keys_that_match(".he.l."):
            print(s)
    

