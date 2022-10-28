""" A wrapper for the tkinter [Canvas] class.

See the [Tk canvas command] reference for more information.

[Canvas]: https://tkdocs.com/tutorial/canvas.html

[Tk canvas command]: https://www.tcl.tk/man/tcl8.6/TkCmd/canvas.html

Examples
--------

Initialize a tkinter instance.

>>> root = tkinter.Tk()
>>> result = root.geometry('800x600')

Create the canvas, set the canvas dimensions, and update the toplevel window.

>>> canvas = Canvas(root)
>>> canvas.dimensions = (800, 600)
>>> canvas.pack()
>>> root.update()

Verify the canvas dimensions.

>>> canvas.width == 800
True
>>> canvas.height == 600
True

Update the canvas background color.

>>> canvas.background_color = 'green'
>>> canvas.update()
>>> canvas.background_color == 'green'
True

Modify the canvas width.

>>> canvas.width = 600
>>> canvas.update()
>>> canvas.width == 600
True

Add a rectangle to the canvas.

>>> canvas.find_all() == ()
True
>>> item = Item(canvas=canvas)
>>> item.id = canvas.create_rectangle(0, 0, 1, 1, fill='red')
>>> canvas.update()
>>> canvas.find_all() == (item.id,)
True

Resize the rectangle.

>>> item.coordinates = (100, 100, 300, 200)
>>> canvas.update()

Change the default black outline of the rectangle to yellow.

>>> item['outline'] = 'yellow'
>>> canvas.update()

Remove the rectangle from the canvas and destroy.

>>> #item.delete() 
>>> del item
>>> canvas.update()
>>> canvas.find_all() == ()
True

Explicitly cleanup by destroying the toplevel window.

>>> root.destroy()

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


# Canvas wrapper class.
class Canvas(tkinter.Canvas):
    """ A wrapper for tkinter.Canvas. """
    
    @property
    def background_color(self):
        """ Canvas background [color].
        
        [color]: https://tkdocs.com/tutorial/fonts.html#colors
        """
        return self.cget('bg')
    
    @background_color.setter
    def background_color(self, value): self.configure(bg=value)
    
    @property
    def width(self):
        """ Integer width of the canvas, in pixels. """
        return int(self.cget('width'))
    
    @width.setter
    def width(self, value): self.configure(width=value)
        
    @property
    def height(self):
        """ Integer height of the canvas, in pixels. """
        return int(self.cget('height'))
    
    @height.setter
    def height(self, value): self.configure(height=value)
    
    @property
    def dimensions(self):
        """ Width and height of the canvas. Structured as a 2-tuple. """
        return (self.width, self.height)
    
    @dimensions.setter
    def dimensions(self, value): self.configure(width=value[0], height=value[1])
    
  

# Item wrapper (base) class.
class Item:
    """ A wrapper for Tkinter Canvas items.
    
    Notes
    -----
    
    Changes to options and parameters in this class take effect immediately, but
    might not be visible until the Tkinter canvas is updated. This is a common 
    mistake.
    """
    
    def __init__(self, canvas):
        self.canvas = canvas
    
    @property
    def canvas(self):
        """ Tkinter Canvas with which the item is associated. """
        return self._canvas
    
    @canvas.setter
    def canvas(self, value): self._canvas = value
    
    @property
    def id(self):
        """ Unique Tkinter canvas item ID. """
        return self._id
    
    @id.setter
    def id(self, value : int): self._id = value
    
    @property
    def coordinates(self): 
        """ Tkinter canvas coordinates. """
        return self.canvas.coords(self.id)
        
    @coordinates.setter
    def coordinates(self, value): self.canvas.coords(self.id, *value)
        
    def __getitem__(self, key):
        """ Get option values for a Tkinter canvas item. """
        return self.canvas.itemcget(self.id, key)
        
    def __setitem__(self, key, value):
        """ Set options for a Tkinter canvas item. """
        self.canvas.itemconfigure(self.id, **{key: value})
        
    def delete(self):
        """ Remove the item from the canvas. """
        self.canvas.delete(self.id)
        
    def __del__(self):
        """ Destructor that removes the item from the canvas. """
        try: self.canvas.delete(self.id)
        except tkinter.TclError as e:
            if str(e) != 'invalid command name ".!canvas"': raise e
    
  
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
  

