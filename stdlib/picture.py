"""
picture.py

The picture module defines the Picture class.
"""

#-----------------------------------------------------------------------

import pygame
import sys
import color
import stdarray
import os

#-----------------------------------------------------------------------

_DEFAULT_WIDTH = 512
_DEFAULT_HEIGHT = 512

#-----------------------------------------------------------------------

class Picture:
    """
    A Picture object models an image.  It is initialized such that
    it has a given width and height and contains all black pixels.
    Subsequently you can load an image from a given JPG or PNG file.
    """
    def __init__(self, arg1=None, arg2=None):
        """
        If both arg1 and arg2 are None, then construct self such that
        it is all black with _DEFAULT_WIDTH and height _DEFAULT_HEIGHT.
        If arg1 is not None and arg2 is None, then construct self by
        reading from the file whose name is arg1.
        If neither arg1 nor arg2 is None, then construct self such that
        it is all black with width arg1 and and height arg2.
        """
        if (arg1 is None) and (arg2 is None):
            maxW = _DEFAULT_WIDTH
            maxH = _DEFAULT_HEIGHT
            self._surface = pygame.Surface((maxW, maxH))
            self._surface.fill((0, 0, 0))
        elif (arg1 is not None) and (arg2 is None):
            fileName = arg1
            try:
                self._surface = pygame.image.load(fileName)
            except pygame.error:
                raise IOError()
        elif (arg1 is not None) and (arg2 is not None):
            maxW = arg1
            maxH = arg2
            self._surface = pygame.Surface((maxW, maxH))
            self._surface.fill((0, 0, 0))
        else:
            raise ValueError()
            
    #-------------------------------------------------------------------

    #def load(self, f):
    #    """
    #    Change self by reading from the file whose name is f. The
    #    dimensions of the read image override the dimensions specified
    #    in the constructor.
    #    """
        #if sys.hexversion >= 0x03000000:
        #    # Hack because Pygame without full image support
        #    # can handle only .bmp files.
        #    bmpFileName = f + '.bmp'
        #    os.system('convert ' + f + ' ' + bmpFileName)
        #    self._surface = pygame.image.load(bmpFileName)
        #    os.system('rm ' + bmpFileName)
        #else:
        #    self._surface = pygame.image.load(f)

    #    self._surface = pygame.image.load(f)

    #-------------------------------------------------------------------

    def save(self, f):
        """
        Save self to the file whose name is f.
        """
        #if sys.hexversion >= 0x03000000:
        #    # Hack because Pygame without full image support
        #    # can handle only .bmp files.
        #    bmpFileName = f + '.bmp'
        #    pygame.image.save(self._surface, bmpFileName)
        #    os.system('convert ' + bmpFileName + ' ' + f)
        #    os.system('rm ' + bmpFileName)
        #else:
        #    pygame.image.save(self._surface, f)

        pygame.image.save(self._surface, f)

    #-------------------------------------------------------------------

    def width(self):
        """
        Return the width of self.
        """
        return self._surface.get_width()

    #-------------------------------------------------------------------

    def height(self):
        """
        Return the height of self.
        """
        return self._surface.get_height()

    #-------------------------------------------------------------------

    def get(self, x, y):
        """
        Return the color of self at location (x, y).
        """
        pygameColor = self._surface.get_at((x, y))
        return color.Color(pygameColor.r, pygameColor.g, pygameColor.b)

    #-------------------------------------------------------------------

    def set(self, x, y, c):
        """
        Set the color of self at location (x, y) to c.
        """
        pygameColor = pygame.Color(c.getRed(), c.getGreen(),
           c.getBlue(), 0)
        self._surface.set_at((x, y), pygameColor)
