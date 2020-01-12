# Created for BADS 2018
# See README.md for details
# this one is not inspired by algorithms from the book, but useful for running java and python in parallel
# Python 3

def java_string_hash(key):
    """ If key is a string, compute its java .hash() code. Taken from http://garage.pimentech.net/libcommonPython_src_python_libcommon_javastringhashcode/ """
    h = 0
    for c in key:
        h = (31 * h + ord(c)) & 0xFFFFFFFF
    return ((h + 0x80000000) & 0xFFFFFFFF) - 0x80000000

def trailing_zeros(i):
    zeros = 0
    while i & 1 == 0 and zeros < 32:
        zeros += 1
        i = i >> 1
    return zeros
