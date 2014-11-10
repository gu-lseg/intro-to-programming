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

Learning Tips 
=============

Intuitions
----------

Your intuitions are your best guide. Always try to understand, never be
bothered by not getting it. Keep your questions as pending. You don't need to
understand everything.

Practice & experiment
---------------------

Ideally try to program one hour a day.

Always experiment and try things out. You can only learn to program by doing.

Emotions
--------

Learning something like programming can be frustrating. 

Computers and humans are different; we excel at different things. 

Computers are utterly stupid, they are unforigivingly precise and logical. 
Humans can be logical but they also have intelligence, imagination, and creativity.

All programmers, beginners and advanced, make plenty of mistakes and often get stuck. 

Manage your expectations. Know that everyone has been through the same.
Computers are a tool waiting for you to learn to master them.

Everyone can learn to program
-----------------------------

Studies have shown the only difference between people who are good at
programming and those who aren't is almost completely related to amount of time spent programming.

Go very slow
------------

As humans we think at a higher intuitive level. We think square, or move
forward. 

Computers need everything broken down into steps. Each step is a command.

Programming as an activity is about breaking down our concepts into smaller defined steps.
In effect we define our concepts in commands.

Find a project
--------------

Although programming has plenty of intrinsic value its only as popular as it is
because of the things you can do with it.

Unfortunately we won't look into detail at the many application domains as we
don't have time. Use the resources section to choose an area that is of
interest and focus on it.

World of objects
================

We live in an environment that contains objects and we use language to refer to them. Similarly programming involves creating and manipulating objects in an environment.

Python is a programming language and it is used to create and manipulate things in an environment. Everything that can exist in python is an object. 

Python consists of two things:

* an Interpreter - Creates and maintains an environment within which it interprets the python language.
* a Language - Used to refer, create, and interact with objects in an environment.


Python language goals
=====================

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


Shapes and Koans
================

There are plenty of exercises in this course. They come in two types.

`shapes.py`
-----------

We will use turtles and geometry in order to learn about designing abstractions

The outcome is that you have a `shapes.py` python file that evolves as you
learn new programming constructs.

Koans
-----

As noted learning to program takes practice and repetition. 

Programming koans are a great way to do this. 

Throughout the course we will make reference to these koans.

Instructions
------------

Instructions for running python and the koans are in the Appendix. Go there
now.
