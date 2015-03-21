Introduction
************

Learning to program requires much practice. However it is also very rewarding and creative.

The purpose of this course it to give you enough programming vocabulary to
get a taste of what it is.

Hello and Welcome
=================

1. Press `Windows + R` (the two keys together)
2. A search box pops up.
3. Type `cmd.exe` and press enter. 

When `cmd.exe` launches you see:: 

    C:\Users\greg-lo>

The line tells you your current location followed by a prompt `>`. 

`cmd.exe` is a program often called a shell. It is an alternative to the point and
click that we are all used to.

Typing `python`, you enter the python interpreter::

    C:\Users\greg-lo> python3
    Python 3.4.2 (v3.4.2:8711a0951384, Sep 21 2014, 21:16:45) [MSC v.1600 32 b
    it (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Note the prompt has changed to `>>>`. Python is waiting for your instructions.

.. tip::

    Do not confuse the shell with the python interpreter.

    If the prompt is `>` you are in cmd.exe, if the prompt is `>>>` you are in
    the python interpreter.

In Python type the following and press enter::

    >>> print('hi')

Congratulations you have just written and executed a line of python!

Exercise
--------

Explore and experiment with the interpreter. Try printing other words.

Can you make Errors appear (it shouldn't be too difficult)? 
How many different ones can you make?

Errors
======

Getting errors and troubleshooting them is a large part of programming.

Typically given a problem to solve a programmer thinks up an idea that may work then
battles through errors until it does work.

Beginners understandably often get frustrated with
them. However, build up resilience by taking time to understand them. 
They are always correct and trying to guide you to a solution. 

Here are three you will see a lot are::

    >>> def asdfwe:
      File "<stdin>", line 1
        def asdfwe:
                  ^
    SyntaxError: invalid syntax

    >>> if 5 > 6:
    ... print('yes')
      File "<stdin>", line 2
        print('yes')
            ^
    IndentationError: expected an indented block

    >>> def asdfwe:
      File "<stdin>", line 1
        def asdfwe:
                  ^
    SyntaxError: invalid syntax

By the end of this course, you should be able to instantly map the above errors
to solutions.

Object oriented programming
===========================

We can see our world as containing different types of objects that we can classify according to common attributes and behaviours.

For example in a classroom there many objects that are instances of the type Chair and many other objects that are instances of the type Person.

Objects have:

* Attributes - Chairs have four legs, Persons have two.
* Behaviours - Persons can walk. Persons can move chairs.

Objects can interact with other objects of different types. An object of type Person can
can sit on an object of type Chair. 

This is the essence of object oriented thinking. It is about using programmatic 
objects to model a domain of interest to a programmer.

This style of programming provides a clear, simple, and consistent model of computation
that maps well to our intuitions about the world.

This course introduces different types of objects: `String`, `Integer`, `Turtle`. 

You will discover what attributes and behaviours these objects have and how
to use these to write programs to get stuff done.

Python
======

Python is a simple to learn yet fully featured, high-level, object oriented programming language. It's popular both in academia, science and other industries. The concepts however will apply to most other object oriented languages. 

Two things to bear in mind:

* A language - The textual instructions you type.
* An interpreter - A program (called `python`) that reads and executes that language.

Together we will learn the correct syntax and grammar of the Python language. 

When we ask the interpreter to execute it, it is interpreter that understands how to translate Python scripts into creating and manipulating objects according to your instructions.

Questions
---------

What other languages have you heard of?

Explain in your own words but using the concepts `interpreter` and `language`
what happened above when you printed text.

Language goals
==============

Our goal is move from this::

    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

to this::

    def square(side):
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)

Questions
---------

Amongst yourselves:

* What does the first code extract do?
* What does the second code extract do?
* Which do you prefer and why?
