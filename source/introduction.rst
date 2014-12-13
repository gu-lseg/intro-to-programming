Introduction
************

Learning to programm requires much practice and is very rewarding and creative.

The purpose of this course it to give you enough programming vocabulary to
get a taste of what it is.


Object oriented programming
===========================

Our world contains objects and we classify these according to types.

In a classroom there many objects that are instances of the type Chair. You also have many objects that are instances of the type Person.

Objects have:

* Attributes - Chairs have four legs. 
* Behaviours (called methods) - Persons can walk.

Objects can interact even if they are of different types. An object of type Person can
sit on an object of type Chair.

This is the essence of object oriented thinking. It is about using programmatic 
objects to model something of interest to a programmer.

This style of programming provides a clear, simple, and consistent model of computation
that maps well to our intuitions about the world.

Python
======

This course uses Python to introduce Object Oriented programming.

Python is a simple to learn yet fully featured, high-level, object oriented programming language. It's popular both in academia and industry. 

The concepts however will apply to most other object oriented languages. 

Python consists of two things:

* Language - Expresses the creation and interaction of objects in an environment.
* Interpreter - Creates and maintains an environment within which it translates language instructions to actually create and manipulate objects.

Language goals
==============

Our goal is move from step by step instructions such as::

    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

to expressing the same thing but using richer language constructs::

    def square(side):
        for i in range(2):
            turtle.forward(side)
            turtle.left(90)


Abstractions
============

Why is the second snippet of code above better than the first? 

Note that ultimately the computer only knows how to execute step by step instructions anyway.

Computers are complex. Even the smallest operation hides layers of incredible
complexity. Programming is not only about getting a computer to do things. It is about
writing code that is useful to humans.

The result of good programming is code that is understandable to humans. As
programmers we harness complexity by writing code that rhymes with our
intuitions. Good code is code that we can use with a minimal amout of context
and already be productive.

The above code called `square` can be understood even by a non programmer. Intuition
helps because the code is defined at the appropriate level of abstraction over the complex details for understanding to take place.

This course illustrates that creative programming is aobut constructing useful abstractions. It is also about exercising your intuition to make you more productive.

By calling::

    >>> square(100)


But there are two major advantages for us programmers:

* the detail and complexity is gone. A user can fire and forget, relying 
  on intuition to get her job done.
* the definition of the function object called `square` is shorter clearer
  and truer to its mathematical (conceptual) definition.

By defining and composing layers of abstraction we arrive at ever more 
useful programs.


Exercises
=========

There are three types of programming materials.

.. tip:: 
    Instructions for running python and the koans are in the Appendix. 

Turtles
-------

To learn about designing programs we will use a drawing tool called `turtles`.

Throughout the course your `shapes.py` python file will evolve as you
learn new programming constructs.

`turtles` combined with concepts from simple geometry will help us learn about designing abstractions.


Koans
-----

A koan is a code snippet. It presents a puzzle for you to solve.

We use Koans as a kind of drill to gain hands on practice. 

They are to be used in combination with the interpreter where you can
experiment.

Practicals
----------

These are programs you will be asked to write that have some real world value.


