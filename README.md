---
title: README
author: a.whit ([email](mailto:nml@whit.contact))
date: October 2022
---

<!-- License

Copyright 2022 Neuromechatronics Lab, Carnegie Mellon University (a.whit)

Created by: a. whit. (nml@whit.contact)

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
-->


# tkinter_shapes

A Python package that implements simple [tkinter] wrappers that are intended to 
facilitate manipulation of shapes and polygons rendered on a canvas. The 
primary objective is to provide a simple, intuitive interface to a limited 
subset of Tk functionality.

## Installation

The package can be used as-is, so long as the [Python path] is set 
appropriately.
                 
However, a ``setup.cfg`` file has been provided, to facilitate package 
installation via [setuptools]. Package installation can be accomplished via the 
command:

```
pip install path/to/tkinter_shapes
```

## Getting started

Perhaps the best way to introduce the package functionality is via an example. 

The first step is to create a graphical user interface (GUI) window. Import the 
GUI class and create an instance.

```python
>>> from tkinter_shapes import GUI
>>> gui = GUI()
```

Although the GUI might initialize without any issue, the top-level window 
itself will not be visible until the GUI is updated. This is a common mistake: 
the GUI or canvas must be updated before any changes are visible.

```python
>>> gui.update()
```

Try resizing the GUI window.

```python
>>> gui.dimensions = (800, 600)
>>> gui.update()
```

Shapes are drawn on a canvas widget. Initialize a canvas with a black 
background color.

```python
>>> from tkinter_shapes import Canvas
>>> canvas = Canvas(gui)
>>> canvas.background_color = 'black'
>>> canvas.pack()
>>> gui.update()
```

Reshape the canvas to be a square that fills the available space.

```python
>>> canvas.dimensions = (600, 600)
>>> canvas.update()
```

Initialize a circle on the canvas. The circle is drawn as a polygon. Set the 
number of polygon vertices to `1000`, in order to draw a smooth shape.

```python
>>> from tkinter_shapes import Circle
>>> circle = Circle(canvas=canvas, position=(100, 100), radius=50, N=1000)
```

The default color is black, so the circle will not be visible. Set the circle 
outline and fill color to blue.<!-- [^canvas_image] -->

```python
>>> circle['outline'] = circle['fill'] = 'blue'
>>> canvas.update()
```

<!-- 
[^canvas_image]: The canvas should appear as pictured. The image was created 
                 via the tkinter [Canvas postscript] command. A black rectangle 
                 was inserted to represent the canvas background.

[Canvas postscript]: https://www.tcl.tk/man/tcl8.6/TkCmd/canvas.html#M61

![The canvas after creating the circle.](assets/image/example_canvas-1.svg)
-->

Query the dimensions of the circle bounding box, before and after resizing it.

```python
>>> circle.dimensions
(100.0, 100.0)
>>> circle.radius = 40
>>> circle.dimensions
(80.0, 80.0)
>>> canvas.update()
```

Move the circle to the center of the canvas.

```python
>>> circle.position = (300, 300)
>>> canvas.update()
```

Draw a red square, with sides of length equal to the radius of the circle. 

```python
>>> from tkinter_shapes import Polygon
>>> r = circle.radius
>>> vertices = [(-r, -r), (+r, -r), (+r, +r), (-r, +r)]
>>> square = Polygon(canvas=canvas, vertices=vertices, outline='red')
>>> canvas.update()
```

The square is drawn at the origin, so it is only partially visible. Move the 
square to overlap with, and obscure part, the circle.

```python
>>> square.position = circle.position
>>> canvas.update()
```

The square now matches the bounding box of the circle. Make the square 
transparent, to make the circle visible once again.

```python
>>> square['fill'] = ''
>>> canvas.update()
```

Remove a vertex from the square polygon to convert it to an isosceles triangle.

```python
>>> triangle = square
>>> triangle.vertices = square.vertices[1:]
>>> canvas.update()
```

Cleanup by deleting the shapes and destroying the GUI.

```python
>>> del circle
>>> triangle.delete()
>>> gui.destroy()
```

### Example doctests

The examples in this README are rendered in [doctest] format, and can be run 
via the following code:[^python_paths]

[^python_paths]: Provided that the package is installed, or the [Python path] 
                 is otherwise set appropriately.

```
import doctest
doctest.testfile('README.md', module_relative=False)

```

## License

Copyright 2022 [Neuromechatronics Lab][neuromechatronics], 
Carnegie Mellon University

Created by: a. whit. (nml@whit.contact)

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

<!---------------------------------------------------------------------
   References
---------------------------------------------------------------------->

[tkinter]: https://docs.python.org/3/library/tkinter.html

[Python path]: https://docs.python.org/3/tutorial/modules.html#the-module-search-path

[doctest]: https://docs.python.org/3/library/doctest.html

[setuptools]: https://setuptools.pypa.io/en/latest/userguide/quickstart.html#basic-use

[neuromechatronics]: https://www.meche.engineering.cmu.edu/faculty/neuromechatronics-lab.html


