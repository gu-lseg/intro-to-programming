Calling Functions
*****************

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

Geometry Exercises
==================

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
