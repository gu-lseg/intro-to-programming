Defining Functions
******************

Abstractions
============

Computers need step by step instructions. Humans however operate at higher
levels of abstraction.

Functions are one way to introduce abstractions. They let you name code for
future execution.

They enable us to no longer think of details.

Defining Functions
==================

The ``def`` keyword followed by a name and then a colon identifies a function
definition::

    def going_nowhere():
        turtle.forward(50)
        turlle.backward(50)

The body of a function is the following block of code.

A block is defined by a colon, and one or more indented lines.

The indents are 4 spaces. The block ends on the first non indented line.
        
(Take care to use spaces and not tabs for indenting)

With Parameters
===============

Defining a function with parameters is similar::

    def line(length):
        turtle.forward(length)


Exercises
=========

Shapes
------

Reopen ``shapes.py`` and make a function for every shape.


Shapes with Paramaters
----------------------

Reopen ``shapes.py`` and make new functions with sensible parameters.


From shapes to houses: Higher Abstractions
==========================================

You can use the already defined shapes as building blocks for even higher abstractions.

Using the ipython interactive shell copy and paste these lines of code in and
execute them.

::

    def house():
        square(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        equilateral_triangle(100)


::

    def house():
        square(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        equilateral_triangle(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.left(90)

:: 

    def row_of_houses():
        house()
        turtle.forward(100)
        house()
        turtle.forward(100)
        house()
        turtle.forward(100)


Try your own. Enjoy thinking at a higher level!

Think of what you can do with basic parts.
Lego? Minecraft? Bricks?
