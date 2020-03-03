from setuptools import find_packages, setup

setup(
    name="itu.algs4",
    version="0.2.4",
    description='Python 3 port of the Java code in "Algorithms, 4th Edition" by Sedgewick and Wayne',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author='Algorithms group at ITU Copenhagen',
    # author_email='',
    url="https://github.com/itu-algorithms/itu.algs4/",
    license="GNU General Public License v3 (GPLv3)",
    packages=find_packages(exclude=["examples", "tests"]),
    include_package_data=True,
    extras_require={
        "audio": ["numpy"],
        "visual": ["pygame"],
        "dev": ["flake8", "black", "isort", "pytest", "pytest-cov", "coveralls", "mypy"],
    },
    zip_safe=False,
    platforms="any",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
