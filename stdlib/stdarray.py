"""
stdarray.py

The stdarray module defines functions related to creating, reading,
and writing one- and two-dimensional arrays.
"""

import stdio

#=======================================================================
# Array creation functions
#=======================================================================

def create1D(length, value=None):
    """
    Create and return a 1D array containing length elements, each
    initialized to value.
    """
    return [value] * length

#-----------------------------------------------------------------------

def create2D(rowCount, colCount, value=None):
    """
    Create and return a 2D array having rowCount rows and colCount
    columns, with each element initialized to value.
    """
    a = [None] * rowCount
    for row in range(rowCount):
        a[row] = [value] * colCount
    return a

#=======================================================================
# Array writing functions
#=======================================================================

def write1D(a):
    """
    Write array a to sys.stdout.  First write its length. bool objects
    are written as 0 and 1, not False and True.
    """
    length = len(a)
    stdio.writeln(length)
    for i in range(length):
        # stdio.writef('%9.5f ', a[i])
        element = a[i]
        if isinstance(element, bool):
            if element == True:
                stdio.write(1)
            else:
                stdio.write(0) 
        else:
            stdio.write(element)
        stdio.write(' ')
    stdio.writeln()

#-----------------------------------------------------------------------

def write2D(a):
    """
    Write two-dimensional array a to sys.stdout.  First write its
    dimensions. bool objects are written as 0 and 1, not False and True.
    """
    rowCount = len(a)
    colCount = len(a[0])
    stdio.writeln(str(rowCount) + ' ' + str(colCount))
    for row in range(rowCount):
        for col in range(colCount):
            #stdio.writef('%9.5f ', a[row][col])
            element = a[row][col]
            if isinstance(element, bool):
                if element == True:
                    stdio.write(1)
                else:
                    stdio.write(0)
            else:
                stdio.write(element)
            stdio.write(' ')
        stdio.writeln()

#=======================================================================
# Array reading functions
#=======================================================================

def readInt1D():
    """
    Read from sys.stdin and return an array of integers. An integer at
    the beginning of sys.stdin defines the array's length.
    """
    count = stdio.readInt()
    a = create1D(count, None)
    for i in range(count):
        a[i] = stdio.readInt()
    return a

#-----------------------------------------------------------------------

def readInt2D():
    """
    Read from sys.stdin and return a two-dimensional array of integers.
    Two integers at the beginning of sys.stdin define the array's
    dimensions.
    """
    rowCount = stdio.readInt()
    colCount = stdio.readInt()
    a = create2D(rowCount, colCount, 0)
    for row in range(rowCount):
        for col in range(colCount):
            a[row][col] = stdio.readInt()
    return a

#-----------------------------------------------------------------------

def readFloat1D():
    """
    Read from sys.stdin and return an array of floats. An integer at the
    beginning of sys.stdin defines the array's length.
    """
    count = stdio.readInt()
    a = create1D(count, None)
    for i in range(count):
        a[i] = stdio.readFloat()
    return a

#-----------------------------------------------------------------------

def readFloat2D():
    """
    Read from sys.stdin and return a two-dimensional array of floats.
    Two integers at the beginning of sys.stdin define the array's
    dimensions.
    """
    rowCount = stdio.readInt()
    colCount = stdio.readInt()
    a = create2D(rowCount, colCount, 0.0)
    for row in range(rowCount):
        for col in range(colCount):
            a[row][col] = stdio.readFloat()
    return a

#-----------------------------------------------------------------------

def readBool1D():
    """
    Read from sys.stdin and return an array of booleans. An integer at
    the beginning of sys.stdin defines the array's length.
    """
    count = stdio.readInt()
    a = create1D(count, None)
    for i in range(count):
        a[i] = stdio.readBool()
    return a

#-----------------------------------------------------------------------

def readBool2D():
    """
    Read from sys.stdin and return a two-dimensional array of booleans.
    Two integers at the beginning of sys.stdin define the array's
    dimensions.
    """
    rowCount = stdio.readInt()
    colCount = stdio.readInt()
    a = create2D(rowCount, colCount, False)
    for row in range(rowCount):
        for col in range(colCount):
            a[row][col] = stdio.readBool()
    return a

#=======================================================================

def _main():
    """
    For testing.
    """
    write2D(readFloat2D())
    write2D(readBool2D())

if __name__ == '__main__':
    _main()
