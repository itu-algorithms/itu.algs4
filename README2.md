# Algs4 for Python

Translation of the Java code in "Algorithms 4th edition" by Sedgwick and Wayne to python3.



## Installation instructions

In order for the package to work, you must have `python3` and `setup-tools`/`pip` already installed - see [python homepage](https://python.org) for instructions.

1. Download and unzip the repository.
2. Open a command prompt or terminal and navigate to the downloaded folder.
3. Use the command `pip install .` to install the package (this will also work for updating the package, when a newer version is available).

*Note:* If you're using `virtualenv` or `anaconda` make sure to activate/select the desired environment before installing.



## Usage

The package is divided into five sub-packages representing the first five chapters of "Algorithms 4th edition", as well as the `stdlib` package from [this book](https://introcs.cs.princeton.edu/python/code/) (with slight modification), and a package containing a number of exception classes. 

Use the `help` function on any package or sub-packages to get a list of its contents. For example `help(algs4)` yields the following:

```
Help on package algs4:

NAME
    algs4

PACKAGE CONTENTS
    errors (package)
    fundamentals (package)
    graphs (package)
    searching (package)
    sorting (package)
    stdlib (package)
    strings (package)

FILE
    (built-in)
```



### Importing

Besides the hierarchical structure, all class- and file-names from the book have been written in lower-case style with underscores instead of the Pascal case style of the Java version. For example `EdgeWeightedDigraph.java` has been renamed to `edge_weighted_digraph.py`. Class names still use Pascal case though (following Python convention).

**Example**

```python
# Importing the Digraph class 
from algs4.graphs.edge_weighted_digraph import EdgeWeightedDigraph

# Some files contain multiple classes, for example:
from algs4.fundamentals.uf import UF
from algs4.fundamentals.uf import QuickUnionUF
```



### Documentation

You can use the built-in `help` function on any public class or function to get a description of what it does. This documentation should also work with your IDE of choice.