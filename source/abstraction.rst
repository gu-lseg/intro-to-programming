Abstraction
***********

Defining reusable components and the ability to repeat them is imensely powerful.

Think of everything you can make from Lego bricks. Minecraft is a world build
with cubes. In the real world think of all the components and repetition you
typically find in a skyscraper.

This is where programming starts to become creative. You can define the
universe of things that is of interest to you.

Building on layers of details you can construct palaces.

These are phsical and familiar to us. Just think of what you can do with basic building blocks.

Programmers model many other domains. Think of an area where you are expert and
how you might code it.

What objects, functions and variables would need to be defined?

Building abstractions
=====================

Building on our previously defined concept of a house we now use repetition 
to define a row of houses.

:: 

    def row_of_houses(number, size):
        for i in range(number):
            house(size)
            turtle.forward(size)


Exercises
=========

hexagon
-------

::

    def hexagon(size):
        for _ in range(6):
            turtle.forward(size)
            turtle.left(60)


Shape
-----

::

    def draw_shape(sides, length):
        for _ in range(sides):
            turtle.forward(length)
            turtle.right(360 / sides)
