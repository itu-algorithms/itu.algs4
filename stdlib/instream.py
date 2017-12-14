"""
instream.py

The instream module defines the InStream class.
"""

#-----------------------------------------------------------------------

import sys
if sys.hexversion < 0x03000000:
    import urllib
else:
    import urllib.request as urllib
import re

#-----------------------------------------------------------------------

class InStream:

    """
    An InStream object wraps around a text file or sys.stdin, and
    supports reading from that stream.

    Note:  Usually it's a bad idea to mix these three sets of methods:

    -- isEmpty(), readInt(), readFloat(), readBool(), readString()

    -- hasNextLine(), readLine()
    
    -- readAll(), readAllInts(), readAllFloats(), readAllBools(),
       readAllStrings(), readAllLines()

    Usually it's better to use one set exclusively.
    """

    #-------------------------------------------------------------------

    def __init__(self, fileOrUrl=None):
        """
        Construct self to wrap around a stream. The stream can be
        a file whose name is given as fileOrUrl, a resource whose URL
        is given as fileOrUrl, or sys.stdin by default.
        """
        self._buffer = ''
        self._stream = None
        self._readingWebPage = False

        if fileOrUrl is None:
            import stdio # To change the mode of sys.stdin
            self._stream = sys.stdin
            return

        # Try to open a file, then a URL.
        try:
            if sys.hexversion < 0x03000000:
                self._stream = open(fileOrUrl,'rU')
            else:
                self._stream = open(fileOrUrl, 'r', encoding='utf-8')
        except IOError:
            try:
                self._stream = urllib.urlopen(fileOrUrl)
                self._readingWebPage = True
            except IOError:
                raise IOError('No such file or URL: ' + fileOrUrl)

    #-------------------------------------------------------------------

    def _readRegExp(self, regExp):
        """
        Discard leading white space characters from the stream wrapped
        by self.  Then read from the stream and return a string
        matching regular expression regExp.  Raise an EOFError if no
        non-whitespace characters remain in the stream. Raise a
        ValueError if the next characters to be read from the stream
        do not match regExp.
        """
        if self.isEmpty():
            raise EOFError()
        compiledRegExp = re.compile(r'^\s*' + regExp)
        match = compiledRegExp.search(self._buffer)
        if match is None:
            raise ValueError()
        s = match.group()
        self._buffer = self._buffer[match.end():]
        return s.lstrip()

    #-------------------------------------------------------------------

    def isEmpty(self):
        """
        Return True iff no non-whitespace characters remain in the
        stream wrapped by self.
        """
        while self._buffer.strip() == '':
            line = self._stream.readline()
            if sys.hexversion < 0x03000000 or self._readingWebPage:
                line = line.decode('utf-8')
            if line == '':
                return True
            self._buffer += str(line)
        return False

    #-------------------------------------------------------------------

    def readInt(self):
        """
        Discard leading white space characters from the stream wrapped
        by self.  Then read from the stream a sequence of characters
        comprising an integer.  Convert the sequence of characters to an
        integer, and return the integer.  Raise an EOFError if no
        non-whitespace characters remain in the stream.  Raise a
        ValueError if the next characters to be read from the stream
        cannot comprise an integer.
        """
        s = self._readRegExp(r'[-+]?(0[xX][\dA-Fa-f]+|0[0-7]*|\d+)')
        radix = 10
        strLength = len(s)
        if (strLength >= 1) and (s[0:1] == '0'): radix = 8
        if (strLength >= 2) and (s[0:2] == '-0'): radix = 8
        if (strLength >= 2) and (s[0:2] == '0x'): radix = 16
        if (strLength >= 2) and (s[0:2] == '0X'): radix = 16
        if (strLength >= 3) and (s[0:3] == '-0x'): radix = 16
        if (strLength >= 3) and (s[0:3] == '-0X'): radix = 16
        return int(s, radix)

    #-------------------------------------------------------------------

    def readAllInts(self):
        """
        Read all remaining strings from the stream wrapped by self,
        convert  each to an int, and return those ints in an array.
        Raise a ValueError if any of the strings cannot be converted
        to an int.
        """
        strings = self.readAllStrings()
        ints = []
        for s in strings:
            i = int(s)
            ints.append(i)
        return ints

    #-------------------------------------------------------------------

    def readFloat(self):
        """
        Discard leading white space characters from the stream wrapped
        by self.  Then read from the stream a sequence of characters
        comprising a float.  Convert the sequence of characters to an
        float, and return the float.  Raise an EOFError if no
        non-whitespace characters remain in the stream.  Raise a
        ValueError if the next characters to be read from the stream
        cannot comprise a float.
        """
        s = self._readRegExp(r'[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?')
        return float(s)

    #-------------------------------------------------------------------

    def readAllFloats(self):
        """
        Read all remaining strings from the stream wrapped by self,
        convert each to a float, and return those floats in an array.
        Raise a ValueError if any of the strings cannot be converted
        to a float.
        """
        strings = self.readAllStrings()
        floats = []
        for s in strings:
            f = float(s)
            floats.append(f)
        return floats

    #-------------------------------------------------------------------

    def readBool(self):
        """
        Discard leading white space characters from the stream wrapped
        by self.  Then read from the stream a sequence of characters
        comprising a bool.  Convert the sequence of characters to an
        bool, and return the bool.  Raise an EOFError if no
        non-whitespace characters remain in the stream.  Raise a
        ValueError if the next characters to be read from the stream
        cannot comprise an bool.
        """
        s = self._readRegExp(r'(True)|(False)|1|0')
        if (s == 'True') or (s == '1'):
            return True
        return False

    #-----------------------------------------------------------------------

    def readAllBools(self):
        """
        Read all remaining strings from the stream wrapped by self,
        convert each to a bool, and return those bools in an array.
        Raise a ValueError if any of the strings cannot be converted
        to a bool.
        """
        strings = self.readAllStrings()
        bools = []
        for s in strings:
            b = bool(s)
            bools.append(b)
        return bools


    #-------------------------------------------------------------------

    def readString(self):
        """
        Discard leading white space characters from the stream wrapped
        by self.  Then read from the stream a sequence of characters
        comprising a string, and return the string. Raise an EOFError
        if no non-whitespace characters remain in the stream.
        """
        s = self._readRegExp(r'\S+')
        return s

    #-----------------------------------------------------------------------

    def readAllStrings(self):
        """
        Read all remaining strings from the stream wrapped by self,
        and return them in an array.
        """
        strings = []
        while not self.isEmpty():
            s = self.readString()
            strings.append(s)
        return strings

    #-------------------------------------------------------------------

    def hasNextLine(self):
        """
        Return True iff the stream wrapped by self has a next line.
        """
        if self._buffer != '':
            return True
        else:
            self._buffer = self._stream.readline()
            if sys.hexversion < 0x03000000 or self._readingWebPage:
                self._buffer = self._buffer.decode('utf-8')
            if self._buffer == '':
                return False
            return True

    #-------------------------------------------------------------------

    def readLine(self):
        """
        Read and return as a string the next line of the stream wrapped
        by self.  Raise an EOFError is there is no next line.
        """
        if not self.hasNextLine():
            raise EOFError()
        s = self._buffer
        self._buffer = ''
        return s.rstrip('\n')

    #-------------------------------------------------------------------

    def readAllLines(self):
        """
        Read all remaining lines from the stream wrapped by self, and
        return them as strings in an array.
        """
        lines = []
        while self.hasNextLine():
            line = self.readLine()
            lines.append(line)
        return lines

    #-------------------------------------------------------------------

    def readAll(self):
        """
        Read and return as a string all remaining lines of the stream
        wrapped by self.
        """
        s = self._buffer
        self._buffer = ''
        for line in self._stream:
            if sys.hexversion < 0x03000000 or self._readingWebPage:
                line = line.decode('utf-8')
            s += line
        return s

    #-------------------------------------------------------------------

    def __del__(self):
        """
        Close the stream wrapped by self.
        """
        if self._stream is not None:
            self._stream.close()

#=======================================================================
# For Testing
#=======================================================================

def _main():
    """
    For testing. The first command-line argument should be the name of
    the method that should be called. The optional second command-line
    argument should be the file or URL to read.
    """

    import stdio

    testId = sys.argv[1]
    if len(sys.argv) > 2:
        inStream = InStream(sys.argv[2])
    else:
        inStream = InStream()

    if testId == 'readInt':
        stdio.writeln(inStream.readInt())
    elif testId == 'readAllInts':
        stdio.writeln(inStream.readAllInts())
    elif testId == 'readFloat':
        stdio.writeln(inStream.readFloat())
    elif testId == 'readAllFloats':
        stdio.writeln(inStream.readAllFloats())
    elif testId == 'readBool':
        stdio.writeln(inStream.readBool())
    elif testId == 'readAllBools':
        stdio.writeln(inStream.readAllBools())
    elif testId == 'readString':
        stdio.writeln(inStream.readString())
    elif testId == 'readAllStrings':
        stdio.writeln(inStream.readAllStrings())
    elif testId == 'readLine':
        stdio.writeln(inStream.readLine())
    elif testId == 'readAllLines':
        stdio.writeln(inStream.readAllLines())
    elif testId == 'readAll':
        stdio.writeln(inStream.readAll())

if __name__ == '__main__':
    _main()
