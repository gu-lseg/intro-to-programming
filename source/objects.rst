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

How do we discover what methods do string objects have? 

Documentation is available in the interpreter::

    >>> help(str)

See also online documentation: |string_docs|

.. |string_docs| raw:: html

    <a href="https://docs.python.org/3.4/library/string.html" target="_blank">https://docs.python.org/3.4/library/string.html</a>

Questions
---------

Using `help`, or online documentation and using a string (eg 'abcabc') find methods that:

* confirms whether the string is alphabetical
* confirms wether the string is alphnumerical
* confirms whether the string is lowercase
* returns `Abc`
* returns `ABC`
* counts the number of 'a's

Consult the online documentation: |string_methods|

.. |string_methods| raw:: html

    <a href="https://docs.python.org/3.4/library/stdtypes.html#string-methods" target="_blank">https://docs.python.org/3.4/library/stdtypes.html#string-methods</a>

Koans
-----

Run these to explore `str` objects:: 

    python contemplate_koans.py about_strings
    python contemplate_koans.py about_strings_manipulation


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

Arithmetic Operators
--------------------

Two objects of type `int`, separated by an arithmetic operators `*` `/` `-` `+`, have the
same behaviour we expect from basic arithmentic.

::

    >>> 5 + 4
    9
    >>> 5 - 6
    -1

This special syntax exists to make working with `int` objects intuitive.


Comparison Operators
--------------------

Likewise two objects of type `int`, separated by an comparison operators `==`
`>=` `<=` `<` `>`, have the same behaviour we expect. 

These are expressions and these evaluate to `True` or `False`.

::

    >>> 5 == 4
    False
    >>> 5 < 6
    True
    >>> 6 <= 6
    True

Again the special syntax exists to fit our existing expectations.

Koans
-----

Run these to explore `int` objects:: 

    python contemplate_koans.py about_integers


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
