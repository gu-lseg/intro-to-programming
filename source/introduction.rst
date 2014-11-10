Introduction
************

Like most things worth learning programming takes time.

You don't expect to learn a foreign language or a musical instrument in
a weekend. Master musicians state they are always learning. With programming it
is the same.

The purpose of this course it to give you just enough programming vocabulary to
get a taste of what it is.

You will find that whilst it requires application it is a very rewarding
activity.

Although we use Python, the concepts are the same in most other languages.
Indeed any second language is easy to learn after the first. 

The differences between any programming language is very litle compared to 
the differences between human languages.

Applied Programming
===================

Although programming has plenty of intrinsic value its only as popular as it is
because of the things you can do with it.

Programming is always applied to something. Its an activity that seeks to
capture some aspect of reality that is useful to us. 

As humans we think at a higher intuitive level. We think square, or move
forward. 

Computers need everything broken down into steps. Each step is a command.

Programming as an activity is about breaking down our concepts into smaller defined steps.
In effect we define our concepts in commands.

Unfortunately we won't look into detail at the many application domains as we
don't have time. Use the resources section to choose an area that is of
interest and focus on it.

A world of objects
==================

We live in an environment that contains objects and we use language to refer to them. Similarly programming involves creating and manipulating objects in an environment.

Python is a programming language and it is used to create and manipulate things in an environment. Everything that can exist in python is an object. 

Python consists of two things:

* an Interpreter - Creates and maintains an environment within which it interprets the python language.
* a Language - Used to refer, create, and interact with objects in an environment.


Intuitions
==========

In the following `turtle` is an object.

We want to give you just enough programming ability to go from writting::

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

Without knowing programming someone can read the above and make some sense of
it.

It is important to practice your intuition and be patient as it evolves.

Abstractions
============

The reason why intuition enables us to understand the above code is because the
developer who wrote the code behind the turtle object defined a good level of
abstraction.

This course also illustrates the idea that creative programming is aobut constructing abstractions that are useful to your area of interest.

In the above code note that we go from a series of instructions to a named block of shorter instructions. 

If you call::

    >>> square(100)

The code does the exactly the same but `square` one is at a higher level of abstraction. 

By defining and composing layers of abstraction we arrive at ever more complex
and useful programs.

Python
======

Instructions for running python are in the Appendix.

Koans
=====

Learning takes practice and repetition. Koans are a great way to do this in
programming.

Throughout the course we will make reference to these koans.

See the appendix for instructions.

Exercise
========

Using your intuition alone try to complete the about_asserts koans.

