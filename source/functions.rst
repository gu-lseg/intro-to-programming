Functions - Verbs
*****************

Functions
=========

Functions are a type of object. 

Think of them as actions, verbs, or commands.

They have names::

    run

They are called (actioned) by using parentheses::

    run()

Sometimes we call and pass parameters (here a number)::

    run("quickly")

Think of parameters as adverbs: 'run, quickly'


Turtle functions
================

Here we introduce functions that turtles understand. 

Now type::

    import turtle

.. image:: /images/turtle-init.png


::

    turtle.forward(25)

.. image:: /images/turtle-forward.png

::

    turtle.left(30)

.. image:: /images/turtle-left.png


Movement:

``turtle.forward(<distance>)`` moves the turtle forward by the given distance. 

``turtle.left(<angle>)`` rotates the turtle by number of degrees left.

``turtle.backward(...)``

``turtle.right(...)``


Environment:

``turtle.reset()``  clears the drawing

``turtle.shape("turtle")`` change the shape into a turtle

``turtle.color("red")``

    

Geometry Exercises
==================

Programming is interesting when applied to something. Here we will
program some geometrical concepts we have.

As humans we think at a higher intuitive level. We think square, or move
forward. 

But computers need everything explained. 
Programming is about breaking down our concepts into smaller defined steps.
We are in effect defining our concepts.

Lets define some of our Gemetrical concepts.

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


