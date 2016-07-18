Data Structures
***************

Data structures are objects that contain or organise other objects in a useful
way. We will look at two datastructures in this lesson: lists and dictionaries.

We will learn how to create lists and dictionaries and examine how to access
their contents. Then we look at how to do something with every item in a data
structure. To do this we use loops.

Lists
=====

A list is a data structure which contains objects in a specific order.

Creating lists
--------------

To create a list from some other objects use square brackets like so::

    >>> monty_python = ['John', 'Terry G', 'Eric', 'Michael', 'Terry J', 'Graham']
    >>> monty_python
    ['John', 'Terry G', 'Eric', 'Michael', 'Terry J', 'Graham']
    >>> type(monty_python)
    <type 'list'>

You can also create lists using some built-in functions such as ``list`` and
``range``::

    >>> list('abc')
    ['a', 'b', 'c']
    >>> range(4)
    [0, 1, 2, 3]


Accessing items
---------------

You can access a specific item in a list like so::

    >>> abc = ['a', 'b', 'c']
    >>> abc[0]
    'a'
    >>> abc[2]
    'c'

.. tip::

   It's important to note that the first item in a list is at position zero, not
   position one.

Updating lists
--------------

You update lists in a similar way::
    
    >>> abc[2] = 'd'
    >>> abc
    ['a', 'b', 'd']

.. tip::

   You can only update positions in the list which are already occupied. If you
   try doing ``abc[25] = 'z'`` the computer will say:

   ``IndexError: list assignment index out of range``


Dictionaries
============

Dictionaries contain key value mappings.

They can be used to collect information (data) about something. 
Here we use a dictinary to represent a Person.

creation
--------

.. code-block:: python

    >>> {'name': 'Brian', 'age': 23, 'sex': 'M'}              # literal
    >>> dict([('name', 'Brian'), ('age', 23), ('sex', 'M')])  # constructor


extraction & update
-------------------

Special syntax: `<dict-name>[<key>]` for extracting and updating an attribute.

.. code-block:: python

    >>> person = {'name': 'Brian', 'age': 23, 'sex': 'M'}
    >>> person['name']                          # extract value
    'Brian'
    >>> person['name'] = 'Naomi'                # update value
    >>> person['name']
    'Name'

If you request a non-existent key you get a `KeyError`.


Nesting 
=======

Data structures can include any type of object including other data structures.

Here is a list of dictionaries:

.. code-block:: python

    >>> persons = [
            {'name': 'Naomi', 'age': 32, 'sex': 'F', 'status': 'Single'},
            {'name': 'Jane', 'age': 29, 'sex': 'F', 'status': 'Married'},
            {'name': 'Brian', 'age': 23, 'sex': 'M', 'status': 'Single'}
        ]

Nested data structures are extremely common.

Think how this could be useful for example to store information about all
students in a class.


The `for` loop
==============

Use `for` to iterate over each item in a given list.

Here by iterate through a list of `str` objects we change the colour of our
turtle alex.

.. code-block:: python

    from turtle import Turtle, exitonclick

    alex = Turtle()

    for a_colour in ["yellow", "red", "purple", "blue"]:
       alex.color(a_colour)
       alex.forward(50)
       alex.left(90)

    exitonclick()


Refactoring `square`
--------------------

We refactor `square` combining `range` with a for loop.

.. code-block:: python

    def square(side):
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)

Drawing a square is reduced to repeating the same action four times. 

Thanks to the for loop our definition of a square in code:

* is shorter and more readable.
* communicates an insight into the geometry of a square.


Exercises
=========


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

Write code that can draw any shape like this:

.. image:: /images/turtle-all-shapes.png

.. tip::

    The sum of the external angles of any shape is always 360 degrees.


Practical: Paper Sissors Rock
-----------------------------

Steps:

1. user inputs either paper, sissors or rock.
2. computer randomly chooses one too.
3. print outcome according to the rules of the game:

   * If user chose 'paper' and computer chose 'rock', then print 'rock wins'
   * if user chose 'sissors' and computer chose 'paper' then print 'sissors
     wins'
   * ... and so on ...
4. Exit

You will need to use some randomness:
    
.. code-block:: python

    >>> import random
    >>> random.choice(['a', 'b', 'c'])

Looping `turtles`
-----------------

Using the following as template draw this:

.. image:: /images/turtle-queue.png

Put the following in a file called `turtle_queue.py` and finish off the
program.

.. code-block:: python

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

