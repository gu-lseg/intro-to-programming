Objects
*******

We live in a world of things. We use language to refer to these things.

Similarly, Python is a language that refers to a world of things. Programming, we use and define things.

These things are called objects. Everything in python is an object. Turtle is an object.

Physically, an object is something that exists in the computer's memory. 

Conceptually, an object represents something with meaning to you the programmer.


Objects & Types
===============

We classify things in our world as types and we have words to refer to them.

For example we talk of chairs, doors, people, spaceships...

We understand each type to mean an object that has a set of attributes and
enables actions:
You can sit on a chair; you can open or close a door.

The type of a Python object also determines the attributes and actions that
programmers can interact with.

You have already interacted with turtle's behavour. 

Now we introduce two new basic types.


Strings
=======

Strings are a sequence of letters::

    "hello"

A sequence of letters starting and ending with ``"`` (a double quote) indicates
a String object to python.


Integers
========

Integers are positive numbers::

    5

A number indicates an Integer to python. Unlike for strings no special syntax
is needed. In a way a number represents itself.


Tip:

    You can always ask for the type of an object using this command::

        type(5)


Exercises
=========

Strings and Integers with +
---------------------------

Both string and integer objects respond to the + symbol.

What do you expect the difference to be between the following commands?

First plus sign with strings::

    'abc' + 'def'

Second plus sign with integers::
    
    5 + 4

Test your answer with python.


'5' Vs 5
--------

What is the diffference between::

    '5'

and::
    
    5


names and values
----------------

Given this code::

    hello = "hello"

What is the difference between the meaning of each set of characters on either
side of the equal sign?
