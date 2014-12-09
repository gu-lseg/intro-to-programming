Introduction
************

Learning to programm requires much practice and is very rewarding and creative.

The purpose of this course it to give you enough programming vocabulary to
get a taste of what it is.


Object oriented programming
===========================

Our world contains objects and we classify these according to types.

In a classroom there many objects that are instances of the type Chair. You also have many objects that are instances of the type Person.

Chairs have attributes. They have four legs and a back. Typically Persons 
have two legs, two arms, one head... 

Objects have behaviours. An object of type Person can walk.

Objects of different types can interact together. An object of type Person can
sit on an object of type Chair.

This is the essence of object oriented thinking. It is about using programmatic 
objects to model something an area of interest.

This style of programming provides a clear, simple, and consistent model of computation
that maps well to our intuitions.

Python
======

This course uses Python to introduce Object Oriented programming.

Python is chosen as it is a simple, high-level, object oriented programming language. It's very popular in both the academic world and widely used in industry. 

The concepts however will apply to most other object oriented languages. 

Python consists of two things:

* an Interpreter - Creates and maintains an environment within which it interprets the python language.
* a Language - Used to refer, create, and interact with objects in an environment.

We can interact with the interpreter in 3 different ways:

* running code from a file
* interactive coding using the python interpreter
* step by step execution using `pdb` the python debugger

These approaches complement each other.

Language goals
==============

Our goal is move from::

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
