Getting Started
***************

Interactive coding
==================

One way to run python is by using the interactive shell.

Type ``python`` in the terminal.

Now type::

    >>> import turtle
    >>> turtle.shape("turtle")
    >>> turtle.forward(25)


Introducing Turtles
===================

The turtle will follow any instruction you give it.

Type::

    >>> import turtle

.. image:: /images/turtle-init.png


::

    >>> turtle.forward(25)

.. image:: /images/turtle-forward.png

::

    >>> turtle.left(30)

.. image:: /images/turtle-left.png


Experiment with the following instructions.


Movement:

``turtle.forward(<distance>)`` moves the turtle forward by the given distance. 

``turtle.backward(<distance>)``

``turtle.left(<angle>)`` rotates the turtle by number of degrees left.

``turtle.right(<angle>)``



Environment:

``turtle.reset()``  clears the drawing

``turtle.shape("turtle")`` change the shape into a turtle

``turtle.color("red")``


file coding 
===========

Interactive coding is great for exploration. But code is most often executed from file.

Create a file `my_turtle_file.py` with this code:: 

    # A line beginning with '#' is a comment. Python ignores it.

    import turtle
    turtle.shape("turtle")
    turtle.forward(25)
    turtle.exitonclick()  # Why this? Test by commenting it out.

In the console we call the python command with the filename as parameter::

    python my_turtle_file.py



Errors
======

Errors and Exceptions are a constant feature of programming.

They always tell you what when wrong. They don't always tell you
why things went wrong though but in those cases they act as clues.

Learn to read errors first using intuition then by debugging and researchig. It
is a skill and it does get easier. Soon you will map errors to solutions very
quickly.

Tip:

    Google errors!

SyntaxError
===========

Learning a language involves making many syntax (grammatical) errors.

A function defined badly::

    >>> def print_hi:
      File "<stdin>", line 1
        def print_hi 
                       ^
    SyntaxError: invalid syntax
    >>>

The programmer has forgotten that function definitions must have
parentheses `()` between the function name and the ending colon `:`.

::

    >>> def print_hi():
        print('hi')

No error this time. `print_hi` is properly defined.


Exercises
=========

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

Put all the code inside a file named `shapes.py` and execute it::
    
    python3 shapes.py


Square
------

Draw a square as in the following picture:

.. image:: /images/turtle-square.png

Squares have right angles which are 90 degrees.


Rectangle
---------

Draw a rectangle.

.. image:: /images/turtle-rectangle.png


Equilateral Triangle
--------------------

An equilateral triangle has 3 sides of equal length and each corner has an angle of 60 degrees.

Many squares
------------

Now, draw many squares. Each one tilted left of the previous. 
Experiment with the angles between the individual squares.

.. image:: /images/turtle-many-squares.png

The picture shows three 20 degree turns. You could try 30 and 40...

House
-----

Combining previous code, draw a simple house.
