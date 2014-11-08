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


Windows
=======

We interact with python using the command program.

You can find it by searching in the start prompt. 

A shortcut: 

* Press these two keys together `Windows + R` 
* In the serach prompt that pops up enter and select `cmd.exe`.

cmd.exe cheat sheet
-------------------

* exit  - exit cmd.exe
* cd    - change directory
* dir   - list the directory's contents
* copy  - copy a file or a directory
* move  - move a file or a directory
* mkdir - make a directory
* del   - delete a file or directory

Running Python
--------------

When you install python in windows it gives you the option to add the
executable (`python.exe`) to your system path. 

Unfortunately we need to specify the full path each time: `\Python34\python.exe`.

::

    C:\Users\greg-lo>\Python34\python.exe
    Python 3.4.2rc1 (v3.4.2rc1:8711a0951384, Sep 21 2014, 21:16:45) [MSC v.1600 32 b
    it (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import turtle
    >>> turtle.forwards(10)


Koans
=====

Learning takes practice and repetition. Koans are a great way to do this in
programming.

Throughout the course we will make reference to these koans.

Setup 
-----

Python Koans is available on Github:
Steps:

* Download zip from https://github.com/arachnegl/python-koans
* move it from Downloads into your home directory (for me its `C:\Users\greg-lo`)
* unzip it 
* change directory (`cd`) into the python-koans-master directory

Here are the commands::

    C:\Users\greg-lo>\move Downloads\python-koans-master .
    C:\Users\greg-lo>\unzip python-koans-master.zip
    C:\Users\greg-lo>\cd python-koans-master
    C:\Users\greg-lo\python-koans-master>

Running
-------

Now we are ready to execute the contemplate_koans.py program::

    C:\Users\greg-lo>\Python34\python.exe contemplate_koans.py about_asserts

    Thinking AboutAsserts
      test_assert_truth has damaged your karma.

    You have not yet reached enlightenment ...
      AssertionError: 0 is not true

    Please meditate on the following code:
      File "/Users/greg/TEACHING/python_koans/koans/about_asserts.py", line 13, in test_assert_truth
        self.assertTrue(_____)  # This should be true


    You have completed 0 koans and 0 lessons.
    You are now 77 koans and 9 lessons away from reaching enlightenment.

Note that you are asked to mediate on a file with a line number.

Open this file in SublimeText. You can find SublimeText in the Start search prompt.

Open the file as per the output of `contemplate_koans`:
C:\Users\greg-lo\python-koans-master\koans\about_asserts.py

* Go to line 13 and replace `____` with True. 
* Save the file. 
* Rerun the Koans     
     C:\Users\greg-lo>\Python34\python.exe contemplate_koans.py about_asserts

You should find that one line has gone Green. You now have a new challenge.

.. tip::

    It is often easy to confuse the command shell and the python interpreter.
    Python doesn't run in the command shell and likewise shell commands don't
    work in the interpreter.

    The interpreter has `>>>` as its prompt

    The command shell has the file path eg `C:\Users\greg-lo\>`

Exercise
========

Using your intuition alone try to complete the about_asserts koans.

