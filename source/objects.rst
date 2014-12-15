Text & Numbers
**************

In this section we examine three new types of objects

========  ===========  ============
Type      Used for     Examples
========  ===========  ============
Integers  Numbers      -5    16
Floats    Decimal      3.4  -23.001
Strings   Text         'abc' 'bob'
========  ===========  ============

We will look at how to create objects of these types and what methods
(behaviours) they have.


Integers
========

Objects that are instances of type `int` represent numbers with no deciamal
part. They can be positive or negative.

Creation 
--------

::

    >>> 3              
    3
    >>> type(-5)        # confirm type
    int

To convert objects of type `str` into objects of type `int`::

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

.. tip::
    `int` objects are used to solve problems that require manipulating numbers
    but with no decimal point such as age, and days, IDs.

Koans
-----

Run these to explore `int` objects:: 

    python contemplate_koans.py about_integers

Floats
======

`float` objects represent rational numbers, numbers that have a decimal value.

::

    >>> 3.4
    3.4
    >>> type(3.0)
    <class 'float'>
    >>> float('3.4')     # constructor can convert from str
    3.4

All operators we saw defined on `int` work on `float` as you'd expect.

Strings 
=======

Objects that are instances of type `str` represent text.

Creation
--------
::

    >>> "hi"        
    hi
    >>> type('hi')     # confirm type
    str

When you execute the code `"hi"` or `str("hi")`, the python interpreter:

1. Creates an object of type `str`
2. Gives it the value "hi"
3. Returns this newly created object


Methods
-------

Methods that exist on string objects facilitate working with text. We will
explore these by running the koans::

    python contemplate_koans.py about_strings

Consult the online documentation: |string_methods|

.. |string_methods| raw:: html

    <a href="https://docs.python.org/3.4/library/stdtypes.html#string-methods" target="_blank">https://docs.python.org/3.4/library/stdtypes.html#string-methods</a>


Exercises
=========

'5' Vs 5
--------

Describe in detail what the interpreter does when you type the following and
enter:: 

    >>> '5'

    >>> 5

Comparison Operators
--------------------

What is the result this line of code?::

    3 < '5'

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
