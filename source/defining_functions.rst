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


Functions with Parameters
=========================

We have already seen calling functions with parameters.

This is how to define a function that takes parameters:: 

    def line(length):
        turtle.forward(length)

Tip:

    People also call parameters arguments.


IndentationError
================

Indentation is the number of spaces a piece of code is from the left hand side of
the page.

It is important in python. It defines blocks of code. A block of code is code
that goes together.

It is not unusual to get this kind of error::

    >>> def awef():
    ... print('hi')
      File "<stdin>", line 2
        print('hi')
            ^
    IndentationError: expected an indented block

It simply means we have gotten the indentation wrong. Here the programmer has
forgotten to add 4 spaces on the new line after the colon.


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
