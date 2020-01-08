import sys

from algs4.searching.bst import BST
from algs4.stdlib import stdio

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            sys.stdin = open(sys.argv[1])
        except IOError:
            print("File not found, using standard input instead")

    data = stdio.readAllStrings()
    st: BST[str, int] = BST()
    i = 0
    for key in data:
        st.put(key, i)
        i += 1

    print("LEVELORDER:")
    for key in st.level_order():
        print(str(key) + " " + str(st.get(key)))

    print()

    print("KEYS:")
    for key in st.keys():
        print(str(key) + " " + str(st.get(key)))
