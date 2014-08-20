Abstractions
************

With functions our programming expressivity has just taken a leap.

Computers need step by step instructions. Humans however operate at higher
levels of abstraction.

Functions are one way to introduce abstractions. They let you name code for
future execution.

They enable us to no longer think of details.


Case study: From shapes to houses
=================================

You can use the already defined shapes as building blocks for even higher abstractions.

Consider the following.

::

    def house():
        square(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        equilateral_triangle(100)
        turtle.right(90)             # return turtle to point of departure
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


By reusing the code which defined our concepts of a square and triangle we have
defined the concept of a house.

Try your own. Enjoy thinking at a higher level!

Be inspired
===========

This is where programming starts to become creative. You can define the
universe of things that is of interest to you.

Building on layers of details you can construct palaces.

Exercise
========

Think of everything you can make from Lego, Minecraft, Bricks...

These are phsical and familiar to us. Just think of what you can do with basic building blocks.

Programmers model many other domains. Think of an area where you are expert and
how you might code it.

What objects, functions and variables would need to be defined?
