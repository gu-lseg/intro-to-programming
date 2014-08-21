Repetition
**********

Computers don't have any intuition, that is why we have to give step by step instructions.

Computers however never get bored.

Combined with abstraction, the ability to repeat vastly expands our programming
expressivity.

Repeating oneself
=================

You have probably had enough of typing all those turtle function calls.

Here we learn how to tame repetition.

The For loop
============

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
