from setuptools import setup, find_packages

setup(
    name="algs4_python",
    version="0.2.0.16",
    packages= [
        'algs4.fundamentals',
        'algs4.sorting',
        'algs4.searching',
        'algs4.graphs',
        'algs4.strings',
        'algs4.stdlib',
        'algs4.errors'
        ],
    
    #package_dir = {
    #    'algs4.fundamentals': './fundamentals',
    #    'algs4.sorting': './sorting',
    #    'algs4.searching': './searching',
    #    'algs4.graphs': './graphs',
    #    'algs4.strings': './strings',
    #    'algs4.stdlib': './stdlib',
    #    'algs4.errors': './errors'        
    #},
    
    description="A translation of the algorithms covered in the book Algorithms 4th edition, for use in an introductory algorithms course at The IT University of Copenhagen.",
    
    install_requires = [
       # 'numpy',
        'pygame',
    ],
    
)
