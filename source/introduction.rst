Introduction
************

Learning to programm takes practice.

It requires application and is very rewarding and creative.

The purpose of this course it to give you just enough programming vocabulary to
get a taste of what it is.

Python
======

Python is a good language to learn as it is simple, high-level, powerful, and
widely used in industry.

Whilst python is taught the concepts are the same in most other languages. 

Python consists of two things:

* an Interpreter - Creates and maintains an environment within which it interprets the python language.
* a Language - Used to refer, create, and interact with objects in an environment.

Using the python language we will interact with the interpreter in 3 different ways:

* running code from a file
* interactive coding using the python interpreter
* step by step execution using `pdb` the python debugger

These approaches complement each other.

Object oriented programming
===========================

Our world contains objects and we use language to refer to them. Similarly object oriented programming involves creating and manipulating objects in an environment.

We show that the inuitive syntax that python offers systematically 
reduces to a single type of operation: objects calling methods on each other.

For example::

    >>> 'a' + 'b' 
    'ab'
    >>> 'a'.__add__('b')
    'ab'

We will learn that Python offers a variety of builtin `special` methods
(functions defined on objects).

This style of programming provides a clear, simple, and consistent model of computation
that maps well to our intuitions.

Language goals
==============

Enough programming ability to go from writting::

    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

to::

    def square(side):
        for i in range(2):
            turtle.forward(side)
            turtle.left(90)


Abstractions
============

A novice can read the above and make some sense of it. Intuition helps because
the developer who wrote the code defined a good level of abstraction over the 
complex details.

This course illustrats that creative programming is aobut constructing abstractions useful to an area of interest.

By calling::

    >>> square(100)


the result is the same as executing all the 8 lines of previous code. 

The interpreter is indifferent to the two bits of code. It is the
longer snippet that will be executed anyway.

But there are two major advantages for us programmers:

* the detail and complexity is gone. A user can fire and forget, relying 
  on intuition to get her job done.
* the definition of the function object called `square` is shorter clearer
  and truer to its mathematical (conceptual) definition.

By defining and composing layers of abstraction we arrive at ever more 
useful programs.


Exercises
=========

There are plenty of exercises throughout this course and they are of two types.

`shapes.py`
-----------

We will use a drawing tool called `turtles` combined with concepts from simple geometry in order to learn about designing abstractions.

Throughout the course your `shapes.py` python file will evolve as you
learn new programming constructs.

Koans
-----

A koan is like a mini snippet of code. It presents a puzzle for you to resolve.

We use Koans to gain hands on practice using intuition and experimentation.

Throughout the course we will make reference to these koans.


Instructions
------------

Instructions for running python and the koans are in the Appendix. Go there
now.
