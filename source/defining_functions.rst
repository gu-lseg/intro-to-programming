Defining Functions
******************


Simple Functions
================

The ``def`` keyword is followed by the function object name, followed by () and then a colon. 

example::

    def going_nowhere():
        turtle.forward(50)
        turlle.backward(50)

The body of a function is the following block of code.

A block is defined by a colon, and one or more indented lines.

The indents are 4 spaces. The block ends on the first non indented line.
        
(Take care to use spaces and not tabs for indenting)

SyntaxError
===========

It is normal to take some time getting used to the syntax of any language.

In python people always struggle a bit when they first define functions::

    >>> def my_function:
      File "<stdin>", line 1
        def my_function:
                       ^
    SyntaxError: invalid syntax
    >>>

Be precise.

Functions with Parameters
=========================

We have already seen calling functions with parameters.

This is how to define a function that takes parameters:: 

    def line(length):
        turtle.forward(length)

Tip:

    People also call parameters arguments.

Exercises
=========

Shapes
------

Reopen ``shapes.py`` and define every shape as function.

Does this make the code more modular, readable, reusable?

Shapes with Paramaters
----------------------

Reopen ``shapes.py`` and make new functions with sensible parameters.

Does this make the code more general and reusable?
