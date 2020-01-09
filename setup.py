from setuptools import find_packages, setup

setup(
    name='algs4',
    version='0.2.1.7',
    description='Python 3 port of the Java code in "Algorithms, 4th Edition" by Sedgewick and Wayne',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    # author='',
    # author_email='',
    # url='',
    license='GPLv3',
    packages=find_packages(exclude=['examples', 'tests']),
    extras_require={
        'audio': ['numpy'],
        'visual': ['pygame'],
        'dev': ['flake8', 'isort', 'pytest', 'pytest-cov', 'coveralls'],
    },
)
