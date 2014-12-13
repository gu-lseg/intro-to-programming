Data Structures
***************

Data structures or collections contain other objects. 

They are meant to keep a collection of objects together.

We will look at two: `lists`, `dictionaries`.

It takes some time and practice knowing when to use each.

The functions that interest us are accessing and updating elements of the structures. Also typically collections almost always combine with iteration. Which means going through each of the
members of the collection and effecting some action.

We will leave a more indepth investigation of the various methods to the Koans. Also see the python tutorial: 

https://docs.python.org/2/tutorial/datastructures.html

As always first we explore how to create objects using literals and
constructors, then we examine some functions typical of each object.

Lists
=====

Lists are container objects. They contain ordered items.

creation:: 

    >>> pythons = ['John Cleese', 'Eric Idle', 'Michael Palin', 'Terry Gilliam']
    >>> list(['John Cleese', 'Eric Idle', 'Michael Palin', 'Terry Gilliam'])
    ['John Cleese', 'Eric Idle', 'Michael Palin', 'Terry Gilliam']
    >>> abc = list('abc')              # the list constructor can take a string
    >>> abc
    ['a', 'b', 'c']                    # the result is a list of its characters

introspection::
    
    >>> type(pythons)
    <class 'list'>
    >>> dir(pythons)
    [ ... many methods ... ]

special syntax methods:: 

    >>> abc = ['a', 'b', 'c']
    >>> abc[0]                        # extract elements
    'a'
    >>> abc[2] = 'd'                  # assignment
    >>> abc
    ['a', 'b', 'd']

.. tip::
    Lists are very useful. Only the most trivial programs don't use them.

IndexError
----------

Lists and tuples are zero indexed. The first element is at index 0.

If you ask for an element that doesn't exist you will get an IndexError::

    >>> [][0]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range

range
-----

The `range` function combined with the `list` constructor is a shortcut way to create a list with a specified number of increasing integers::

    >>> list(range(3))   # think: give me numbers up to 3
    [0, 1, 2]

It provides a handy way of doing things a certain number of times.

::

    >>> for i in range(2):
    ...    print('hi') 
    'hi'
    'hi'


Dictionaries
============

Dictionaries contain key value mappings.

They can be used to represent things as well. Here we use a dictinary to
represent a Person.

creation::

    >>> {'name': 'Brian', 'age': 23, 'sex': 'M'}              # literal
    >>> dict([('name', 'Brian'), ('age', 23), ('sex', 'M')])  # constructor
    >>> type(person)
    <class 'dict'>


Special syntax for extracting and updating an attribute::

    >>> person['name']
    'Brian'
    >>> person['name'] = 'Naomi'
    >>> person['name']
    'Name'

If you request a non-existent key you get a `KeyError`.

Nested
======

Data structures can include any type of object including other data structures.

Here is a list of dictionaries::

    >>> persons = [
            {'name': 'Naomi', 'age': 32, 'sex': 'F', 'status': 'Single'},
            {'name': 'Jane', 'age': 29, 'sex': 'F', 'status': 'Married'},
            {'name': 'Brian', 'age': 23, 'sex': 'M', 'status': 'Single'}
        ]

Nested data structures are extremely common.



for loops
=========

Use `for` to iterate over each item in a given list.

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
    Loops are flow control statements which work hand in hand with data structures. 


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


Exercises
=========

Koans
-----

::

    > python3 contemplate_koans.py about_lists
    > python3 contemplate_koans.py about_dictionaries


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
