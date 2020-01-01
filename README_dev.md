# AlgorithmsInPython
Translation of the Java code in "Algorithms" by Sedgwick and Wayne to python3

# Test

In the root directory, run

```
python3 -m unittest test/test_bst.py
```

# Types

The binary search tree now type checks using mypy, try

```
 mypy --strict -m algs4.searching.bst
```

# Examples

Client code should be migrated to ```examples/```. 


# Useful Resources
## the book
https://algs4.cs.princeton.edu/home/
## a python version of a similar book
https://introcs.cs.princeton.edu/python/home/
## all java code -- good list, includes what needs to be done
https://algs4.cs.princeton.edu/code/

https://github.com/kevin-wayne/algs4


# The People

Riko Jacob <rikj@itu.dk>,
Thore Husfeldt <thore@itu.dk>,

Morten Tychsen Clausen <mocl@itu.dk>, 
Frederik Haagensen <haag@itu.dk>, 
Anton Mølbjerg Eskildsen <aesk@itu.dk>, 
Andreas Holck Høeg-Petersen <anhh@itu.dk>, 
Martino Secchi <msec@itu.dk>, 
Otto Stadel Clausen <otcl@itu.dk>

# Who works on what

# Coding style 

https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions

## we have subdirectories for the code, one for each chapter
## if java relies on having different implementations depending on the type:
Use somehting like
```
class DirectedDFS:
	def __init__(self, G, *s):
```
like in `graphs/directed_dfs.py`

Otherwise we use static factory methods where the name indicates the expected type.
If appropriate we use `isinstance()` and its variants, for example to distinguish undirected and directed graphs. 
## things like 'node' are inside classes, no leading underscore
## file names, variables, methods are file_name (and not CamelCase, adjustting from algs4), only classes are CamelCase (PascalCase)
## there is one file per version of an algorithm / data structure (like in algs4), the name, and importantly the docstring, reflects which version it is
## java main becomes __main__ stuff; follow what is there; adjust the initial comment
## don't replicate imports unless 

## variable names: 
- lower case letter with underscore
- like in the book
- private variables become _variable_name

## if java has toString(), then we have __repr__()

## keep the comments from the java code 
## if in doubt, we go with the book, not the code on the book web site (keep it simple)
## docstring without formatting
# ideas
- should we include generators (additionally to iterators) everywhere?

