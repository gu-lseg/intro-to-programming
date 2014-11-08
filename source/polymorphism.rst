Polymorphism
************

Polymorphism means that different types respond to the same function.

Polymorphism is very useful as it makes programming more intuitive and
therefore easier.

Polymorphism is a fancy word that just means the same function is
defined on objects of different types. 


Python provides protocols which is polymorphism under the hood. These implement consistent behaviour 
for built in objects of different type.

Protocols
=========

Everything is an object and all actions ultimately mean calling functions defined on objects.

Protocols are polymorphic functions that are embbedded into python. Most
importantly the interpreter is aware of them.

Protocols enable:

* consistency - programmers can rely on intuition
* special syntax - interpreter translates nice syntax to functions on objects.

We will look at two protocols: `__contains__` and `__iter__`

__add__
=======

`x + y` resolves to `x.__add__(y)`

::

    >>> 1 + 2
    3
    >>> one = 1
    >>> one.__add__(2)
    3
    >>> '1' + '2'
    '12'
    >>> '1'.__add__('2')
    '12'


__contains__
============

`__contains__` is the built in protocol for membership. 

`x in y` resolves to `y.__contains__(x)`

When the interpreter encounters `'b' in ['a', 'b']` it knows to look for the `__contains__`
function on the object to the right of `in` and pass it the object to the left
of `in` as parameter.

A list object has that function defined and the interpreter then executes the corresponding code block.


All data structures have the concept of membership defined::

    >>> 'b' in ['a', 'b']
    True
    >>> 'b' in ('a', 'b')
    True
    >>> 'b' in {'a': 1, 'b': 2}
    True
    >>> 'b' in {'a', 'b'}
    True

Demonstrating `__contains__`::

    >>> ['a', 'b'].__contains__('b')
    True
    >>> ('a', 'b').__contains__('b')
    True
    >>> {'a': 1, 'b': 2}.__contains__('b')
    True
    >>> {'a', 'b'}.__contains__('b')
    True


__iter__
========

In this section we are going to see how iteration is implemented in Python.

This code::

    >>> for i in [1, 2]:
    ...     print(i)
    ...
    1
    2



Exercise
========

Boolean Operators
-----------------

Using introspection functions, which protocol functions do the following syntax
resolve to:

* `3 > 2`
* `3 < 2`
* `3 <= 2`
* `3 >= 2`

String representations
----------------------

What function gets called when we get results in the interpreter?
Is it the same that gets called when we type `print(x)`?
