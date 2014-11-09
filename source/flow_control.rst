Flow Control
************

Computers don't have any intuition, that is why we have to give step by step instructions.

Combined with abstraction, the ability to repeat vastly expands our programming
expressivity.

We will examine in turn the important control statements that Python provides.


Go to these links and follow the tutorials there. Then come back here and
complete this page.

http://opentechschool.github.io/python-beginners/en/conditionals.html

http://opentechschool.github.io/python-beginners/en/conditional_loops.html

http://opentechschool.github.io/python-beginners/en/loops.html


Boolean Operators
=================

These expression evaluate to `True` or `False` according to the values of x and
y.

::

    x == y           # x equal to y
    x != y           # x not equal to y
    x > y            # x greater than y
    x < y            # x less than y
    x >= y           # x greater than or equal to y
    x <= y           # x less than or equal to y


User input
==========

To capture input from the user we use a function named `input`::

    >>> name = input("Please enter your name: ")
    Please enter your name: 

The interpreter waits for a response.

If the user types in `Sophocles` a string obejct 'Sophocles' is assinged to
name.

if statement
============

We use boolean expressions to make decisions.

:: 

    >>> x = int(input("Please enter an integer: "))
    Please enter an integer: 42
    >>> if x < 0:
    ...     x = 0
    ...     print('Negative changed to zero')
    ... elif x == 0:
    ...     print('Zero')
    ... elif x == 1:
    ...     print('Single')
    ... else:
    ...     print('More')

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


Koans - Control Statements
--------------------------

Truth and Falsehood::

    > python3 contemplate_koans.py about_true_and_false

Boolean operators

::

    > python3 contemplate_koans.py about_control_statements


Paper Sissors Rock
------------------

As a challenge code the paper sissors rock game.

You will need to use some randomness. This is how::
    
    >>> import random
    >>> random.randint(0, 2)
