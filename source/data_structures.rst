Data Structures
***************

Data structures or collections contain other objects. 

They are meant to keep a collection of objects together.

We will look at two: `lists`, `dictionaries`.

It takes some time and practice knowing when to use each.

The functions that interest us are accessing and updating elements of the structures. Also typically collections almost always combine with iteration. Which means going through each of the
members of the collection and effecting some action.

We will leave a more indepth investigation of the various methods to the Koans. Also see the python tutorial: 

https://docs.python.org/2/tutorial/datastructures.html

As always first we explore how to create objects using literals and
constructors, then we examine some functions typical of each object.

Lists
=====

Lists are container objects. They contain ordered items.

creation:: 

    >>> pythons = ['John Cleese', 'Eric Idle', 'Michael Palin', 'Terry Gilliam']
    >>> list(['John Cleese', 'Eric Idle', 'Michael Palin', 'Terry Gilliam'])
    ['John Cleese', 'Eric Idle', 'Michael Palin', 'Terry Gilliam']
    >>> abc = list('abc')              # the list constructor can take a string
    >>> abc
    ['a', 'b', 'c']                    # the result is a list of its characters

introspection::
    
    >>> type(pythons)
    <class 'list'>
    >>> dir(pythons)
    [ ... many methods ... ]

special syntax methods:: 

    >>> abc = ['a', 'b', 'c']
    >>> abc[0]                        # extract elements
    'a'
    >>> abc[2] = 'd'                  # assignment
    >>> abc
    ['a', 'b', 'd']

.. tip::
    Lists are very useful. Only the most trivial programs don't use them.

IndexError
----------

Lists and tuples are zero indexed. The first element is at index 0.

If you ask for an element that doesn't exist you will get an IndexError::

    >>> [][0]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    IndexError: list index out of range


Dictionaries
============

Dictionaries contain key value mappings.

creation::

    >>> {'name': 'Brian', 'age': 23, 'sex': 'M', 'status': 'Single'}  # literal
    {'sex': 'M', 'age': 23, 'status': 'Single', 'name': 'Brian'}
    >>> dict([('name', 'Brian'), ('age', 23), ('sex', 'M'), ('status', 'Single')])  # constructor
    {'sex': 'M', 'age': 23, 'status': 'Single', 'name': 'Brian'}

introspection::

    >>> type(person)
    <class 'dict'>
    >>> dir(person)
    [ ... many methods ... ]

Special syntax for extracting and updating an attribute::

    >>> person['name']
    'Brian'
    >>> person['name'] = 'Naomi'
    >>> person['name']
    'Name'

.. tip::
    Dictionaries are very useful, however their usage overlaps somewhat with Classes
    (more on that later). 

KeyError
--------

If you request a non-existent key you get this error::

    >>> {'a':1}['b']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'b'

Nested
======

Data structures can take any object including other data structures.

Here are some examples.

A list of dictionaries::

    >>> persons = [
            {'name': 'Naomi', 'age': 32, 'sex': 'F', 'status': 'Single'},
            {'name': 'Jane', 'age': 29, 'sex': 'F', 'status': 'Married'},
            {'name': 'Brian', 'age': 23, 'sex': 'M', 'status': 'Single'}
        ]

Nested data structures are extremely common.

Exercises
=========

Koans
-----

Lists::

    > python3 contemplate_koans.py about_lists
    
Dictionaries::
    
    > python3 contemplate_koans.py about_dictionaries

