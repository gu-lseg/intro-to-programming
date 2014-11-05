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
