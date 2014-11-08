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

Python on Windows

::

C:\Users\greg-lo>\Python34\python.exe
Python 3.4.2rc1 (v3.4.2rc1:8711a0951384, Sep 21 2014, 21:16:45) [MSC v.1600 32 b
it (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import turtle
>>> turtle.forwards(10)

Koans
=====

Effective learning practice and repetition. Koans are a great way to do this in
programming.

Throughout the course we will make reference to these koans.

Downloading Koans
-----------------

Python Koans is available on Github:

    https://github.com/arachnegl/python-koans

You will need to download the source as a zip and unzip it on your machine.

Follow the instructions on the above link.

Running
-------

C:\Users\greg-lo>\Python34\python.exe
Python 3.4.2rc1 (v3.4.2rc1:8711a0951384, Sep 21 2014, 21:16:45) [MSC v.1600 32 b
it (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import turtle
>>> turtle.forwards(10)

::

    > python3 contemplate_koans.py about_asserts

    Thinking AboutAsserts
      test_assert_truth has damaged your karma.

    You have not yet reached enlightenment ...
      AssertionError: 0 is not true

    Please meditate on the following code:
      File "/Users/greg/TEACHING/python_koans/koans/about_asserts.py", line 13, in test_assert_truth
        self.assertTrue(_____)  # This should be true


    You have completed 0 koans and 0 lessons.
    You are now 77 koans and 9 lessons away from reaching enlightenment.
