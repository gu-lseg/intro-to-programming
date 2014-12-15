Quick Start
***********

In this section we learn how to create an object of type Turtle. We then
interact with this object and discover what attributes and methods (behaviours)
it has.

We also look at two ways to execute python code. The interactive interpreter
and calling python on a file that contains code.


.. tip::

    Don't just read! Type everything and experiment.


Interactive coding
==================

One way to run python is by using the interactive interpreter.

One way to enter the python interpreter is through `cmd.exe`:

1. Press the two keys Windows + R together
2. Enter `cmd.exe` in the search prompt and enter.

A window will appear with a prompt:: 

    C:\Users\greg-lo>

Type `python3` to enter the interactive shell::

    C:\Users\greg-lo>python
    Python 3.4.2 (v3.4.2:8711a0951384, Sep 21 2014, 21:16:45) [MSC v.1600 32 b
    it (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.

    >>> print('Hi') 

Turtles
=======

Type::

    >>> from turtle import Turtle
    >>> tess = Turtle()

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

Now experiment drawing shapes.


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
  
    C:\Users\greg-lo>python my_turtle_file.py


.. tip::

    Make sure the file you created exists in the location where you execute this
    command. The location is given by the prompt.


.. tip::

    Just like all word document file names end with .doc, all files with python code should end with .py


Exercises
=========

Documentation
-------------

Visit the `turtle` online documentation. 

|turtle_docs|

.. |turtle_docs| raw:: html

    <a href="https://docs.python.org/3/library/turtle.html" target="_blank">https://docs.python.org/3/library/turtle.html</a>


Questions:

* What colors does a turtle's `color` method recognise?
* What shapes does a trutle's `shape` method recognise?

The `help` function provides documenation directly in the interactive shell::

    >>> help(tess.forward)

Try any previously used functions and get into habit of automatically doing this.

Find some new turtle object methods and experiment.

.. tip::

    As you experiment you will want to do know how to do new things. Get into
    the habit of exploring the documenation to see what you can do.


Shapes
------

Lets program some shapes. We do this by breaking down into step by step instructions principles of geometry.

Put all code inside a file named `shapes.py` to be executed using::
    
    python shapes.py


Shapes:

* Draw a square as in the following picture. 
  
.. tip:: Squares have right angles which are 90 degrees.

.. image:: /images/turtle-square.png



* Draw a rectangle.

.. image:: /images/turtle-rectangle.png


* Draw an equilateral triangle. 

.. tip:: An equilateral triangle has 3 sides of equal length and each corner has an angle of 60 degrees.

* Draw many squares. Each square should be tilted left of the previous. 

.. image:: /images/turtle-many-squares.png

Experiment with the angles between the individual squares. The picture shows three 20 degree turns. You could try 30 and 40...

* Draw a simple house.

.. tip:: Reuse the code you have already written.


Koans
-----

Using your intuition try to complete the about_asserts koans.

Visit the appendix on windows for getting started.

::

    C:\Users\greg-lo>python contemplate_koans.py about_asserts

.. tip::

    Try copying small lines of code into the python interpreter to experiment 
    interactively with the code. Do this whenever you are stuck.
