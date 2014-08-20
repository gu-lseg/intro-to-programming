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

