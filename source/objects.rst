Objects
*******

Object Oriented programming is about defining and manipulating objects to do something
meaningful to the programmer.

An Object:

* Exists as a pattern of 0s and 1s in the computer's memory. 
* Conceptually represents something of meaning to the programmer.

The function `id` returns the location in memory of a passed object::

    >>> id(tess)
    4428974960

So our digital tess lives at the above address in our computer memory chip.

.. tip::

    In practice we don't typically need to know what location our objects are at.

An object is always an instance of a Type and the Type determines an objects':

* attributes
* methods (behaviours)

Here we revisit turtles and introduce two new types of objects. We focus on creation and manipulation.

By the end of this section we will have examined 3 types of objects:

* Turtles - represent and manipulate graphics.
* Strings - represent and manipulate text. 
* Integers - represent and manipulate whole numbers.


Turtles
=======

Turtle objects represent pens that enable us to draw pictures.

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
    We call an object by adding parenthesis at the end of its name. Here the
    parenthesis are empty but then often aren't.

Lets confirm the type of tess::

    >>> type(tess)
    turtle.Turtle

.. tip:: 
    The function `type` returns the type of a passed object.

Turtle is a special kind of object in that it produces new objects. We call it
a constructor object.

Methods
-------

We have already explored the various methods (behaviours) that exist on turtle
objects.


Strings 
=======

Objects that are instances of type `str` represent text.

Creation
--------
::

    >>> str('hi')      # constructor
    'hi'
    >>> "hi"           # literal
    hi
    >>> type('hi')     # confirm type
    str

When you execute the code `"hi"` or `str("hi")`, the python interpreter:

1. Creates an object of type `str`
2. Gives it the value "hi"
3. Returns this newly created object

Creating strings is very common, so the python language gives us a shortcut
notation to create them. A literal literraly represents an
object and one is created and returned immediately. This is in contrast to
constructor objects such as `str` or `Turtle`.

Methods
-------

It is natural to expect methods that exist on string objects facilitate working with text.

So what methods do string objects have?

`str` functions::

    >>> help(str)

Visit the online documentation to get a good overview and discover new methods:

https://docs.python.org/3.4/library/string.html

We will revisit string methods in the Koans.

Integers
========

Objects that are instances of type `int` represent whole numbers.

Creation 
--------

::

    >>> int(3)         # constructor 
    3
    >>> 3              # literal
    3
    >>> type(5)        # confirm type
    int

You can use the constructor `int` to convert objects of type `str` into objects of
type `int`::

    >>> int('3')
    3

Methods
-------

Objects of type `int` methods map to arithmetic enabling us to use them to 
solve basic math problems.

::

    >>> help(5)        # display documentation

The arithmetic operations you'd expect are implemented on int objects::

    >>> 5 + 4
    9
    >>> 5 - 6
    -1

Special syntax exists which enable manipulating `int` objects in ways that map
directly to arithmetic. 

Two objects of type `int`, separated by an arithmetic operators `*` `/` `-` `+`, have the
exact behaviour we expect from basic arithmentic.

This is an example of a python programming feature that exists
to make working with `int` objects intuitive.


Exercises
=========

'5' Vs 5
--------

Describe in detail what the interpreter does when you type the following and
enter:: 

    >>> '5'

    >>> 5


Strings, Integers, and the + operator
-------------------------------------

Instances of both `str` and `int` objects recognise the `+` symbol.

What output would you expect of the following lines of code?

::

    '1' + '2'

    1 + 2

Use the interpreter to test your answer with python.

Try the same above but this time using `*` instead of `+`. What can you
conclude of the meaning of `*`?


`str` methods 
-------------

Using the `help`, or the online documentation and a string (eg 'abcabc') find methods that:

* confirms whether the string is alphabetical
* confirms wether the string is alphnumerical
* confirms whether the string is lower
* returns `Abc`
* returns `ABC`
* counts the number of 'a's

.. tip::

    https://docs.python.org/3.4/library/stdtypes.html#string-methods

Koans & `str`
-------------

In these Koans we will spend time exploring `str` objects.

:: 

    python contemplate_koans.py about_strings
    python contemplate_koans.py about_strings_manipulation
