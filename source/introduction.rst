Introduction
************

Learning to program requires much practice. However it is also very rewarding and creative.

The purpose of this course it to give you enough programming vocabulary to
get a taste of what it is.

print('Hello')
==============

First we need to open the 'terminal' - An application that provides text-based access to the operating system.

1. Press `Cmd(apple) + Spacebar` (the two keys together). A search box pops up.
2. Type `terminal` and press enter. 

The program `terminal` will launch and you should see a prompt:: 

   ~

The line tells you your current location followed by `>`. 

`terminal` is a program often called a shell. It is an alternative to the point and
click 'graphical user interface' that we are all used to.

Typing `python` and you enter the python interpreter::

    ~> python
    Python 2.7.11 (default, Dec 26 2015, 17:47:15) 
    [GCC 4.2.1 Compatible Apple LLVM 7.0.2 (clang-700.1.81)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Note the prompt has changed to `>>>`. Python is waiting for your instructions.

.. tip::

    Do not confuse the shell with the python interpreter.

    If the prompt is `>` you are in terminal
    If the prompt is `>>>` you are in the python interpreter.

In the interpreter type the following and press enter::

    >>> print('Hello')

Congratulations you have just written and executed a line of python!

Exercise
--------

1. Explore and experiment with the interpreter. Try printing other words.

2. What happens if you miss off the end bracket `print('hello'`? How do you continue?

3. Can you make Errors appear (it shouldn't be too difficult)? 
   How many different ones can you make? Make a list and google each one.

Errors
======

Troubleshooting errors is a large part of programming.

Typically given a problem to solve a programmer thinks up an idea that may work then
battles through errors until it does work.

Often beginners understandably get frustrated with them. Don't. Instead build up 
resilience by taking time to understand them. 
They are always correct and trying to guide you to a solution. 

Here are three you will see a lot::

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

By the end of this course, you should be able to instantly understand and map the above errors
to solutions.

.. tip::

    Troubleshooting Errors:

    1. Reading error messages. Try to intuitively solve them.
    2. Google errors. There isn't a single error someone hasn't already had.
    3. Ask an expert. If really stuck ask someone for help.

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

Python
======

Python is a simple to learn yet fully featured, high-level, object oriented programming language. It's popular both in academia, science and other industries. The concepts however will apply to most other object oriented languages. 

Two things to bear in mind:

* A language - The textual instructions you type.
* An interpreter - A program (called `python`) that reads and executes that language.

Together we will learn the correct syntax and grammar of the Python language. 

When we ask the interpreter to execute it, it is interpreter that understands how to translate Python scripts into creating and manipulating objects according to your instructions.

This course introduces different types of Python objects: `String`, `Integer`, `Turtle`, `lists`...

You will discover what attributes and behaviours these objects have and how
to use these to write programs to get stuff done.

Questions
---------

1. What other languages have you heard of?
2. Explain in your own words but using the concepts `interpreter` and `language`
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
