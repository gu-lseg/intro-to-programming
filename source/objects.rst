Objects
*******

We see the world as containing objects. We classify those objects according to
types.

In a classroom there many objects that are instances of the type chair. You also have many objects that are instances of the type person.

Chairs have attributes. They typically have four legs and a back. Persons also
have attributes. They have 2 legs, 2 arms, a head... 

Objects of type Person can interact with objects of type Chair in various ways. 
They can sit on them, move them, or even stand on them.


Types
=====

An Object:

* Physically exists as a pattern of 0s and 1s in the computer's memory. 
* Conceptually represents something with meaning to the programmer.

An object is always an instance of a Type. Type determines an objects:

* attributes
* behaviours (we call these methods)

Programming is about defining and manipulating objects to do something
meaningful to the programmer.

In this section we are interested in:

* creating objects using literals and constructors.
* inspecting objects using introspection functions.


Introspection 
=============

The functions `type('a')` and `dir('a')` help us learn about objects::

    >>> type(5)
    int
    >>> type('5')
    str
    >>> dir('5')
    [ ... list of attributes and methods of an object ... ]
    >>> dir(5)
    [ ... list of attributes and methods of an object ... ]
    

Strings 
=======

Objects that are instances of type `str` represent text.

creating `str` instances
------------------------
::

    >>> "hi"           # literal
    hi
    >>> str("hi")      # constructor function
    hi
    >>> type('hi')     # confirm type
    str

When you execute the code `"hi"` or `str("hi")`, the python interpreter:

1. Creates an object of type `str`
2. Gives it the value "hi"
3. Returns this newly created object

introspecting `str` instances
-----------------------------

What attributes and functions

`str` functions::

    >>> dir("string")
    [' .... many .... ']

Many methods are defined on objects of type `str`. These facilitate working with text.
Use the documents to get an overview.

https://docs.python.org/3.4/library/string.html

Integers
========

Objects that are instances of type `int` represent whole numbers.

creating `int` instances
------------------------
::

    >>> 3              # literal
    3
    >>> int(-5)        # constructor function
    -5
    >>> type(5)        # confirm type
    int


introspecting `int` instances
-----------------------------

Methods defined on objects of type `int`::

    >>> dir(5)
    [ ... many ... ]

The arithmetic operations you'd expect are implemented on int objects::

    >>> 5 + 4
    9
    >>> 5 - 6
    -1

For two objects of type `int` it's interpretation is identical to basic
arithmentic.


`+` and `__add__`
=================

The symbol `+` is called an operator. It takes two objects on either 
side of it. Its interpretation depends on the types of objects it is applied to. 

`x + y` resolves to `x.__add__(y)`

::

    >>> 1 + 2
    3
    >>> one = 1
    >>> one.__add__(2)
    3
    >>> '1' + '2'
    '12'
    >>> '1'.__add__('2')
    '12'

.. tip:: 

    Any object that implements the `__add__` function will work
    with the `<object> + x` syntax.

.. tip:: 

    Other operators: `*` `-` `/`

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

    >>> dir('5')
    [ .... ]
    >>> dir(5)
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

Using the interpreter and introspection functions, for the string 'abcabc' find a method that:

* confirms whether the string is alphabetical
* confirms wether the string is alphnumerical
* confirms whether the string is lower
* returns `Abc`
* returns `ABC`
* counts the number of 'a's

.. tip::

    * Search dir('abcabc') for contenders and experiment
    * docs https://docs.python.org/3/library/stdtypes.html#string-methods

Koans - `str` functions
-----------------------

:: 

    python3 contemplate_koans.py about_strings
    python3 contemplate_koans.py about_strings_manipulation


`*` `/` `-` `%` Operators
-------------------------

Using introspection which special functions does the following syntax
resolve to:

* `3 - 2`
* `3 * 2`
* `3 / 2`
* `3 % 2`

String representations
----------------------

What function gets called when we get results in the interpreter?
Is it the same that gets called when we type `print(x)`?

