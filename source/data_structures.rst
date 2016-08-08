Data Structures
***************

Data structures are objects that contain or organise other objects in a useful
way. We will look at two datastructures in this lesson: lists and dictionaries
("dicts").

We will learn how to create these data structures, and how to access and
update their contents. We'll also look at how to do something with every item
in a data structure. To do this we use loops.

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

``list`` takes another object which can be represented as a list and returns that
list. In this case it takes the string "abc" and turns it into a list of its
letters.

``range`` creates a list of numbers from zero up to some number.


Accessing items
---------------

You can access a specific item in a list like so::

    >>> abc = ['a', 'b', 'c']
    >>> abc[0]
    'a'
    >>> abc[2]
    'c'

.. tip::

   The first item in a list is at position zero, *not* position one.

Updating lists
--------------

<<<<<<< HEAD
You update lists in a similar way::
    
    >>> abc[2] = 'd'
    >>> abc
    ['a', 'b', 'd']
=======
The `range` function combined with the `list` constructor is a quick way of creating a list
with a specified number of increasing integers.
>>>>>>> master

.. tip::

   You can only access and update positions in the list which are already
   occupied. For example try doing ``abc[25] = 'z'``; the computer will say:

   ``IndexError: list assignment index out of range``


Dictionaries
============

A dictionary or "dict", is another type of data structure which contains other
objects. But unlike in a list the order of the objects is not important and we
don't access or update an item using its index.

Instead, each object has a name. These names are called "keys" and the objects
are called "values"; a dictionary contains "key-value pairs". If we have a
key we can get access to the corresponding value.

Dictionaries are often used to contain information about a specific thing, in
the examples below we use a dictionary to contain information a person.

Creating dicts
--------------

When creating a dict we use curly brackets. These enclose a series of
pairs of keys and values like ``key: value`` separated by commas.

    >>> brian = {'name': 'Brian', 'age': 23, 'sex': 'M'}
    >>> brian
    {'age': 23, 'name': 'Brian', 'sex': 'M'}
    >>> type(brian)

.. tip::

   When ``brian`` is printed to the terminal, the keys and values aren't
   necessarily shown in the order they were defined in. Dictionaries don't
   care about the order of their contents like lists do.
    
Accessing values in a dict
--------------------------

You access a value in a dictionary in a similar way to how you access an item in
a list::

    >>> brian['name']
    'Brian'
    >>> brian['age']
    23

Updating a dict
---------------

The way you update a dict is similar to how you update a list too.

    >>> brian['age'] = 24
    >>> brian
    {'age': 24, 'name': 'Brian', 'sex': 'M'}

.. tip::

   If you access or update a non-existent key the computer will say there is a
   ``KeyError``.


Nesting
=======

Data structures can include any type of object including other data structures.

Here is a list of dictionaries:

.. code-block:: python

    >>> people = [
            {'name': 'Naomi', 'age': 32, 'sex': 'F', 'status': 'Single'},
            {'name': 'Jane', 'age': 29, 'sex': 'F', 'status': 'Married'},
            {'name': 'Brian', 'age': 23, 'sex': 'M', 'status': 'Single'}
        ]

Nested data structures are extremely common.

Think how this could be used to store information about all of the students
in a class.


The `for` loop
==============

Often, when we have a list of objects, we want to go through them one by one
and do something with each of them.

Use ``for`` to iterate over each item in a given list.

.. code-block:: python

    from turtle import Turtle, exitonclick

    alex = Turtle()

    for a_colour in ["yellow", "red", "purple", "blue"]:
       alex.color(a_colour)
       alex.forward(50)
       alex.left(90)

    exitonclick()

Here by iterating through a list of `str` objects we change the colour of our
turtle alex.


Refactoring `square`
--------------------

We can refactor `square` by combining `range` with a `for` loop.

.. code-block:: python

    def square(side):
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)

Drawing a square is reduced to repeating the same action four times.

Thanks to the `for` loop our definition of a square in code:

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


Practical: Paper Scissors Rock
-----------------------------

Steps:

1. The user inputs either 'paper', 'scissors' or 'rock'.
2. The computer randomly chooses one too.
3. The outcome is printed, according to the rules of the game:

   * If the user chooses 'paper' and the computer chooses 'rock', then print 'rock wins'
   * if the user chooses 'scissors' and the computer chooses 'paper' then print 'scissors wins'
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
