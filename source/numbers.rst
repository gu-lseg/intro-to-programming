Numbers
*******

In this and the following section we examine three new types of objects

========  ===========  ============
Type      Used for     Examples
========  ===========  ============
Integers  Numbers      -5    16
Floats    Decimal      3.4  -23.001
Strings   Text         'abc' 'bob'
========  ===========  ============

We will look at how to create objects of these types and how to manipulate
them.


Integers & Floats
=================

`int` objects represent natural numbers. 
`float` objects represent rational numbers, numbers that have a decimal value.
Both types can represent positive or negative numbers.

Creation 
--------

It is easier to create ints and floats than it was to create turtles.

You can just type them out::

    >>> 3              
    3
    >>> type(-5)        # confirm type
    int
    >>> 3.4
    3.4
    >>> type(3.0)
    <class 'float'>

Questions
---------

1. What is the different between an `int` and a `float`?
2. Why do we have two different types to represent numbers?
3. Find some uses cases where you'd choose an `int` and others where
   a `float` is more suitable.

Number Operators
================

.. tip::

    Unlike turtle object methods, we use operators to manipulate number objects.
    This special syntax exists as it maps to our expectations and so
    is more intuitive.

Arithemtic operators
--------------------

Two number objects separated by an arithmetic operator `*` `/` `-` `+`, actions
behaviour we expect from basic arithmentic.

::

    >>> 5 + 4
    9
    >>> 5 - 6
    -1

The behaviour is to compute and return the result as a new number object with the same
type. In the above example `5 + 4` equals the 9 which is of type `int`.

Questions
---------

1. What is the difference between `2 * 5 + 3` and `2 * (5 + 3)`? What are the
   answers of each expression?
2. What happens when you divide `5` by `2`? What about `5` by `2.0`. Is there a
   difference? If so, why?

Comparison operators
--------------------

Likewise two number objects separated by comparison operators `==` `!=`
`>=` `<=` `<` `>`, have the behaviour we expect. 

::

    >>> 5 == 4
    False                # What is this?
    >>> 5 < 6
    True                 # and this?
    >>> 6 <= 6
    True


.. tip::

    `int` objects are used to solve problems that require manipulating numbers
    but with no decimal point such as age, and days, IDs.

These are expressions and these evaluate to `True` or `False`.


The `if` conditional
====================

This pattern::

    if <boolean expression>:
        <block of code>            # Note 4 space indent

mirrors the syntax required to define conditional behaviour.

Typically we use the result of comparison statements to make decisions on what
code to execute.::

    if 6 > 5:
        print('Greater Than')

`if` statements can combine with else::

    if 6 > 5:
        print('Greater Than')
    else:
        print('Not Greater Than')


Questions
---------

1. In an if conditional, what happens if the boolean is true?
2. When does the `else` block of code run in an if else statement?
3. What are some use cases for an if conditional?

Number Exercises
================

1. A bar wants to ensure only adults are allowed in. Write a program in a file named
   `bar.py` that prints 'underaged' or 'ok' depending on the age entered in the code.

2. A ride operator needs to ensure clients are taller than 150cm due to security.
   Write a prgram in a file named `ride.py` that will print 'ok' or 'not tall enough' 
   given a height entered in the code.

3. A trader wants to algorithmically buy 'ACME` corp stock if they rise above
   0.005$ but sell if they are below 0.001$. Write a script `trader.py` that 
   prints 'buy', 'sell', 'hold' depending on a sale price entered in the script.
