Introduction
************

Programming is a creative activity.

Like most things worth learning it takes some time to learn.

You don't expect to learn a foreign language or a musical instrument in
a weekend. Master musicians state they are always learning. With programming it
is the same.

The purpose of this course it to give you just enough programming vocabulary to
get a taste of what it is.

Although we use Python, the concepts are the same in most other languages.
Indeed any second language is easy to learn after the first.

A world of objects
==================

We live in an environment that contains objects and we use language to refer to them. Similarly programming involves creating a manipulating objects in an environment.

Everything in python is an object. Turtle for example is an object.

Python consists of two things:

* an Interpreter - Creates and maintains an environment within which it interprets the python language.
* a Language - Used to refer, create, and interact with objects in an environment.


Programming ability 
===================

Give you just enough programming ability to go from::

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


Goal: Abstractions
==================

The main take away this course illustrates is the idea of using your
programming to express abstractions that are useful to your area of interest.

In the above code note that we go from a series of instructions to a named
block of shorter instructions. 

If you call::

    >>> square(100)

The code does the exactly the same. 

The second one is at a higher level of abstraction. We will learn to understand
that one better. We will also conclude that we can reuse it to compose more
complicated concepts.

Don't worry if you didn't completely understand the above. You weren't meant
to. The course will revisit these ideas throughout and especially conclude with
them.

Practice using Koans
====================

Repeititon is key to learning programming. Koans are a way to rote learn.

https://github.com/arachnegl/python-koans
