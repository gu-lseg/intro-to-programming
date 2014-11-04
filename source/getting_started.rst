Getting Started
***************

Interactive Python
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


Running code in a File
======================

We have programmed using the Python interactive shell.

The other way to program uses files. 

We `call` the python program on a file containing python code.

Put the following code into a file:: 

    # A line beginning with '#' is a comment. Python ignores it.

    import turtle
    turtle.shape("turtle")
    turtle.forward(25)
    turtle.exitonclick()  # Why this? Test by commenting it out.

and save the file as `my_turtle_file`.

Now in the console call the python command with the filename as parameter::

    python my_turtle_file.py


This is the more usual way to run programs.


Learn your Errors!!
===================

Errors (and Exceptions) are a constant feature of programming.

They always tell you what when wrong. They don't always tell you
why things went wrong though, in those cases they act as a clues.

As programmers learn to read errors their intuitions develop and solutions come
quicker.

Tip:

    Google errors!

SyntaxError
===========

Learning any language involves making many 'grammatical' or syntax errors.

Here we define a function badly::

    >>> def print_hi:
      File "<stdin>", line 1
        def print_hi 
                       ^
    SyntaxError: invalid syntax
    >>>

Here the programmer has forgotten that function definitions must have
parentheses ().

::

    >>> def print_hi():
        print('hi')

No error this time. `print_hi` is properly defined.

