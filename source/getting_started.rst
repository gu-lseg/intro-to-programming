Quick Start
***********

Interactive coding
==================

One way to run python is by using the interactive interpreter.

Type python without anything following to enter the interactive shell::

    C:\Users\greg-lo>\Python34\python.exe
    Python 3.4.2rc1 (v3.4.2rc1:8711a0951384, Sep 21 2014, 21:16:45) [MSC v.1600 32 b
    it (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.

    >>> print('Hi') 

.. tip::

    Don't just read! Type everything and experiment.

Turtles
=======

The turtle will follow any instruction you give it.

Type::

    >>> from turtle import Turtle
    >>> tess = Turtle()               # create a turtle object called tess

.. image:: /images/turtle-init.png

::

    >>> tess.forward(100)

.. image:: /images/turtle-forward.png

::

    >>> tess.left(30)

.. image:: /images/turtle-left.png

Type these in::

    >>> tess.shape('turtle')
    >>> tess.color('green')
    
    >>> bob = Turtle()
    >>> bob.shape('circle')
    >>> bob.color('red')
    >>> bob.backward(100)

Now have fun and experiment drawing shapes.


File coding
===========

Code is most often executed from file.

Using SublimeText create a file named `my_turtle_file.py` with this code:: 

    from turtle import Turtle, exitonclick

    tess = Turtle()
    tess.shape("turtle")
    tess.forward(100)

    exitonclick()  # Why this? Experiment by commenting it out.

In cmd.exe call the python command with the filename `my_turtle_file.py` as parameter::
  
    C:\Users\greg-lo>\Python34\python.exe my_turtle_file.py


.. tip::

    Make sure the file you created exists in the location where you execute this
    command.

    The location is given by the prompt.



Exercises
=========

Documentation
-------------

Visit the `turtle` online documentation. 

https://docs.python.org/3/library/turtle.html

Questions:

* What colors does a turtle's `color` method recognise?
* What shapes does a trutle's `shape` method recognise?

The `help` function provides documenation directly in the interactive shell::

    >>> help(turtle.forward)

Try any previously used functions and get into habit of automatically doing this.

Find some new turtle object methods and experiment.

Shapes
------

Here we will program some shapes.

Lets define some of our gemetrical concepts by breaking them down into using step by step instructions.

Put code inside a file named `shapes.py` to be executed using::
    
    python3 shapes.py


Draw a square as in the following picture:

.. image:: /images/turtle-square.png

Squares have right angles which are 90 degrees.


Draw a rectangle.

.. image:: /images/turtle-rectangle.png


Draw an equilateral triangle.
An equilateral triangle has 3 sides of equal length and each corner has an angle of 60 degrees.

Now, draw many squares. Each one tilted left of the previous. 
Experiment with the angles between the individual squares.

.. image:: /images/turtle-many-squares.png

The picture shows three 20 degree turns. You could try 30 and 40...

Combining previous code, draw a simple house.


Koans
-----

Using your intuition alone try to complete the about_asserts koans.

::

    C:\Users\greg-lo>\Python34\python.exe contemplate_koans.py about_asserts
