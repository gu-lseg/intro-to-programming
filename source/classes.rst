Classes
*******

User Defined Types
==================

Classes are how programmers define objects that make new objects. Think of them
as object templates or factories.

Defining
========

A `python.py` file contains:: 

    class Python():
        
        def __init__(self, name, sex, age, length):
            self.name = name
            self.sex = sex
            self.age = age
            self.length = length

        def move(self):
            print("{} moves".format(self.name))


class object
=============

::

    >>> from python import Python
    >>> type(Python)
    <class 'type'>
    >>> dir(Python)
    [ ... many methods ... ]


Instances
=========

Creating
--------

::
    
    >>> john = Python('John', 'M', 15, 4)
    >>> type(john)
    <class 'python.Python'>
    >>> dir(john)
    [ ... many methods ... ]


Note we get `move` which we defined, but we also get many methods others.

Functions & Methods
===================

::
    >>> Python.move
    <function Python.move at 0x10f9b6840>
    >>> john.move
    <bound method Python.move of <python.Python object at 0x10fb04898>>

A function and a method are very similar. A function can stand alone, a method
however is 'bound' to an object. When defined methods always take self as their
first argument. It is thereby implicit when called.

__str__
========

The `__str__` method is called on an object when we pass it to the `print` function.

We decide that the semantics of printing a python is to show a visual
representation of a snake using characters.

New definition in `python.py`::

    class Python():
        
        def __init__(self, name, sex, age, length):
            self.name = name
            self.length = length

        def __str__(self):
            body = '=' * self.length
            return "{}>".format(body)

Interactive shell::

    >>> from python import Python
    >>> john = Python('John', 5)
    >>> print(john)
    ~-=====%>



Exercises
=========

Decide on the semantics of the following built in magic methods:

__add__

__lt__
