Conclusions
***********

Programming
===========

The constructs we have learned (loops, conditions, data structures) mean that we
can be very expressive as programmers.

Combined with abstractions we can combine new programs together.

Building on our previously defined concept of a house we now use repetition
to define a row of houses.

::

    def row_of_houses(number, size):
        for i in range(number):
            house(size)
            turtle.forward(size)

This is how complex and useful programs are built.


Abstractions
============

We have gone from understanding this::

    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

to programming like this::

    def square(side):
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)

Why is the second version better than the first?

Computers are complex. Even the smallest operation hides layers of incredible
complexity. Programming is not only about getting a computer to do things. It is about
writing code that is useful to humans.

Good programming is harnessing complexity by writing code that rhymes with our
intuitions. Good code is code that we can use with a minimal amount of context
and that allows us to be productive straight away.

By calling::

    >>> square(100)

The above code called `square` can be understood even by a non programmer. Intuition
helps because the code is defined at the appropriate level of abstraction over the complex details for understanding to take place.

The two major advantages are:

* detail and complexity is hidden.
* the definition of the function object called `square` is shorter clearer
  and truer to its mathematical (conceptual) definition.


This course illustrates that creative programming is about constructing useful
abstractions. It is also about exercising your intuition to make you more
productive.

Design
======

We have gone from step by step instructions to defining blocks of code in such
a way as to define higher level concepts.

Defining reusable components and the ability to repeat them is immensely powerful.

Think of everything you can make from Lego bricks. Minecraft is a world build
with cubes. In the real world think of all the components and repetition you
typically find in a skyscraper.

This is where programming starts to become creative. You can define the
universe of things that is of interest to you.


Exercises
=========

A Text editor
-------------

Think about the objects that you'd have to use to represent editing text.


Your Project
------------

Programmers model other domains. Think of an area in which you are an expert and
how you might code it.

What objects, functions and variables would need to be defined?
