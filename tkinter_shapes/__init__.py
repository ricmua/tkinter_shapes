""" Simple tkinter wrappers intended to facilitate manipulation of shapes and 
    polygons rendered on a canvas.

Examples
--------

>>> gui = GUI()
>>> gui.dimensions = (800, 600)

>>> canvas = Canvas(gui)
>>> canvas.pack()
>>> canvas.dimensions = (600, 600)
>>> canvas.background_color = 'black'

>>> circle_a = Circle(canvas=canvas, position=(100, 100), radius=50, N=100000)
>>> circle_b = Circle(canvas=canvas, fill='green', position=(200, 300), N=1000)

>>> circle_a['outline'] = circle_a['fill'] = 'blue'
>>> circle_b['outline'] = 'green'
>>> circle_b.radius = 50

>>> canvas.update()

>>> del circle_a
>>> circle_b.delete()
>>> gui.destroy()

"""

# Copyright 2022 Carnegie Mellon University Neuromechatronics Lab (a.whit)
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# 
# Contact: a.whit (nml@whit.contact)


# Define the version.
__version__ = '0.0.1'

# Import local objects.
from tkinter_shapes.gui import GUI
from tkinter_shapes.canvas import Canvas
from tkinter_shapes.polygon import Polygon
from tkinter_shapes.polygon import Circle
#from .rectangle import Rectangle

# Run doctests.
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)
    
  


