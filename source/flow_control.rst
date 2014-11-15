Conditionals
************

Conditional flow control is how a computer makes decisions.

This how we break out of doing the same thing all the time.

Go to these links and follow the tutorials there. Then come back here and
complete this page.

`bool` objects
==============

The use of True and False has been intuitive up till now. Here we explore them
further.

::
    
    >>> type(True)
    bool
    >>> type(False)
    bool


Boolean Operators
=================

These expression evaluate to `True` or `False` according to the values of x and
y.

::

    x == y           # x equal to y
    x != y           # x not equal to y
    x > y            # x greater than y
    x < y            # x less than y
    x >= y           # x greater than or equal to y
    x <= y           # x less than or equal to y


User input
==========

To capture input from the user we use a function named `input`::

    >>> name = input("Please enter your name: ")
    Please enter your name: 

The interpreter waits for a response.

If the user types in `Sophocles` a string obejct 'Sophocles' is assinged to
name.

if statement
============

We use boolean expressions to make decisions.

:: 

    >>> x = int(input("Please enter an integer: "))
    Please enter an integer: 42
    >>> if x < 0:
    ...     x = 0
    ...     print('Negative changed to zero')
    ... elif x == 0:
    ...     print('Zero')
    ... elif x == 1:
    ...     print('Single')
    ... else:
    ...     print('More')


Exercises
=========

Koans - Control Statements
--------------------------

Truth and Falsehood::

    > python3 contemplate_koans.py about_true_and_false

Boolean operators::

    > python3 contemplate_koans.py about_control_statements


`>` `<` `=<` `=>` `!=` Operators
--------------------------------

Using introspection which special functions does the following syntax
resolve to:

* `3 > 2`
* `3 < 2`
* `3 <= 2`
* `3 >= 2`
* `3 != 2`

Further resources
-----------------

http://opentechschool.github.io/python-beginners/en/conditionals.html

