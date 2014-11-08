Flow Control
************

Computers don't have any intuition, that is why we have to give step by step instructions.

Combined with abstraction, the ability to repeat vastly expands our programming
expressivity.

We will examine in turn the important control statements that Python provides.


Repetition
==========

Computers however never get bored.

It gets tedious typing turtle function calls.

Here we learn new constructs to handle repetition.

For loop
========

The for loop programming construct provides us with a mean of expressing
repetition.

Looping through a sequence of string objects:: 

    for name in "John", "Sam", "Jill":
        print("Hello " + name)

Looping through a sequence of numbers::

    >>> for i in range(2):
    ...     print(i)
    ...
    0
    1

The `range(n)` function is shorthand for ``0, 1, 2, ..., n-1``. 

NB:

    Another word used more often than looping is iterating it means the same.

While loop
==========

if

Looping the Square
==================

We have defined a square function like this::

    def square(side):
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)

The repetition is tedious to type and heavy to read. Lets use a for loop to remove it::

    def square(side):
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)

The code is much shorter. It communicates better the nature of drawing a square: 
that is the same thing repeated four times. It is more readable.

Tip:

    Rewriting code to equivalent code is called refactoring.

Exercise
========

Refactor all the shapes in `shapes.py` and make good use of loops where you
can.


Variable length hexagons
------------------------

Write a function that allows you to draw hexagons of any size you want, each
time you call the function.


.. image:: /images/shapes.png

.. tip::

   The sum of the external angles of any shape is always 360 degrees!

.. rst-class:: solution


Building worlds with abstractions
=================================

Building on our previously defined concept of a house we now use repetition 
to define a row of houses.

:: 

    def row_of_houses(number, size):
        for i in range(number):
            house(size)
            turtle.forward(size)

Abstraction
===========

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


Solution
--------

::

    def hexagon(size):
        for _ in range(6):
            turtle.forward(size)
            turtle.left(60)


Solution
--------

::

    def draw_shape(sides, length):
        for _ in range(sides):
            turtle.forward(length)
            turtle.right(360 / sides)
