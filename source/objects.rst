Objects
*******

An Object:

* Physically, exists as a pattern of 0s and 1s in the computer's memory. 
* Conceptually, represents something with meaning to the programmer.

Programming is about defining and manipulating objects to do something
meaningful to the programmer.

To know an objects' memory location::

    >>> id('a')
    4403687864

Every object has a type and a way to create them.

Types
=====

Objects are instances of a type. An objects' type defines its set of attributes and behaviours.

Taking the turtle object as an example:

attributes::

    >>> turtle.pi

behaviour:: 

    >>> turtle.forward(25)
    >>> turtle.shape("turtle")

The interpreter executes these instructions. It knows how to match the sequence
of letters typed in and executed to existent code that defines the `turtle`
object.

Introspection 
=============

The `type('a')` and `dir('a')` functions help us learn about objects::

    >>> type(5)
    int
    >>> type('5')
    str
    >>> dir('5')
    [ ... list of attributes and functions of an object ... ]
    >>> dir(5)
    [ ... list of attributes and functions of an object ... ]
    
We will use the above functions to explore the next two object types.

Strings 
=======

`str` objects represent text in Python

::

    >>> type('hi')
    str

Creation::

    >>> "hi"       # literal
    hi
    >>> str("hi")  # constructor
    hi

On `enter` a newly created `str` object is `returned` by the interpreter on the
following line.

`str` functions::

    >>> dir("string")
    [' .... many .... ']

Many functions are defined by the `str` type to facilitate working with text.
Use the documents to get an overview.

https://docs.python.org/3.4/library/string.html

Integers
========

Integers are whole numbers

::

    >>> type(5)
    int


Creation::

    >>> 3
    3
    >>> int(-5)
    -5

Like strings the interpreter takes a number typed by the programmer literally. Thus it creates an object of type `int` with the value 5.

`int` functions:: 

    >>> dir(5)
    [ ... many ... ]

Mathematical operations you'd expect are implemented on int objects::

    >>> 5 + 4
    9
    >>> 5 - 6
    -1

Note:: 
    
    >>> int.__sub__(5, 6)
    -1

The notation `5 - 6` and `int.__sub__(5, 6)` is different but have the same
result.

Actually the `-` is resolved to `__sub__` by the interpreter. When the
interpreter reads `5 - 6` it knows to resolve the `-` to `__sub__`. 


The point is despite special syntax Python consistently operates on functions defined on objects.


Strings and Integers with +
---------------------------

Both string and integer objects respond to the `+` symbol.

What do you expect the difference to be between the following commands?

First plus sign with strings::

    >>> 'abc' + 'def'

Second plus sign with integers::
    
    >>> 5 + 4

Test your answer with python.

Try the same above but this time using `*` instead of `+`. What can you
conclude of the meaning of `*`?


'5' Vs 5
--------

What is the diffference between::

    '5'

and::
    
    5


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

    > python3 contemplate_koans.py about_asserts

::

    > python3 contemplate_koans.py about_strings

::

    > python3 contemplate_koans.py about_strings_manipulation
