Objects & Names
***************

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


Names
=====

To work effectively with objects we need a way to refer to them. This is called assignemnt.

Names are like the nouns we use in every day speach.

Naming integer objects::

    >>> x = 5
    >>> four = 4

String object::

    >>> first_name = "greg"

Unlike in maths, the equals symbol means assignment not equality.
Python reads `x = 5` as assign the value (object of type `int`) 5 to the name x.

We can reassign variables to any object::

    >>> x = 5            # x refers to an Integer object
    >>> x = 'greg'       # x refers now to a String object 

A variable by itself is an expression and it evaluates to its object::

    >>> x
    5

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

Names & Reusability
===================

Names are often called variables. Names give us a lot of expressivity. They enable you to generalise your code facilitating code reuse.

Consider that you write this code to draw a square::

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

Now you decide the sides should be of length 100.

Without names you have to go back and replace 50 with 100 four times.

Instead using names you can do this::

    side = 50
    right_angle = 90

    turtle.forward(side)
    turtle.left(right_angle)
    turtle.forward(side)
    turtle.left(right_angle)
    turtle.forward(side)
    turtle.left(right_angle)
    turtle.forward(side)
    turtle.left(right_angle)

Now, if you change your mind you need only update one value.

Note that our programatic definition mirrors the mathematical defintion in
that the lenguth of a square's side is irrelevant to its nature as a square.

Names help in: 

- efficient programming.
- capturing meaning. 

Tip:

    If you find yourself needing to replace many similar values in order
    to update your code, using names is worth considering.


    
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

Using the interpreter and introspection functions, for the string 'abcabc' find a method that:

* confirms whether the string is alphabetical
* confirms wether the string is alphnumerical
* confirms whether the string is lower
* returns `Abc`
* returns `ABC`
* counts the number of 'a's

Tips:

* Search dir('abcabc') for contenders and experiment
* Familiarise yourself with the official docs https://docs.python.org/3/library/stdtypes.html#string-methods

Koans
-----
