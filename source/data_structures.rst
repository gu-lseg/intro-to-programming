Data Structures
***************

Data structures or collections contain other objects. 

They are meant to keep a collection of objects together.

Python offers four main ones: `lists`, `dictionaries`, `tuples`, `sets`.

It takes some time and practie knowing when to use each.

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

KeyError
--------

If you request a non-existent key you get this error::

    >>> {'a':1}['b']
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'b'


Tuples
======

Tuples are very similar to lists. Order matters. 

However they are used like lightweight dictionaries: instead of having keys we use 
values in a certain order.

creation::
    
    >>> person = ('Brian', 23, 'M', 'Single')   # literal

introspection::
    
    >>> type(person)
    >>> dir(person)

special syntax methods::

    >>> person[2]
    'M'
    >>> person[2] = 'F'         # Brian has a sex change
    >>> person[2]
    'F'

Tuples have their use but they aren't seen as often as lists and dictionaries.

Sets
====

Sets are collections of unordered and unique elements.

Set definitions are similar to those you find on math sets. Venn diagrams can
be used to explain each one.

creation::
    
    >>> names = {'John Cleese', 'Eric Idle', 'Michael Palin', 'Terry Gilliam'}
    # literal
    >>> set(['John Cleese', 'Eric Idle', 'Michael Palin', 'Terry Gilliam'])
    # constructor
    >>> abc = set('abc')

introspection::

    >>> type(names)
    >>> dir(names)

methods::

    >>> abc, bcd = set('cab'), set('bdc')
    >>> abc.intersection(bcd)
    {'b', 'c'}
    >>> def_ = set('fed')
    >>> abc.intersection(def_)
    set()                             # empty set
    

To understand the methods thing of Venn Diagrams.

Sets have their uses but aren't seen as much as the others.

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


Special Methods
===============

A lot of data structure types share many special methods. This is a design
choice made by the creators of python. 

By giving us identical or similar methods and special syntax the language 
remains consistent and therfore easier to rely on our intuitions.

We will explore two such methods here.

in and  __contains__
---------------------

`__contains__` is the special method for testing membership. 

`x in y` resolves to `y.__contains__(x)`

When the interpreter encounters `'b' in ['a', 'b']` it knows to look for the `__contains__`
function on the object to the right of `in` and pass it the object to the left
of `in` as parameter.

All data structures have the concept of membership defined::

    >>> 'b' in ['a', 'b']
    True
    >>> ['a', 'b'].__contains__('b')
    True
    >>> 'b' in ('a', 'b')
    True
    >>> ('a', 'b').__contains__('b')
    True
    >>> 'b' in {'a': 1, 'b': 2}
    True
    >>> {'a': 1, 'b': 2}.__contains__('b')
    True
    >>> 'b' in {'a', 'b'}
    True
    >>> {'a', 'b'}.__contains__('b')
    True

Any object that implements the `__contains__` function will work
with the `x in <object>` syntax.

for x in y: and  __iter__
-------------------------

`__iter__` is how iteration is implemented in Python. This protocol is a bit more involved
than the previous protocols.

Taking this code::

    >>> number = [1, 2]
    >>> for i in [1, 2]:
    ...     print(i)
    ...
    1
    2

Roughly `for i in iterable` translates to:

1. `__iter__` is called on the iterable object, 
2. an object of type iterator is returned.
3. `__next__` called repeatedly on the iterator which returns an item in the iterable.
4. interpreter actions the code in the for loop
5. Steps 3 and 4 repeat until iterator object runs out of items at which point it throws a `StopIteration` exception.

To illustrate::

    >>> itr_obj = [1, 2].__iter__()
    >>> type(itr_obj)
    <class 'list_iterator'>
    >>> itr_obj.__next__()
    1
    >>> itr_obj.__next__()
    2
    >>> itr_obj.__next__()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

Any object that implements the `__iter__` function will work 
with the `for x in <object>: ...` syntax.


Exercises
=========

Koans
-----

Lists::

    > python3 contemplate_koans.py about_lists
    
Dictionaries::
    
    > python3 contemplate_koans.py about_dictionaries

Tuples::

    > python3 contemplate_koans.py about_tuples

Sets::
    
    > python3 contemplate_koans.py about_sets

len() implementation
--------------------

len() works on many objects which are container like types::

    >>> len('hi')
    2
    >>> len([1, 2])
    2

Which special function is called by the function `len` on the object it is passed?
