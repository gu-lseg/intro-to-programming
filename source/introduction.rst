Introduction
************

Learning to programm takes practice.

It requires application and is very rewarding and creative.

The purpose of this course it to give you just enough programming vocabulary to
get a taste of what it is.

We use Python, but the concepts are the same in most other languages. 
Learning a second programming language is far easier.


Python
======

Our world contains objects and we use language to refer to them. Similarly programming involves creating and manipulating objects in an environment.

Python consists of two things:

* an Interpreter - Creates and maintains an environment within which it interprets the python language.
* a Language - Used to refer, create, and interact with objects in an environment.


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

Without knowing programming someone can read the above and make some sense of
it. Intuition helps because the developer who wrote the code defined a good level of
abstraction over the complex details.

This course illustrates the idea that creative programming is aobut constructing abstractions that are useful to your area of interest.

By calling::

    >>> square(100)

the result is the same but as a programmer you have kept detail and complexity
at bay.

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
