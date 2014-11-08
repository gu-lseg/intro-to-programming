Flow Control
************

Computers don't have any intuition, that is why we have to give step by step instructions.

Combined with abstraction, the ability to repeat vastly expands our programming
expressivity.

We will examine in turn the important control statements that Python provides.

Boolean Operators
=================

Loops
=====

Computers however never get bored.

It gets tedious typing turtle function calls.

Here we learn new constructs to handle repetition.

For loop
--------

We haven't seen list objects yet but your intuition should be enough for now.

Looping through a list of string objects:: 

    for name in ["John", "Sam", "Jill"]:
        print("Hello " + name)

Looping through a sequence of numbers::
`range` is a function object that takes an object of type `int` as parameter
and returns an object that when combined with `list` gives a list of `int`
objects with values 0 to n-1.

    >>> list(range(3))
    [0, 1, 2]

Lets combine it in a for loop::

    >>> for i in range(2):
    ...     print(i)
    ...
    0
    1

.. tip::

    looping and iterating means the same.

While loop
----------

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

.. tip::

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


