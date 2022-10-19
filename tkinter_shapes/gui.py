""" Wrappers for Tkinter graphical primitives to facilitate easy management of 
    the top-level Tkinter GUI window.

Examples
--------

Initialize a GUI window.

>>> gui = GUI()

Set the GUI dimensions and force the window to update.

>>> gui.dimensions = (800, 600)
>>> gui.update()

Verify the new dimensions.

>>> gui.width == 800
True
>>> gui.height == 600
True

Modify the width, update, and verify the change.

>>> gui.width = 600
>>> gui.update()  
>>> gui.dimensions == (600, 600)
True

Explicitly cleanup by destroying the GUI.

>>> gui.destroy()

"""

# Copyright 2022 Carnegie Mellon University Neuromechatronics Lab (a.whit)
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# 
# Contact: a.whit (nml@whit.contact)


# tkinter imports.
import tkinter


# GUI window class.
class GUI(tkinter.Tk):
    """ A GUI class to be used in place of tkinter.[Tk] to initialize a 
        [Toplevel] window.

    [Toplevel]: https://tkdocs.com/pyref/toplevel.html

    [Tk]: https://docs.python.org/3/library/tkinter.html#tkinter.Tk
    """
    
    @property
    def width(self):
        """ Integer width of the GUI window, in pixels. """
        return self.winfo_width()
    
    @width.setter
    def width(self, value): self.dimensions = (value, self.height)
        
    @property
    def height(self):
        """ Integer height of the GUI window, in pixels. """
        return self.winfo_height()
    
    @height.setter
    def height(self, value): self.dimensions = (self.width, value)
    
    @property
    def dimensions(self):
        """ Width and height of the GUI window. Structured as a 2-tuple. """
        return (self.width, self.height)
    
    @dimensions.setter
    def dimensions(self, value):
        (width, height) = value
        self.geometry(f'{width}x{height}')
    
  

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
  

