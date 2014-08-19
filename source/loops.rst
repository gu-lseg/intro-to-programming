Repetition
**********

Repeating oneself
=================

Humans have intuition, computers don't (yet?).
Humans get bored, computers don't.

Combined with abstraction, the ability to repeat vastly expands our programming
expressivity.

There are different kinds of loops but we will look at only one.

The For loop
============

Example of loop iterating through names::

    for name in "John", "Sam", "Jill":
        print("Hello " + name)

Here we iterate through a list of numbers::

    for i in range(10):
        print(i)


The `range(n)` function can be considered a shorthand for ``0, 1, 2, ..., n-1``. 
If you want to know more about it, you can use 
the help in the Python shell by typing ``help(range)``. 
(Use the `q` key to exit help.)


Exercise
========

Reduce the lines of code in shapes.py by replacing each repeated segment of
code with a loop.
