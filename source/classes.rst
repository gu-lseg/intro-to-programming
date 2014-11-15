Classes
*******

We are now going to bring what we have learnt about object oriented programming
together as we define our own object type using classes.

Classes are how programmers define objects that make new objects. Think of them
as object templates or factories.

.. tip::

    The Koans are structured as classes with each koan as a method.

Defining a Class
================

Much like we defined functions lets define a class.

A `python.py` file contains:: 

    class Python():
        """ A class that represents a snake """
        
        def __init__(self, name, sex, age, length):
            self.name = name
            self.sex = sex
            self.age = age
            self.length = length

        def move(self):
            print("{} moves".format(self.name))

        def eat(self):
            """ a snake gets longer when it eats """
            self.lenth = self.legnth + 1

        def starve(self):
            """ a snake shorter when it starves """
            # is there a bug here?
            self.lenth = self.legnth - 1
            


The class object
================

Lets introspect the new type of object::

    >>> from python import Python
    >>> type(Python)
    <class 'type'>
    >>> dir(Python)
    [ ... many methods ... ]


Instances
=========

A class gives us a constructor function to create our snakes. Implicitly it
runs the __init__ function as defined on the class.

Creating::
    
    >>> john = Python('John', 'M', 15, 4)
    >>> jane = Python('Jane', 'F', 4, 6)

Introspecting::

    >>> type(john)
    <class 'python.Python'>
    >>> dir(john)
    [ ... many methods ... ]


Note we get `move`, `starve`, and `eat`  which we defined, but we also get many methods others.

.. tip::

    The other methods are those found when executing `dir(object)`

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

representing snakes
===================

The `__str__` special method is called on an object when we pass it to the `print` function.

We decide that the semantics of printing a python is to show a visual
representation of a snake using characters.

Added to definition in `python.py`::

    class Python():
        
        def __init__(self, name, sex, age, length):
            self.name = name
    [...]

        def __str__(self):
            body = '=' * self.length
            return "{}>".format(body)

results::

    >>> from python import Python
    >>> john = Python('John', 5)
    >>> print(john)
    ~-=====%>

snake equality
==============


Exercises
=========

attack
------

Decide on the semantics of a python attacking another object.

Implement your decision by defining a new method.


__add__
-------

Lets define another special method to exploit the nice syntax python gives us.

Decide on the semantics of 'adding' pythons together.

Implemnent by defining your __add__ method on the Python class.
