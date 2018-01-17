from setuptools import setup, find_packages

setup(
    name="pyalgs",
    version="0.1",
    packages=find_packages(exclude=['algs4_data']),
    
    description="A translation of the algorithms covered in the book Algorithms 4th edition, for use in an introductory algorithms course at The IT University of Copenhagen.",
    
)