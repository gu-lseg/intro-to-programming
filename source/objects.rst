Objects
*******

We live in a world that contains things and we use language to refer to these things. We will call things objects and the world an environment. 

Python is two things:

* An Interpreter - The environment.
* A language - Used to refer, create, and interact with the objects in an 
  environment.

Everything in python is an object. Turtle is an object.

An Object:

* Physically, exists as a pattern of 0s and 1s in the computer's memory. 
* Conceptually, represents something with meaning to the programmer.

Programming is about defining and manipulating objects.

Types
=====

Things are classified as types and a type defines a set of attributes and behaviours. 

There are many objects that are instances of the abstract type chair. All chairs have 4 legs and can be moved or sat on. 

The type of a Python object also determines the attributes and actions that
it has and how to interact with it.

The turtle object has an attribute that is::

    >>> turtle.pi

Turtle behaviour:: 

    >>> turtle.forward(25)
    >>> turtle.shape("turtle")

All the above is defined in python code. It is the interpreter that executes these instructions within an environment.


`type('a')`, `isinstance('a', str)`
===================================

Introspecting objects is often very useful.

Use this to get the type of an object:: 

    >>> type(5)


This confirms whether an object is of a certain type:: 

    >>> isinstance('5', int)


`dir('a')`
==========

Use this to get a list of attributes and methods of an object:: 

    >>> dir('5')
    [ ... many methods ... ]
    >>> dir(5)
    [ ... many methods ... ]
    

Strings 
=======

An object of type String has a sequence of letters::

    >>> "hello"
    'hello'
    >>> type("hello")
    str

Language Syntax: a sequence of letters starting and ending with ``"`` (a double quote)
indicates a String object to the interpreter.


Integers
========

Integers are positive numbers::

    >>> 5
    5
    >>> type(5)
    int

A number indicates an Integer to the interpreter. Unlike for strings no special syntax
is needed. In a way a number represents itself.

    
Exercises
=========

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

String methods
--------------

For the string 'abcabc' find a method that:

* confirms whether the string is alphabetical
* confirms wether the string is alphnumerical
* confimrs whether the string is lower
* returns `Abc`
* returns `ABC`
* counts the number of 'a's

Tips:

* Search dir('abcabc') for contenders and experiment
* Familiarise yourself with the official docs https://docs.python.org/3/library/stdtypes.html#string-methods

