# Algs4 for Python

The textbook [Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/) by Sedgewick and Wayne describes all algorithms as Java programs. They provide the [source code](https://algs4.cs.princeton.edu/code/) online as a jar library [algs4.jar](https://algs4.cs.princeton.edu/code/algs4.jar).
This repository contains the Python3 translation of that Java code.
In addition, it contains, with slight modifications, the `stdlib` package from the book [Introduction to Programming in Python](https://introcs.cs.princeton.edu/python/code/) by Sedgewick, Wayne, and Dondero.

## Installation

This library requires a functioning Python3 environment, for example the one provided by [Anaconda](https://www.anaconda.com/distribution/).
Some optional visual and auditory features depend on the [numpy](http://numpy.org) and [pygame](https://pygame.org) packages.

### With pip and git

If git is available, the following command will install the library in your python environment:

```bash
pip install git+https://github.itu.dk/algorithms/AlgorithmsInPython
```

When requested, you will need to enter your ITU credentials.

### With pip and zip

To install this library without git:

1. Download and unzip the repository.
2. Open a command prompt or terminal and navigate to the downloaded folder. There should be the file `setup.py`.
3. Use the command `pip3 install .` to install the package (this will also work for updating the package, when a newer version is available).  If your python installation is system-wide, use `sudo pip3 install .`

### Step-by-step guide for Windows

To install the `algs4` package:

- Download the repository by pressing the green "Clone or download" button, and pressing "Download ZIP".
- Extract the content of the zip to your Desktop (you can delete the folder after installing the package).
- Open the "Command Prompt" by pressing "Windows + R", type "cmd" in the window that appears, and press "OK".
- If you saved the folder on the Desktop you should be able to navigate to the folder by typing "cd Desktop\AlgorithmsInPython-master".
```
C:\Users\haag>cd Desktop\AlgorithmsInPython-master
```
- When in the correct folder simply type "pip install ." to install the package. 
```
C:\Users\haag\Desktop\AlgorithmsInPython-master>pip install .
```
- After this, the package should be installed correctly and you can delete the folder from your Desktop.

## Test the installation
To test that the package is installed correctly, run python in interactive mode and enter `from algs4.fundamentals.uf import UF`.
```
C:\Users\haag>python
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from algs4.fundamentals.uf import UF
>>> 
```
If no error message occured, the library has been installed correctly.

## Usage

The package `algs4` has a hierarchical structure. It has seven sub-packages, corresponding to: the first five chapters of "Algorithms, 4th Edition", the `stdlib` package of "Introduction to Programming in Python", and a package `error` containing a number of exception classes.

All filenames and package names have been written in lower-case style with underscores instead of the CamelCase style of the Java version. For example `EdgeWeightedDigraph.java` has been renamed to `edge_weighted_digraph.py`. Class names still use CamelCase though, which is consistent with naming conventions in Python.

### Example

```python
# Import the digraph class 
from algs4.graphs.edge_weighted_digraph import EdgeWeightedDigraph

# Some files contain multiple classes, for example:
from algs4.fundamentals.uf import UF
from algs4.fundamentals.uf import QuickUnionUF
```

## Documentation

You can use python's built-in `help` function on any package, sub-package, public class, or function to get a description of what it contains or does. This documentation should also show up in your IDE of choice.
For example `help(algs4)` yields the following:

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
