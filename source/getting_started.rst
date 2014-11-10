Getting Started
***************

Interactive shell
=================

One way to run python is by using the interactive shell.

Type python without anything following to enter the interactive shell::

    C:\Users\greg-lo>\Python34\python.exe
    Python 3.4.2rc1 (v3.4.2rc1:8711a0951384, Sep 21 2014, 21:16:45) [MSC v.1600 32 b
    it (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.

    >>> import turtle
    >>> turtle.shape("turtle")
    >>> turtle.forward(25)

.. tip::

    Where you see `>>>` in the text you can assume the interactive shell is
    bieng used. Don't just read, expriment yourself!

Turtles
=======

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

Documentations
--------------

Look through the documentation and experiment with lines of code you find there.

https://docs.python.org/3/library/turtle.html


Using files
===========

Code is most often executed from file.

Using SublimeText create a file `my_turtle_file.py` with this code:: 

    # A line beginning with '#' is a comment. Python ignores it.

    import turtle
    turtle.shape("turtle")
    turtle.forward(25)
    turtle.exitonclick()  # Why this? Test by commenting it out.

In the console we call the python command with the filename as parameter::
  
    C:\Users\greg-lo>\Python34\python.exe my_turtle_file.py


.. tip::

    Make sure the file you created exists in the location where you execute this
    command.

    Here the location is given by the prompt.



Exercises
=========


Geometry Exercises
------------------

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


Koans
-----

Using your intuition alone try to complete the about_asserts koans.

::

    C:\Users\greg-lo>\Python34\python.exe contemplate_koans.py about_asserts
