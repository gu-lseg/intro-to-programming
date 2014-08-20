Names
*****


Assigning objects to names 
==========================

It is natural that when speaking of a specific object we give it a name.

The names we give our objects are much like the Nouns we use in every day
speach.

Lets name some numbers::

    >>> x = 5
    >>> four = 4

Lets name some strings::

    >>> first_name = "greg"

Unlike in maths, the equals symbol means assignment rather than equality.
Python reads `x = 5` as assign the value (Integer object) 5 to the name x.


Names in Python can refer to any type of objects::

    >>> x = 5            # x refers to an Integer object
    >>> x = 'greg'       # x refers now to a String object 


Names evaluate to objects
=========================

Once defined, when used, a name evaluates to its value::

    >>> x
    5

Think of typing a name as fetching the value (object) it refers to.

Ways to define names
====================

We define a name either by importing it::
    
    >>> import turtle
    >>> turtle 
    <module 'turtle' from '/python2.7/lib-tk/turtle.py'>
    >>>

Or by assigning any object to the name::

    >>> turtle = "turtle"
    >>> turtle
    'turtle'

Remember a function object also has a name. A third way of defining a name is
by defining a function.

We are about to cover defining functions. But here is a preview::

    >>> def my_function():
    ...     print('hello')    # Note 4 space indentation
    ...


Calling functions with names
============================

We can also use call some functions by putting defined names within the ()s.

If you call print with the variable x ``print(x)``, you will output x's value.

With turtle::
    
    >>> import turtle
    >>> x = 5
    >>> turtle.forward(x)

More on this to come.

NameError
=========

Here we introduce the NameError::

    >>> turtle
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'turtle' is not defined
    >>>

Python is telling us it doesn't know what the turtle name refers to. We haven't
defined it. We have forgotten to import it.
