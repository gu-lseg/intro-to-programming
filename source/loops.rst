Loops
*****

Computers however never get bored humans do.

It gets tedious typing turtle function calls.

Here we learn new constructs to handle repetition.

The ability to repeat expands our programming expressivity.

.. tip::
    
    Loops work hand in hand with data structures. Especially collections.

for
===

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

while
=====

Use while loop if you don't know when your loop will terminate.

Example::

    def sumTo(aBound):
        """ Return the sum of 1+2+3 ... n """

        theSum  = 0
        aNumber = 1
        while aNumber <= aBound:
            theSum = theSum + aNumber
            aNumber = aNumber + 1
        return theSum

    print(sumTo(4))
    print(sumTo(1000))


range
=====

Range provides a way of doing things a certain number of times.

::
    >>> list(range(4))
    [0, 1, 2, 3]


Conclusion
==========

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

Refactor `shapes.py`
--------------------

Refactor all the shapes in `shapes.py` and make good use of loops where you
can.

Hexagon
-------

Write code that draws this:

.. image:: /images/turtle-hexagon.png


Honecomb
--------

Write code that draws this:

.. image:: /images/turtle-honeycomb.png

Paper Sissors Rock
------------------

As a challenge code the paper sissors rock game.

You will need to use some randomness. This is how::
    
    >>> import random
    >>> random.randint(0, 2)


Resources
=========

http://opentechschool.github.io/python-beginners/en/conditional_loops.html

http://opentechschool.github.io/python-beginners/en/loops.html

