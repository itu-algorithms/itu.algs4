# `algs4-py`

`algs4-py` is a Python 3 port of the Java code in [Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/).

[![Build Status](https://github.itu.dk/algorithms/AlgorithmsInPython/workflows/check/badge.svg)](https://github.itu.dk/algorithms/AlgorithmsInPython/actions)

## Target audience

`algs4-py` is intended for instructors and students who wish to follow the textbook [Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/) by Sedgewick and Wayne.
It was first created in 2018 by teaching assistants and instructors at [ITU Copenhagen](https://algorithms.itu.dk), where the introductory course on Algorithms and Data Structures is taught bilingually in Java and Python 3.

## Installation

This library requires a functioning Python 3 environment, for example the one provided by [Anaconda](https://www.anaconda.com/distribution/).
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

To install the python package `algs4`:

- Download the repository by pressing the green "Clone or download" button, and pressing "Download ZIP".
- Extract the content of the zip to your Desktop (you can delete the folder after installing the package).
- Open the "Command Prompt" by pressing "Windows + R", type "cmd" in the window that appears, and press "OK".
- If you saved the folder on the Desktop you should be able to navigate to the folder by typing "cd Desktop\AlgorithmsInPython-master".
```
C:\Users\haag>cd Desktop\AlgorithmsInPython-master
```
- When in the correct folder, type `pip install .` to install the package. 
```
C:\Users\haag\Desktop\AlgorithmsInPython-master>pip install .
```
- After this, the package should be installed correctly and you can delete the folder from your Desktop.

## Test the installation
To test that the package is installed correctly, run python in interactive mode and enter `import algs4`.
```
➜  ~ python 
Python 3.7.6 | packaged by conda-forge | (default, Jan  7 2020, 22:33:48) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import algs4
>>> 
```
If no error message appears, the library has been installed correctly.

## Usage

The python package `algs4` and has a hierarchical structure. It has seven sub-packages, corresponding to: the first five chapters of [Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/), the `stdlib` package of [Introduction to Programming in Python](https://introcs.cs.princeton.edu/python/), and a package `error` containing some exception classes.

All filenames and package names have been written in lower_case style with underscores instead of the CamelCase style of the Java version. For example `EdgeWeightedDigraph.java` has been renamed to `edge_weighted_digraph.py`. Class names still use CamelCase though, which is consistent with naming conventions in Python.

### Example

A simple program, stored as a file `hello_world.py`, looks like this:
```python
import algs4.stdlib.stdio

algs4.stdlib.stdio.write("Hello World!\n")
```
It can be run with the command `python hello_world.py`.

You can import classes, such as the class EdgeWeightedDigraph, with
```python
from algs4.graphs.edge_weighted_digraph import EdgeWeightedDigraph
```

Some files contain multiple classes, for example:
```python
from algs4.fundamentals.uf import UF
from algs4.fundamentals.uf import QuickUnionUF
```

Look into the [examples](examples) directory for further examples.

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

## Development

`algs4-py` has known bugs and has not been tested systematically. We are open to pull requests, in particular, we appreciate the contribution of high-quality test cases, bug-fixes, and coding style improvements. For more information, see the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Contributors

- Andreas Holck Høeg-Petersen
- Anton Mølbjerg Eskildsen
- Frederik Haagensen
- Holger Dell
- Martino Secchi
- Morten Keller Grøftehauge
- Morten Tychsen Clausen
- Nina Mesing Stausholm Nielsen
- Otto Stadel Clausen
- Riko Jacob
- Thore Husfeldt
- Viktor Shamal Andersen

## License

This project is licensed under the GPLv3 License - see the [LICENSE](LICENSE) file for details

## Links to other projects

- [algs4](https://github.com/kevin-wayne/algs4/) is the original Java implementation by Sedgewick and Wayne.
- The textbook [Introduction to Programming in Python](https://introcs.cs.princeton.edu/python/) by Sedgewick, Wayne, and Dondero has a somewhat different approach from [Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/), and is therefore not suitable for a bilingual course. Nevertheless, our code in [algs4/stdlib/](algs4/stdlib/) is largely based on the [source code](https://introcs.cs.princeton.edu/python/code/) associated with that book.
- [pyalgs](https://github.com/chen0040/pyalgs) is a Python port of `algs4` that uses a more idiomatic Python coding style. In contrast, our port tries to stay as close to the original as possible, so that it can be used with less friction in a bilingual course.
- [Scala-Algorithms](https://github.com/garyaiki/Scala-Algorithms) is a Scala port of `algs4`.
- [Algs4Net](https://github.com/nguyenqthai/Algs4Net) is a .NET port of `algs4`.

