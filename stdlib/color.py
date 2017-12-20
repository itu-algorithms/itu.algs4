"""
color.py

The color module defines the Color class and some popular Color
objects.
"""

#-----------------------------------------------------------------------

class Color:
    """
    A Color object models an RGB color.
    """

    #-------------------------------------------------------------------

    def __init__(self, r=0, g=0, b=0):
        """
        Construct self such that it has the given red (r),
        green (g), and blue (b) components.
        """
        self._r = r  # Red component
        self._g = g  # Green component
        self._b = b  # Blue component

    #-------------------------------------------------------------------

    def getRed(self):
        """
        Return the red component of self.
        """
        return self._r

    #-------------------------------------------------------------------

    def getGreen(self):
        """
        Return the green component of self.
        """
        return self._g

    #-------------------------------------------------------------------

    def getBlue(self):
        """
        Return the blue component of self.
        """
        return self._b

    #-------------------------------------------------------------------


    def __str__(self):
        """
        Return the string equivalent of self, that is, a
        string of the form '(r, g, b)'.
        """
        #return '#%02x%02x%02x' % (self._r, self._g, self._b)
        return '(' + str(self._r) + ', ' + str(self._g) + ', ' + \
            str(self._b) + ')'

#-----------------------------------------------------------------------

# Some predefined Color objects:

WHITE      = Color(255, 255, 255)
BLACK      = Color(  0,   0,   0)

RED        = Color(255,   0,   0)
GREEN      = Color(  0, 255,   0)
BLUE       = Color(  0,   0, 255)

CYAN       = Color(  0, 255, 255)
MAGENTA    = Color(255,   0, 255)
YELLOW     = Color(255, 255,   0)

DARK_RED   = Color(128,   0,   0)
DARK_GREEN = Color(  0, 128,   0)
DARK_BLUE  = Color(  0,   0, 128)

GRAY       = Color(128, 128, 128)
DARK_GRAY  = Color( 64,  64,  64)
LIGHT_GRAY = Color(192, 192, 192)

ORANGE     = Color(255, 200,   0)
VIOLET     = Color(238, 130, 238)
PINK       = Color(255, 175, 175)

# Shade of blue used in Introduction to Programming in Java.
# It is Pantone 300U. The RGB values are approximately (9, 90, 166).
BOOK_BLUE  = Color(  9,  90, 166)
BOOK_LIGHT_BLUE = Color(103, 198, 243)

# Shade of red used in Algorithms 4th edition
BOOK_RED   = Color(150,  35,  31)

#-----------------------------------------------------------------------

def _main():
    """
    For testing:
    """
    import stdio
    c1 = Color(128, 128, 128)
    stdio.writeln(c1)
    stdio.writeln(c1.getRed())
    stdio.writeln(c1.getGreen())
    stdio.writeln(c1.getBlue())

if __name__ == '__main__':
    _main()
