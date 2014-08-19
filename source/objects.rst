Objects - Things
****************

Objects & Types
===============

Python is a language of things called objects. Everything is an object.

Physically, an object is something that exists in the computer's memory.

Conceptually, an object represents something with meaning to the programmer and
python.


An object's type defines the behaviour and use of an object.

Think of analogies in real life:

- A door can be closed. 
- A chair can be sat on.
- A chair can't be closed.
- A door can't be sat on.


Aside - Running Python
======================

One way to run python is by using the interactive shell.

Type ``ipython`` in the terminal.

Now type::

    import turtle
    turtle.shape("turtle")
    turtle.forward(25)


The other (more usual) way to run Python programs is by using files. 

Put this into a file::

    # A line beginning with '#' is a comment. Python ignores it.

    import turtle
    turtle.shape("turtle")
    turtle.forward(25)
    turtle.exitonclick()  # Why this? Test by commenting it out.

Save the file and now run it with::

    python my_turtle_file.py


Strings & Integers
==================

Here are two types of objects.

Strings are a sequence of letters::

    "hello"

A sequence of letters starting and ending with ``"`` (a double quote) indicates
a String object to python.

Integers are positive numbers::

    5

A number indicates an Integer to python. Unlike for strings no special syntax
is needed. In a way a number represents itself.

Strings and numbers are different types of things.

Exercises
=========

Use the interactive python shell.

Different behaviour with +
--------------------------

Both string and integer objects respond to the + symbol.

What are the diffferences between::

    'abc' + 'def'

and::
    
    5 + 4


'5' Vs 5
--------

What is the diffference between::

    '5'

and::
    
    5
