# Development

## Testing

Before you can run tests, you should clone the repository, and install the
package in "editable" mode, including its development dependencies:
```bash
pip install --upgrade -e '.[dev]'
```
Run all tests as follows:
```bash
pytest
```
To additionally display code coverage statistics, use this:
```bash
pytest --cov-report term-missing --cov itu.algs4
```
To run individual tests, you can also do this:
```
python3 -m unittest tests/test_bst.py
pytest tests/test_stack.py
```

## Linter

Run `flake8` to lint all code. We currently only enforce linting on [examples/](examples) and [tests/](tests).
Moreover, run
```
isort -rc
```
to sort import statements.

## Types

Weak type checking is currently enforced only on [examples/](examples) and [tests/](tests). To run the type checker, try:
```
mypy
```
Ideally, we want every module to strictly type check. For example, the binary search trees strictly type check:
```
mypy --strict itu/algs4/searching/bst.py itu/algs4/searching/red_black_bst.py itu/algs4/fundamentals/queue.py
```


## Examples

Client code should be migrated to [examples/](examples).

## Uploading to PyPi

Create package and upload it:
```bash
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
```

## Useful Resources

- the book https://algs4.cs.princeton.edu/home/
- a python version of a similar book https://introcs.cs.princeton.edu/python/home/
- all java code -- good list, includes what needs to be done https://algs4.cs.princeton.edu/code/ https://github.com/kevin-wayne/algs4

## Coding style 

https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions

- we have subdirectories for the code, one for each chapter

- if java relies on having different implementations depending on the type:
Use somehting like
```
class DirectedDFS:
	def __init__(self, G, *s):
```
like in `graphs/directed_dfs.py`

Otherwise we use static factory methods where the name indicates the expected type.
If appropriate we use `isinstance()` and its variants, for example to distinguish undirected and directed graphs. 

- things like 'node' are inside classes, no leading underscore

- file names, variables, methods are file_name (and not CamelCase, adjustting from algs4), only classes are CamelCase (PascalCase)

- there is one file per version of an algorithm / data structure (like in algs4), the name, and importantly the docstring, reflects which version it is

- java main becomes `__main__` stuff; follow what is there; adjust the initial comment

- don't replicate imports unless 

- lower case letter with underscore
  - like in the book
  - private variables become _variable_name

- if java has `toString()`, then we have `__repr__()`

- keep the comments from the java code 

- if in doubt, we go with the book, not the code on the book web site (keep it simple)

- docstring without formatting

## ideas
- should we include generators (additionally to iterators) everywhere?

