Objects & Names
***************

We live in an environment that contains objects and we use language to refer to them. Similarly programming involves creating a manipulating objects in an environment.

Everything in python is an object. Turtle for example is an object.

Python consists of two things:

* an Interpreter - Creates and maintains an environment.
* a Language - Used to refer, create, and interact with objects in an environment.

An Object:

* Physically, exists as a pattern of 0s and 1s in the computer's memory. 
* Conceptually, represents something with meaning to the programmer.

Programming is about defining and manipulating objects to do something
meaningful to the programmer.


Types
=====

Things are classified as types and a type defines a set of attributes and behaviours. 

There are many objects that are instances of the abstract type chair. All chairs have 4 legs and can be moved or sat on. 

The type of a Python object also determines the attributes and actions that it has and how to interact with it.

The turtle object has an attribute that is::

    >>> turtle.pi

Turtle behaviour:: 

    >>> turtle.forward(25)
    >>> turtle.shape("turtle")

All the above is defined in python code. It is the interpreter that executes these instructions within an environment.


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


Introspection 
=============

Introspecting objects is often very useful. The `type('a')`, `isinstance('a', str)` and `dir('a')` are functions help us learn about objects.

To get the type of an object:: 

    >>> type(5)


To confirm if an object is of a certain type:: 

    >>> isinstance('5', int)


To get a list of attributes and methods of an object:: 

    >>> dir('5')
    [ ... many methods ... ]
    >>> dir(5)
    [ ... many methods ... ]
    


Names
=====

To work with objects we need a way to refer to them. This is called assignemnt.

Names are like the nouns we use in every day speach.

Naming integer objects::

    >>> x = 5
    >>> four = 4

String object::

    >>> first_name = "greg"


Unlike in maths, the equals symbol means assignment not equality.
Python reads `x = 5` as assign the value (Integer object) 5 to the name x.

Names in Python can refer to any type of objects. 

Here we reassign x to a different type of object::

    >>> x = 5            # x refers to an Integer object
    >>> x = 'greg'       # x refers now to a String object 

Once defined, a name evaluates to its object::

    >>> x
    5

Think of typing a name as fetching the object it refers to.

Functions
=========

A function is a very special kind of object. Functions also have names. You define a name when you define a function.

Example:: 

    >>> def my_function():
    ...     print('hello')    # Note 4 space indentation
    ...

We 'call' functions by adding `()`s at the end of their names.

If you call print with the variable x ``print(x)``, you will output x's value.

With turtle::
    
    >>> import turtle
    >>> x = 5
    >>> turtle.forward(x)

More on this to come.

NameError
=========

Here we introduce the NameError::

    >>> the_holy_grail
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'the_holy_grail' is not defined
    >>>

Python is telling us it doesn't know what the turtle name refers to. We haven't
defined it. We have forgotten to import it.

    
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

