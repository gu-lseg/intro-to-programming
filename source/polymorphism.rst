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

When we introspect an object we have a lot of attributes that take this format:
`__names__`. This section will make many of those clear.

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

Any object that implements the `__add__` function will work
with the `<object> + x` syntax.

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

Any object that implements the `__contains__` function will work
with the `x in <object>` syntax.

__iter__
========

`__iter__` is how iteration is implemented in Python. This protocol is a bit more involved
than the previous protocols.

Taking this code::

    >>> number = [1, 2]
    >>> for i in [1, 2]:
    ...     print(i)
    ...
    1
    2

Roughly here is the sequence of events:
* interpreter calls `__iter__` on the list object, 
* an object of type iterator is returned.
* interpreter then calls `__next__` repeatedly on the iterator
* interpreter actions the code in the for loop
* interpreter interrupts the loop if a `StopIteration` Exception occurs.

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

len() implementation
--------------------

len() works on many object types::

    >>> len('hi')
    2
    >>> len([1, 2])
    2

Which protocol function is called by the function `len` on the object it is passed?
