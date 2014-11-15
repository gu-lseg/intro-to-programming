Loops
*****

Computers however never get bored humans do.

It gets tedious typing turtle function calls.

Here we learn new constructs to handle repetition.

The ability to repeat expands our programming expressivity.

.. tip::
    
    Loops are flow control statements which work hand in hand with data structures. 


for
===

Iterating through a list of string objects:: 

    for name in ["John", "Sam", "Jill"]:
        print("Hello " + name)

.. tip::
    Use for if you are iterating over all the items in a given sequence or collection.

while
=====

The `while` statement is followed by a condition. The condition defines when
the loop will terminate.


::
    
    >>> import random
    >>> warm = 20
    >>> temperature = random.randrange(5, 30)
    >>> while temperature <= warm:
    ...    print('cold')
    ...    temperature = random.randrange(5, 30)
    cold
    cold
    cold

.. tip::
    Use while if you don't know when your loop will terminate.

range
=====

The `range` function provides a way of doing things a certain number of times.

::

    >>> list(range(4))
    [0, 1, 2, 3]


Refactoring `square`
====================

We refactor `square` combining `range` with a for loop.

::

    def square(side):
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)


Thanks to loops, the code is shorter and more readable.

Moreover it communicates better the nature of drawing a square: 
one action repeated four times. 


Exercises
=========

Looping `turtles`
-----------------

TODO

Refactor `shapes.py`
--------------------

Refactor all the shapes in `shapes.py` and make good use of loops where you
can.

Hexagon
-------

Write code that draws this:

.. image:: /images/turtle-hexagon.png


Honeycomb
---------

Write code that draws this:

.. image:: /images/turtle-honeycomb.png


Any Shape
---------

Write code that draws this:

.. image:: /images/turtle-all-shapes.png

.. tip::

    The sum of the external angles of any shape is always 360 degrees.

Further resorces
----------------

http://opentechschool.github.io/python-beginners/en/conditional_loops.html

http://opentechschool.github.io/python-beginners/en/loops.html
