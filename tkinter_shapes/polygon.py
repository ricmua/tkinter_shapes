""" A wrapper for tkinter polygon [Canvas] items.

See the [create polygon command] reference for more information.

[Canvas]: https://tkdocs.com/tutorial/canvas.html

[create polygon command]: https://www.tcl.tk/man/tcl8.6/TkCmd/canvas.html#M151

Examples
--------

Initialize a tkinter instance.

>>> root = tkinter.Tk()
>>> result = root.geometry('800x600')

Create the canvas, set the canvas dimensions, and update the toplevel window.

>>> canvas = Canvas(root)
>>> canvas.dimensions = (600, 600)
>>> canvas.pack()
>>> root.update()

Update the canvas background color.

>>> canvas.background_color = 'green'
>>> canvas.update()

Add a polygon -- in the shape of a rotated triangle -- to the canvas. 
Verify that the item has been added to the canvas, and that the canvas 
coordinates of the polygon vertices are as expected.

>>> xy = [(100, 100), (200, 300), (300, 200)]
>>> item = Polygon(canvas=canvas, position=(200, 200), vertices=xy)
>>> canvas.find_all() == (item.id,)
True
>>> item.coordinates == [300.0, 300.0, 400.0, 500.0, 500.0, 400.0]
True
>>> canvas.update()

Verify the center-of-mass position and the dimensions of the bounding box.

>>> item.position
(400.0, 400.0)
>>> item.dimensions
(200.0, 200.0)

Color the triangle red with a yellow outline. Update the canvas to display the 
rectangle.

>>> item['fill'] = 'red'
>>> item['outline'] = 'yellow'
>>> canvas.update()

Draw the bounding box containing the polygon.

>>> xmin = min(item.coordinates[::2])
>>> ymin = min(item.coordinates[1::2])
>>> coordinates = [xmin, ymin, xmin+item.width, ymin+item.height]
>>> rectangle_id = canvas.create_rectangle(*coordinates)
>>> canvas.update()

Scale (shrink) the polygon. Verify that the position has not changed.

>>> item.dimensions = (100, 100)
>>> item.position
(400.0, 400.0)
>>> canvas.update()

Stretch the polygon along the horizontal axis.
Verify that the item has been added to the canvas, and that the canvas 
coordinates of the polygon vertices are as expected.

>>> item.width = 200
>>> item.coordinates == [300.0, 350.0, 400.0, 450.0, 500.0, 400.0]
True
>>> canvas.update()

Move the rectangle. 
Verify that the item has been added to the canvas, and that the canvas 
coordinates of the polygon vertices are as expected.

>>> item.position = (200, 100)
>>> canvas.coords(item.id) == [100.0, 50.0, 200.0, 150.0, 300.0, 100.0]
True
>>> canvas.update()

Reshape the polygon (convert the triangle to a quadrilateral).

>>> item.vertices = item.vertices + [(0, -100)]
>>> canvas.update()

Draw a circular polygon.

>>> circular_item = Circle(canvas, position=(200, 200), radius=50, fill='blue')
>>> circular_item.dimensions
(100.0, 100.0)
>>> canvas.update()

Change the circular outline color.

>>> circular_item['outline'] = 'blue'

Scale the circle to twice the radius.

>>> circular_item.radius = 200
>>> all([(abs(x-400) < 1e-6) for x in circular_item.dimensions])
True

Verify that the circle cannot be stretched / skewed to form a different shape.

>>> circular_item.dimensions = (100, 200)
>>> circular_item.radius
100.0
>>> canvas.update()

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


# Math imports.
from math import pi
from math import sqrt
from math import sin
from math import cos

# tkinter imports.
import tkinter

# Local imports.
from tkinter_shapes.canvas import Canvas
from tkinter_shapes.canvas import Item


# Polygon wrapper class.
class Polygon(Item):
    """ A wrapper for items created via tkinter.Canvas.create_polygon. """
    
    def __init__(self, canvas, position=(1,1), vertices=[(0, 0)], **kwargs):
        super().__init__(canvas=canvas)
        self.id = canvas.create_polygon(0, 0, **kwargs)
        self.position = position
        self.vertices = vertices
        
    @property
    def vertices(self):
        (x, y) = self.position
        coordinates = self.coordinates
        xy = list(zip(coordinates[::2], coordinates[1::2]))
        #xy = [(float(xn), float(yn)) for (xn, yn) in xy]
        xy = [(xn - x, yn - y) for (xn, yn) in xy]
        return xy
    
    @vertices.setter
    def vertices(self, value):
        (x, y) = self.position
        #value = [(float(xn), float(yn)) for (xn, yn) in value]        
        #print(f'Value: {value} ({type(value)} of length {len(value)}')
        xy = [(xn + x, yn + y) for (xn, yn) in value]        
        coordinates = [vk for v in xy for vk in v]
        self.coordinates = coordinates
    
    @property
    def position(self):
        """ Coordinates of the center of mass of the polygon. """
        coordinates = self.coordinates
        mean = lambda c: sum(c) / len(c)
        x = mean(coordinates[::2])
        y = mean(coordinates[1::2])
        return (x, y)
    
    @position.setter
    def position(self, value):
        
        # Distribute the position elements.
        (x, y) = value
        
        # Compute coordinates using current vertices.
        xy = [(xn + x, yn + y) for (xn, yn) in self.vertices]
        
        # Set the new coordinates.
        self.coordinates = [vk for v in xy for vk in v]
    
    @property
    def dimensions(self):
        """ Width and height of the polygon bounding box. 
            Structured as a 2-tuple. """
        return (self.width, self.height)
    
    @dimensions.setter
    def dimensions(self, value):
        
        # Compute scale factors.
        sx = value[0] / self.width  if (value[0] != None) else 1
        sy = value[1] / self.height if (value[1] != None) else 1
        
        ## Retrieve current position.
        #(x, y) = self.position
        #
        ## Apply the scale factors.
        #coordinates = self.coordinates
        #xy = list(zip(coordinates[::2], coordinates[1::2]))
        #xy = [(sx*(xn - x) + x, sy*(yn - y) + y) for (xn, yn) in xy]
        #print(f'1: {xy}')
        #
        ## Set the new coordinates.
        #self.coordinates = [vk for v in xy for vk in v]
        
        # Set the new vertices.
        self.vertices = [(sx*xn, sy*yn) for (xn, yn) in self.vertices]
        
    @property
    def width(self):
        """ Integer width of the polygon bounding box, in pixels. """
        extent = lambda c: max(c) - min(c)
        return extent(self.coordinates[::2])
    
    @width.setter
    def width(self, value): self.dimensions = (value, None)
            
    @property
    def height(self):
        """ Integer height of the polygon bounding box, in pixels. """
        extent = lambda c: max(c) - min(c)
        return extent(self.coordinates[1::2])
    
    @height.setter
    def height(self, value): self.dimensions = (None, value)
    
  

# Circular polygon class.
class Circle(Polygon):
    """ A polygon in the shape of a circle. """
    
    def __init__(self, canvas, position=(1,1), radius=1, N=100, **kwargs):
        super().__init__(canvas=canvas, 
                         position=position, 
                         vertices=[(radius, 0)]*N,
                         **kwargs)
    
    @property
    def radius(self):
        """ Radius of the circular polygon. """
        radii = [round(sqrt(xn**2 + yn**2), 6) for (xn, yn) in self.vertices]
        r = radii[0]
        assert all([(rn == r) for rn in radii])
        return r
      
    @radius.setter
    def radius(self, value): self.dimensions = (2*value, 2*value)
    
    @Polygon.vertices.setter
    def vertices(self, value):
        
        # Do not permit non-circular vertices.
        
        # Generate a new unit circle with a number of vertices equal to the 
        # number in the argument, and a radius equal to the maximum distance of 
        # a vertex to the center-of-mass.
        radii = [sqrt(xn**2 + yn**2) for (xn, yn) in value]
        r = max(radii)
        N = len(list(value))
        vertices = self._generate_unit_circle_vertices(N=N)
        vertices = [(r*xn, r*yn) for (xn, yn) in vertices]
        Polygon.vertices.fset(self, vertices)
    
    def _generate_unit_circle_vertices(self, N=100):
        """ Generate vertices for a unit circle centered at zero. """
        theta = [2*pi*n/N for n in range(N)]
        x = [cos(thetan) for thetan in theta]
        y = [sin(thetan) for thetan in theta]
        vertices = zip(x, y)
        return vertices
    
  

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
  

