Repetition
**********

Humans have intuition, computers don't (yet?).
Humans get bored, computers don't.

Combined with abstraction, the ability to repeat vastly expands our programming
expressivity.

Repeating oneself
=================

You have probably had enough of typing all those turtle function calls.

Here we learn how to tame repetition.

The For loop
============

Example of loop iterating through names::

    for name in "John", "Sam", "Jill":
        print("Hello " + name)

Here we iterate through a list of numbers::

    for i in range(10):
        print(i)


The `range(n)` function is shorthand for ``0, 1, 2, ..., n-1``. 


Exercise
========

Reduce the lines of code in shapes.py by replacing each repeated segment of
code with a loop.
