Turtles
*******

Turtle objects know how to draw. Here we explore creating and
manipulating them to draw on the screen.

We also look at the two ways the `python` interpreter can execute your Python code:

* The interactive interpreter (typing directly into the terminal).
* Calling the python interpreter on a file that contains code.

.. tip::

    Don't just read! Type everything and experiment.


Interactive interpreter
=======================

We launch the python interpreter through `terminal`:

1. Press `Cmd(apple) + Spacebar` (the two keys together). A search box pops up.
2. Type `terminal` and press enter.

A window will appear with a prompt::

    ~

Type `python` to enter the interactive shell::

    ~ >python
    ...
    >>>


The interpreter is awaiting your commands. Now type each of the lines, pressing enter after each line::

    >>> from turtle import Turtle
    >>> tess = Turtle()

A window will pop up called `Python Turtle Graphics` containing tess the turtle.

.. image:: /images/turtle-init.png

Try typing some different commands - forward and left are methods on our tess turtle object

Forward takes pixels as it's input - this will move tess forward 100 pixels::

    >>> tess.forward(100)

.. image:: /images/turtle-forward.png

The left and right methods take degrees as their input - this will turn tess left 30 degrees::

    >>> tess.left(30)

.. image:: /images/turtle-left.png

Lets call some more methods on the tess our turtle object

Shape and colour take strings as their inputs::

    >>> tess.shape('turtle')
    >>> tess.color('green')

Lets create 'bob' - a new turtle object::

    >>> bob = Turtle()
    >>> bob.shape('circle')
    >>> bob.color('red')
    >>> bob.backward(100)

Clear your canvas and move both turtles back to the middle

    >>> bob.reset()
    >>> tess.reset()

Exercise
--------

Experiment drawing shapes in different colours.

1. Can you make bob a triangle so you can see which way he is pointing?
2. Can you draw a triangle?
3. What shapes can you draw using both turtles in different colours?

Documentation
-------------

Visit the `turtle` online documentation and explore what Turtle objects can do.

|turtle_docs|

.. |turtle_docs| raw:: html

    <a href="https://docs.python.org/3/library/turtle.html" target="_blank">https://docs.python.org/3/library/turtle.html</a>


Questions:

* What different colors does a turtle's `color` method recognise?
* What shapes does a trutle's `shape` method recognise?

Find some new turtle object methods and experiment.

.. tip::

    As you experiment you will want to do know how to do new things. Get into
    the habit of exploring the documenation to see what you can do.


Turtles
=======

Lets revise what we have learnt in the light of object oriented terminology.

An object can be created. It has a type, and this type determines its methods
(behaviours).

Creation
--------

::

    >>> from turtle import Turtle
    >>> tess = Turtle()

Breakdown:

1. We import an object called Turtle from somewhere called turtle.
2. Turtle is called, creates a new object of type turtle, and returns it.
3. This returned object is assigned to the name tess.

.. tip::
    We call an object by adding parenthesis (brackets) at the end of its name. Here the
    parenthesis are empty but they often aren't.

Run this command to find the object type of tess::

    >>> type(tess)

What type of object is tess?

.. tip::
    The function `type` returns the type of the object passed in.

Turtle is a special kind of object in that it produces new objects. We call it
a constructor object.

Methods
-------

Methods are functions attached to objects. We will explore functions later.

::

    >>> tess.forward(100)

Braces `()` have a special meaning. They indicate calling. You can think of
this as effecting an action.

The effect of calling the method `forward` on an object of type `Turtle` is to
draw a line.

What other methods (behaviours) do turtle objects have?

Code in files
=============

Most code is written and executed from a file.

Use SublimeText to create a file named `my_turtle_file.py` in the documents folder with this code::

    from turtle import Turtle, exitonclick

    tess = Turtle()
    tess.shape("turtle")
    tess.forward(100)

    exitonclick()

.. tip::

    All file names with python code must end with .py

    We can comment out lines of code using #

Open a terminal and make sure you are in the documents directory (:ref:`See Terminal 101 <terminal-101>`). If you still have the Python interpreter open in your terminal you can exit using ``cmd + d``.

In the terminal call the python interpreter command with the filename `my_turtle_file.py` as parameter::

    python my_turtle_file.py


.. tip::

    Make sure the file you created exists in the location where you execute this
    command. The location is given by the prompt.
    You can use the 'Change Directory' command `cd` to get to the right directory
    E.g: `cd /folder` will move the current directory to 'folder'

Questions/Practicals
--------------------

1. What happens if you delete or comment out ``exitonclick()`` in your script and re-run it? Explain why you think this happens - discuss with your team and mentor.

2. What are the differences between using `python` interactively and using files? When would you use one or the other?

3. Challenge yourself to find as many different ways of drawing with a turtle object.

4. Take your time to draw something useful and/or crazy.



Shape Exercises
===============

Lets program some shapes. We do this by breaking down the principles of geometry into step by step instructions.

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

* Really want a challenge? Draw the 'flower' shape below:

.. image:: /images/spirograph.png
