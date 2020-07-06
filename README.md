# Algs4 library for Python 3

`itu.algs4` is a Python 3 port of the Java code in [Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/).

[![Build Status](https://github.com/itu-algorithms/itu.algs4/workflows/check/badge.svg)](https://github.com/itu-algorithms/itu.algs4/actions)
[![Documentation Status](https://readthedocs.org/projects/itualgs4/badge/?version=latest)](https://itualgs4.readthedocs.io/en/latest/?badge=latest)

## Target audience

`itu.algs4` is intended for instructors and students who wish to follow the textbook [Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/) by Sedgewick and Wayne.
It was first created in 2018 by teaching assistants and instructors at [ITU Copenhagen](https://algorithms.itu.dk), where the introductory course on Algorithms and Data Structures is taught bilingually in Java and Python 3.

## Installation

This library requires a functioning Python 3 environment, for example the one provided by [Anaconda](https://www.anaconda.com/distribution/).

Some optional visual and auditory features depend on the [numpy](http://numpy.org) and [pygame](https://pygame.org) packages. These features are not used in the ITU course, and you shouldn’t spend extra time on installing those packages unless you already have them or want to play around with the those parts on your own. 

### With pip

If you have previously installed this package under its old name, we recommend you remove it with
```bash
pip uninstall algs4 algs4_python
```
Then you can install `itu.algs4` simply with
```bash
pip install itu.algs4
```
If you have already installed `itu.algs4` and want to upgrade to a new version, run:
```bash
pip install itu.algs4 --upgrade
```
To test that you have installed the library correctly, run this command:
```bash
python -c 'from itu.algs4.stdlib import stdio; stdio.write("Hello World!")'
```
It should greet you. If an error message appears instead, the library is not installed correctly.

### Alternative: With pip and git

If git is available, the following command will install the library in your Python environment:

```bash
pip install git+https://github.com/itu-algorithms/itu.algs4
```

### Alternative: With pip and zip

To install this library without git:

1. Download and unzip the repository.
2. Open a command prompt or terminal and navigate to the downloaded folder. There should be the file `setup.py`.
3. Use the command `pip3 install .` to install the package (this will also work for updating the package, when a newer version is available).  If your Python installation is system-wide, use `sudo pip3 install .`

### Alternative: Step-by-step guide for Windows

To install the Python package `itu.algs4`:

- Download the repository by pressing the green "Clone or download" button, and pressing "Download ZIP".
- Extract the content of the zip to your Desktop (you can delete the folder after installing the package).
- Open the "Command Prompt" by pressing "Windows + R", type "cmd" in the window that appears, and press "OK".
- If you saved the folder on the Desktop you should be able to navigate to the folder by typing "cd Desktop\itu.algs4-master".
```
C:\Users\user>cd Desktop\itu.algs4-master
```
- When in the correct folder, type `pip install .` to install the package. 
```
C:\Users\user\Desktop\itu.algs4-master>pip install .
```
- After this, the package should be installed correctly and you can delete the folder from your Desktop.

## Package structure

The Python package `itu.algs4` has a hierarchical structure with seven sub-packages:

- [itu.algs4.fundamentals](itu/algs4/fundamentals)
- [itu.algs4.sorting](itu/algs4/sorting)
- [itu.algs4.searching](itu/algs4/searching)
- [itu.algs4.graphs](itu/algs4/graphs)
- [itu.algs4.strings](itu/algs4/strings)
- [itu.algs4.stdlib](itu/algs4/stdlib)
- [itu.algs4.errors](itu/algs4/errors)

While deep nesting of packages is normally [discouraged](https://www.python.org/dev/peps/pep-0423/#avoid-deep-nesting) in Python, an important design goal of `itu.algs4` was to mirror the structure of the original Java code.
The first five packages correspond to the first five chapters of [Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/). The `stdlib` package is based on the one from the related book [Introduction to Programming in Python](https://introcs.cs.princeton.edu/python/). The package `errors` contains some exception classes.

All filenames and package names have been written in lower_case style with underscores instead of the CamelCase style of the Java version. For example `EdgeWeightedDigraph.java` has been renamed to `edge_weighted_digraph.py`. Class names still use CamelCase though, which is consistent with naming conventions in Python.

## Examples

The directory [examples/](examples) contains examples, some of which are
described here.

### Hello World
A simple program, stored as a file [hello_world.py](examples/hello_world.py), looks like this:
```python
from itu.algs4.stdlib import stdio

stdio.write("Hello World!\n")
```
It can be run with the command `python hello_world.py`.

### Sort numbers
A slightly more interesting example is
[sort-numbers.py](examples/sort-numbers.py):
```python
from itu.algs4.sorting import merge
from itu.algs4.stdlib import stdio

"""
Reads a list of integers from standard input.
Then prints it in sorted order.
"""
L = stdio.readAllInts()

merge.sort(L)

if len(L) > 0:
    stdio.write(L[0])
for i in range(1, len(L)):
    stdio.write(" ")
    stdio.write(L[i])
stdio.writeln()
```
This code uses the convenient function `stdio.readAllInts()` to read the
integers (separated by whitespaces) from the standard input and put them in the
array `L`. It then sorts the elements of the array. Finally, it outputs the
sorted list -- the code to do so is somewhat less elegant to get the whitespace
exactly right. (Of course, advanced Python users know more concise ways to
produce the same output: `print(" ".join(map(str, L)))`)

### Import classes
You can import classes, such as the class EdgeWeightedDigraph, with
```python
from itu.algs4.graphs.edge_weighted_digraph import EdgeWeightedDigraph
```


## Documentation

The documentation can be found [here](https://itualgs4.readthedocs.io/en/latest/).

You can use Python's built-in `help` function on any package, sub-package, public class, or function to get a description of what it contains or does. This documentation should also show up in your IDE of choice.
For example `help(itu.algs4)` yields the following:

```
Help on package itu.algs4 in itu:

NAME
    itu.algs4

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

`itu.algs4` has known bugs and has not been tested systematically. We are open to pull requests, and in particular, we appreciate the contribution of high-quality test cases, bug-fixes, and coding style improvements. For more information, see the [CONTRIBUTING.md](CONTRIBUTING.md) file.

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
- The textbook [Introduction to Programming in Python](https://introcs.cs.princeton.edu/python/) by Sedgewick, Wayne, and Dondero has a somewhat different approach from [Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/), and is therefore not suitable for a bilingual course. Nevertheless, our code in [itu/algs4/stdlib/](itu/algs4/stdlib/) is largely based on the [source code](https://introcs.cs.princeton.edu/python/code/) associated with that book.
- [pyalgs](https://github.com/chen0040/pyalgs) is a Python port of `algs4` that uses a more idiomatic Python coding style. In contrast, our port tries to stay as close to the original Java library and the course book’s Java implementations as possible, so that it can be used with less friction in a bilingual course.
- [Scala-Algorithms](https://github.com/garyaiki/Scala-Algorithms) is a Scala port of `algs4`.
- [Algs4Net](https://github.com/nguyenqthai/Algs4Net) is a .NET port of `algs4`.

