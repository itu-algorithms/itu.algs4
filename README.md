# Algs4 for Python

This repository contains the Python3 version of the Java code in [Algorithms, 4th Edition](https://algs4.cs.princeton.edu/home/) by Sedgewick and Wayne.

## Installing Python on a Windows machine
This guide describes step by step how to install Python3 and the algs4 package.
The goal is to go from this:
```
 'python' is not recognized as an internal or external command,
  operable program or batch file.
```
To this:
```
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from algs4.fundamentals.uf import UF
>>> 
```
If you have already installed python 3 simply skip to the next section.

To download python 3, follow the link https://www.python.org/downloads/windows/ and pick the most appropriate installer for your system, download and run it. (I choose Windows x86-64 executable installer since I run a 64 bit operating system.)

In the installer make sure to toggle the "Add Python to Path" checkbox on, before pressing "Install Now".

After the installation is complete you can close the installer, and test that it works correctly.

Open the "Command Prompt" by pressing "Windows + R", type "cmd" in the window that appears, and press "OK".

In the "Command Prompt" try typing "python" to run python, if everything works you should see something like this
```
C:\Users\haag>python
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
If nothing shows up you might not have toggled the "Add Python to Path" checkbox before installing, try reinstalling or alternatively google "how to add python to path windows" to do it manually.

## Installing this algs4 package

In order for the package to work, you must have `python3` and `setup-tools`/`pip3` (or `pip`, change the command below) already installed - see [python homepage](https://python.org) for instructions. Also, some optional visual and auditory features require the `numpy` and `pygame` packages to work - see [numpy homepage](http://numpy.org) and [pygame homepage](https://pygame.org) for instructions.
If you are in this situation, the following command, combined with your ITU credentials, should work:
```bash
pip install svn+https://github.itu.dk/algorithms/AlgorithmsInPython
```

Otherwise, you can manually install it as follows:

1. Download and unzip (or clone) the repository.
2. Open a command prompt or terminal and navigate to the downloaded folder. There should be the file `setup.py`.
3. Use the command `pip3 install .` to install the package (this will also work for updating the package, when a newer version is available).  If your python installation is system wide, use `sudo pip3 install .`

Optionally you can install `numpy` and `pygame` using `pip3 install numpy pygame` or `sudo pip3 install numpy pygame`. Please refer to the home pages of the respective packages if you encounter any problems during installation. 

*Note:* If you're using `virtualenv` or `anaconda` make sure to activate/select the desired environment before installing.

If you changed the repository, you need to reinstall. For that purpose, you need to increase the version number in `setup.py`.

## Installing this algs4 package on a Windows machine

To install the algs4 package go to https://github.itu.dk/algorithms/AlgorithmsInPython (you might have to login to your ITU github - use the same username and password as you use for learnit).

There should be instructions for how to install the package on the github, but for completeness sake I will repeat them here.

Download the repository by pressing the green "Clone or download" button, and pressing "Download ZIP".

Extract the content of the zip to your Desktop (you can delete the folder after installing the package).

You'll want to navigate the "Command Prompt" to the folder.

Open the "Command Prompt" by pressing "Windows + R", type "cmd" in the window that appears, and press "OK".

If you saved the folder on the Desktop you should be able to navigate to the folder by typing "cd Desktop\AlgorithmsInPython-master".
```
C:\Users\haag>cd Desktop\AlgorithmsInPython-master
```
When in the correct folder simply type "pip install ." to install the package. 
```
C:\Users\haag\Desktop\AlgorithmsInPython-master>pip install .
```
After this the package should be installed correctly and you can delete the folder from your Desktop.

To test that the package is installed correctly open the "Command Prompt", and type "python". 
In the interactive shell try typing "from algs4.fundamentals.uf import UF".
```
C:\Users\haag>python
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from algs4.fundamentals.uf import UF
>>> 
```
If something went wrong try to make sure you followed all the instructions correctly, otherwise feel free to post your problems on piazza.

## Usage

The package is divided into five sub-packages representing the first five chapters of "Algorithms 4th, Edition", as well as the `stdlib` package from [this book](https://introcs.cs.princeton.edu/python/code/) (with slight modification), and a package containing a number of exception classes. 

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


## Importing

Besides the hierarchical structure, all class- and file-names from the book have been written in lower-case style with underscores instead of the Pascal case style of the Java version. For example `EdgeWeightedDigraph.java` has been renamed to `edge_weighted_digraph.py`. Class names still use Pascal case though (following Python convention).

**Example**

```python
# Importing the Digraph class 
from algs4.graphs.edge_weighted_digraph import EdgeWeightedDigraph

# Some files contain multiple classes, for example:
from algs4.fundamentals.uf import UF
from algs4.fundamentals.uf import QuickUnionUF
```

## Documentation

You can use the built-in `help` function on any public class or function to get a description of what it does. This documentation should also work with your IDE of choice.
