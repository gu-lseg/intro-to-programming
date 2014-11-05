Functions
*********

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


Simple Functions
================

The ``def`` keyword is followed by the function object name, followed by () and then a colon. 

example::

    def going_nowhere():
        turtle.forward(50)
        turlle.backward(50)

The body of a function is the following block of code.

A block is defined by a colon, and one or more indented lines.

The indents are 4 spaces. The block ends on the first non indented line.
        
(Take care to use spaces and not tabs for indenting)


Parameters
==========

We have already seen calling functions with parameters.

This is how to define a function that takes parameters:: 

    def line(length):
        turtle.forward(length)

Tip:

    People also call parameters arguments.


As we shrink down our code and add functions to remove duplication, we
are *factorizing* it. This is a good thing to do. But the functions we
have defined so far are not very flexible. The variables are defined
inside the function, so if we want to use a different angle or a
distance then we need to write a new function. Our hexagon function can 
only draw one size of hexagon!

That is why we need to be able to give parameters, also called
*arguments*, to the function.  This way the *variables* in the
function can have different values each time we call the function:

Remember how we defined the function ``line_without_moving()`` in the previous
section::

    def line_without_moving():
        turtle.forward(50)
        turtle.backward(50)

We can improve it by giving it a parameter::

    def line_without_moving(length):
        turtle.forward(length)
        turtle.backward(length)

The parameter acts as a *variable* only known inside the function's definition.
We use the newly defined function by calling it with the value we want the
parameter to have like this::

    line_without_moving(50)
    line_without_moving(40)

We have been using functions with parameters since the beginning of the
tutorial with ``turtle.forward()``, ``turtle.left()``, etc... 

And we can put as many arguments (or parameters) as we want, separating them
with commas and giving them different names::

    def tilted_line_without_moving(length, angle):
        turtle.left(angle)
        turtle.forward(length)
        turtle.backward(length)


IndentationError
================

Indentation is the number of spaces a piece of code is from the left hand side of
the page.

It is important in python. It defines blocks of code. A block of code is code
that goes together.

It is not unusual to get this kind of error::

    >>> def awef():
    ... print('hi')
      File "<stdin>", line 2
        print('hi')
            ^
    IndentationError: expected an indented block

It simply means we have gotten the indentation wrong. Here the programmer has
forgotten to add 4 spaces on the new line after the colon.


Building worlds with abstractions
=================================

Building on our previously defined concept of a house we now use repetition 
to define a row of houses.

:: 

    def row_of_houses(number, size):
        for i in range(number):
            house(size)
            turtle.forward(size)

Abstraction
===========

Defining reusable components and the ability to repeat them is imensely powerful.

Think of everything you can make from Lego bricks. Minecraft is a world build
with cubes. In the real world think of all the components and repetition you
typically find in a skyscraper.

This is where programming starts to become creative. You can define the
universe of things that is of interest to you.

Building on layers of details you can construct palaces.

These are phsical and familiar to us. Just think of what you can do with basic building blocks.

Programmers model many other domains. Think of an area where you are expert and
how you might code it.

What objects, functions and variables would need to be defined?


Exercises
=========

Shapes
------

Reopen ``shapes.py`` and define every shape as function.

Does this make the code more modular, readable, reusable?


Shapes with Paramaters
----------------------

Reopen ``shapes.py`` and make new functions with sensible parameters.

Does this make the code more general and reusable?


Variable length hexagons
------------------------

Write a function that allows you to draw hexagons of any size you want, each
time you call the function.


.. image:: /images/shapes.png

.. tip::

   The sum of the external angles of any shape is always 360 degrees!

.. rst-class:: solution

Solution
--------

::

    def hexagon(size):
        for _ in range(6):
            turtle.forward(size)
            turtle.left(60)


Solution
--------

::

    def draw_shape(sides, length):
        for _ in range(sides):
            turtle.forward(length)
            turtle.right(360 / sides)



