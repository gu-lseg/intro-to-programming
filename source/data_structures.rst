Data Structures
***************

Data structures or collections contain other objects. 

They are meant to keep a collection of objects together.

Python offers four main ones: `lists`, `dictionaries`, `tuples`, `sets`.

It takes some time and practie knowing when to use each.

The functions that interest us are accessing and updating elements of the structures. Also typically collections almost always combine with iteration. Which means going through each of the
members of the collection and effecting some action.

See the python tutorial for a more indepth treatment:

https://docs.python.org/2/tutorial/datastructures.html

As usual we will look first how to create the objects using literals and
constructors, and then examine some functions typical of each object.

Lists
=====

Lists are container objects

creation:: 

    >>> ['John Cleese', 'Eric Idle', 'Michael Palin', 'Terry Gilliam']
    >>> list(['John Cleese', 'Eric Idle', 'Michael Palin', 'Terry Gilliam'])

functions::

    >>> abc = ['a', 'b', 'c']
    >>> abc[0]                        # extract elements
    'a'

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

example::

    >>> person = {'name': 'Brian', 'age': 23, 'sex': 'M', 'status': 'Single'}

KeyError
--------

If you request a non-existent key you get this error::

    >>> {'a':1}['b']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'b'


Tuples
======

Tuples can be used like lightweight dictionaries. Instead of having keys we use 
values in a certain order.

example::
    
    >>> person = ('Brian', 23, 'M', 'Single')



Sets
====

Sets are collections of unordered and unique elements.

Set definitions are similar to those you find on math sets. Venn diagrams can
be used to explain each one.

creation::
    
    >>> {'John Cleese', 'Eric Idle', 'Michael Palin', 'Terry Gilliam'}
    >>> set(['John Cleese', 'Eric Idle', 'Michael Palin', 'Terry Gilliam'])


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

A list of tuples::

    >>> persons = [
            ('Naomi', 32, 'F', 'Single'),
            ('Jane',  29, 'F', 'Married'),
            ('Brian', 23, 'M', 'Single')
        ]

