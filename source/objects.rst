Objects
*******

Object Oriented programming is about defining and manipulating objects to do something
meaningful to the programmer.

An Object:

* Exists as a pattern of 0s and 1s in the computer's memory. 
* Conceptually represents something of meaning to the programmer.

We have created and manipulated turtle objects. Turtle objects represent pens
that enable us to draw pictures.

Here we will focus on two more types of objects: 
* Strings represent and help manipulate text in our programs. 
* Integers represent and help manipulate whole numbers in our programs.

We will look at how to create and then manipulate these types of objects.

Types
=====

An object is always an instance of a Type. The Type determines an objects':

* attributes
* methods (behaviours)

The function `type` returns the type of a passed object:: 

    >>> type(5)
    int
    >>> type('5')
    str


Strings 
=======

Objects that are instances of type `str` represent text.

creation
--------
::

    >>> "hi"           # literal
    hi
    >>> type('hi')     # confirm type
    str

When you execute the code `"hi"` or `str("hi")`, the python interpreter:

1. Creates an object of type `str`
2. Gives it the value "hi"
3. Returns this newly created object

methods
-------

What methods do string objects have?

`str` functions::

    >>> help("string")

There are many. These facilitate working with text.
Take time to visit the online documentation to get an overview.

https://docs.python.org/3.4/library/string.html

Objects of type `str` represent text in our programs. String methods help
manipulate text.

Integers
========

Objects that are instances of type `int` represent whole numbers.

creation 
--------
::

    >>> 3              # literal
    3
    >>> type(5)        # confirm type
    int

methods
-------

::

    >>> help(5)        # display documentation

The arithmetic operations you'd expect are implemented on int objects::

    >>> 5 + 4
    9
    >>> 5 - 6
    -1

Two objects of type `int`, separated by an arithmetic operators `*` `/` `-` `+`, have the
exact behaviour we expect from basic arithmentic.


Objects of type `int` represent whole numbers in our programs. Their methods
map to arithmetic enabling us to use them to solve basic math problems.

Exercises
=========

'5' Vs 5
--------

What does the interpreter do when you type:: 

    >>> '5'

Followed by enter?

Same again for::

    >>> 5

Describe every step.

Strings, Integers, and +
------------------------

Both string and integer objects recognise the `+` symbol.

What output would you expect in the following?

::

    >>> '1' + '2'
    _____?
    >>> 1 + 2
    _____?

Test your answer with python.

Try the same above but this time using `*` instead of `+`. What can you
conclude of the meaning of `*`?

Using the output of::

    >>> help(str)
    [ .... ]
    >>> help(int)
    [ .... ]

Which double underscore function do you think might be at play?

names and values
----------------

Given this code::

    five = "five"

What is the difference between the meaning of each set of characters on either
side of the equal sign?

`str` functions 
---------------

Using the `help`, for the `str` and the string 'abcabc' as an example find a method that:

* confirms whether the string is alphabetical
* confirms wether the string is alphnumerical
* confirms whether the string is lower
* returns `Abc`
* returns `ABC`
* counts the number of 'a's

.. tip::

    * docs https://docs.python.org/3/library/stdtypes.html#string-methods

Koans - `str` functions
-----------------------

:: 

    python3 contemplate_koans.py about_strings
    python3 contemplate_koans.py about_strings_manipulation
