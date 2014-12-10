Flow 2: Loops
*************

Here we learn new constructs to handle repetition.

The ability to repeat expands our programming expressivity.

.. tip::
    Loops are flow control statements which work hand in hand with data structures. 


for
===

Here by iterate through a list of `str` objects we change the colour of our
turtle alex.

::

    from turtle import Turtle, exitonclick   

    alex = Turtle()

    for a_colour in ["yellow", "red", "purple", "blue"]:
       alex.color(a_colour)
       alex.forward(50)
       alex.left(90)

    exitonclick()


.. tip::
    Use `for` to iterate over each item in a given list.

range
-----

The `range` function with for provides a handy way of doing things a certain number of times.

::

    >>> for i in range(2):
    ...    print('hi') 
    'hi'
    'hi'


Refactoring `square`
--------------------

We refactor `square` combining `range` with a for loop.

::

    def square(side):
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)

Drawing a square is reduced to repeating the same action four times. 

Thanks to the for loop our definition of a square in code:
* is shorter and more readable.
* communicates an insight into the geometry of a square.

while
=====

The `while` keyword is always followed by a condition. The condition defines when
the loop will terminate.

::
    
    >>> import random
    >>> warm = 20
    >>> temperature = random.randrange(5, 30)
    >>> while temperature <= warm:
    ...    print('cold')
    ...    temperature = random.randrange(5, 30)
    cold
    cold
    cold

.. tip::
    Use while if you don't when you only know a loop will terminate in a given
    condition.


Exercises
=========

Looping `turtles`
-----------------

Using the following as template draw this:

.. image:: /images/turtle-queue.png

`turtle_queue.py`::

    import turtle

    number_of_turtles = 4

    turtles = []
    for _ in range(number_of_turtles):
        turtles.append(turtle.Turtle())

    # position point of origin at bottom left of window
    turtle.setworldcoordinates(0, 0, 600, 600)

    for i, turtle_ in enumerate(turtles):
        turtle_.up()

    # Evenly space out the turtles
    for i, turtle_ in enumerate(turtles):
        ypos = 600 / number_of_turtles * i
        turtle_.setpos(0, ypos)

    for i, turtle_ in enumerate(turtles):
        turtle_.down()

    ###################################
    # Your turn! Enter your code here #
    ###################################

Refactor `shapes.py`
--------------------

Refactor all the shapes in `shapes.py` and make good use of loops where you
can.

Hexagon
-------

Write code that draws this:

.. image:: /images/turtle-hexagon.png


Honeycomb
---------

Write code that draws this:

.. image:: /images/turtle-honeycomb.png


Any Shape
---------

Write code that draws this:

.. image:: /images/turtle-all-shapes.png

.. tip::

    The sum of the external angles of any shape is always 360 degrees.

Further resorces
----------------

http://opentechschool.github.io/python-beginners/en/conditional_loops.html

http://opentechschool.github.io/python-beginners/en/loops.html

http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/IterationSimplifiesourTurtleProgram.html
