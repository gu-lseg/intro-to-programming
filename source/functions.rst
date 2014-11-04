Functions
*********

Action objects
==============

Functions are another type of object. 

Think of them as actions, verbs, or commands.

They have names::

    run

They are called (actioned) by using parentheses::

    run()

Sometimes we call and pass parameters (here a number)::

    run("quickly")

You could think of parameters as adverbs: 'run, quickly'

NB: 

    The name `run` hasn't yet been defined so python won't recognise the above if you
    type it. We are illustrating a point.

All turtle instructions are examples of calling functions attached to the turtle object.

`print` is another function::
    
    >>> print('hello')

`print` simply prints its parameter to the console.


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


Geometry Exercises
------------------

Tip:

    Programming is always applied to something. Its an activity that seeks to
    capture some aspect of reality that is useful to us. 

    As humans we think at a higher intuitive level. We think square, or move
    forward. 

    Computers need everything broken down into steps. Each step is a command.

    Programming as an activity is about breaking down our concepts into smaller defined steps.
    In effect we define our concepts in commands.

Here we will program some geometrical concepts.

Lets define some of our gemetrical concepts using step by step instructions.

Draw a Square
-------------

Draw a square as in the following picture:

.. image:: /images/turtle-square.png

Squares have right angles which are 90 degrees.


Draw a rectangle
----------------

Draw a rectangle.

.. image:: /images/turtle-rectangle.png


Bonus
-----

How about a triangle? In an equilateral triangle (a triangle with all
sides of equal length) each corner has an angle of 60 degrees.


Many squares
------------

Now, draw many squares. Each one tilted left of the previous. 
Experiment with the angles between the individual squares.

.. image:: /images/turtle-many-squares.png

The picture shows three 20 degree turns. You could try 30 and 40...

Task:

    Create a file called `shapes.py` and put all shape related code into it. We
    will be reusing this file.
