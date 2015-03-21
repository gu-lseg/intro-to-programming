Text & Numbers
**************

In this section we examine three new types of objects

========  ===========  ============
Type      Used for     Examples
========  ===========  ============
Integers  Numbers      -5    16
Floats    Decimal      3.4  -23.001
Strings   Text         'abc' 'bob'
========  ===========  ============

We will look at how to create objects of these types and what operators 
(behaviours) they respond to.


Integers & Floats
=================

`int` objects represent natural numbers. 
`float` objects represent rational numbers, numbers that have a decimal value.
Both types can represent positive or negative numbers.

Creation 
--------

Unlike creating turtles there is no formality to creating an `int` and `float`
objects.

You just type them as literals::

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

Why do we have two different types to represent numbers?

Find some practical uses cases where you'd choose an `int` and others where
a `float` is more suitable.

Operators & numbers
===================

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

The behaviour is to compute and return the result as a new object with the same
type.

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

Find some practical uses cases where you'd use the if conditional.

Number Exercises
================

1. A bar wants to ensure only adults are allowed in. Write a program that prints
'underaged' or 'ok' depending on the age entered in the code.

2. A ride operator needs to ensure clients are taller than 150cm due to security.
Write a prgram that will print 'ok' or 'not tall enough' given a height entered
in the code.

3. A trader wants to algorithmically buy 'ACME` corp stock if they rise above
0.005$ but sell if they are below 0.001$. Write a script that prints 'buy',
'sell', 'hold' depending on a sale price entered in the script.


Strings 
=======

Text is reprsented and manipulated using objects instances of type `str`.

Creation
--------
::

    >>> "hi"        
    hi
    >>> type('hi')     # confirm type
    str

When you execute the code `"hi"` or `str("hi")`, the python interpreter:

1. Creates an object of type `str`
2. Gives it the value "hi"
3. Returns this newly created object

Methods
-------

Many! Consult the online documentation: |string_methods|

.. |string_methods| raw:: html

    <a href="https://docs.python.org/3.4/library/stdtypes.html#string-methods" target="_blank">https://docs.python.org/3.4/library/stdtypes.html#string-methods</a>

Questions
---------

Find some practical uses cases of where you'd need to manipulate text.

Using the above documentation and the interpreter interactively try to map
those use cases to actual code solutions.

Try to imagine use cases for each of the methods that exist on
`str` objects in the docs.

Conversion functions
--------------------

Often we need to convert between numbers and text. (Can you think why?)

You can use the `int` and `float` functions to convert `str` objects into number objects::

    >>> int('3')
    3
    >>> float('3.4')     # constructor can convert from str
    3.4
    >>> str(3)
    '3'                  # note the ''s that indicate a str object
    >>> str(3.4)
    '3.4'

User Input
==========

To make programs interactive use a function named `input`::

    >>> name = input("Please enter your name: ")
    Please enter your name: 

When the interpreter meets `input` it:

1. prints the string message passed as an argument to `input`,
2. Buffers (stores) any characters typed
3. On the enter returns the characters as a new String.

Here the resultant string is assigned to the name `name`.

So if the user types in `Sophocles` then enter, a string obejct of value
'Sophocles' is assinged to name.


Text Exercises
==============

1. Rewwrite the number programs to take input from the user. Think of an
appropriate question to print to screen to solicit a correct response.

What if the user enters nonsense? There is rarely a program without some form
of validation.

2. A sign up form on a website for the company 'Very Big Corp. Of America' requires 
information from its clients.

3.1 Write a program that asks clients their name, address, and gender. Ensure that
gender is represented as either 'm', 'f'. If it is not ask the user again.

3.2 The same program now requires people to enter their email address. Add this
but ensure it is well formed. You will need to define what a well formed email address is.

4. A mobile phone company bills clients on a certain plan differently depending on 
whether they have dialed a number containing 0845 or not. Write a program that
asks the user which number they'd like to dial and answers whether it is 'free'
or 'paid'.

5. A geneticist needs your help identifying if a dna sequence exists in a larger
strand of dna. A DNA sequence consists of a sequence of A, T, G, and Cs. Write
a program that takes a DNA sequence from the user and confirms 'Found' or 'Not
Found' depending on whether the input is contained in the target DNA strand.

DNA strand: ATTGCGCCTTATGCTTAACC

As a challenge extend this program to check that the input is correct.

Objects & Types Q&A
===================

If you understand the answers to these you understand everything about objects and types!!

.. tip::
    Use the interpreter to help you find answers


Describe in detail what the interpreter does when you type the following and
enter:: 

    >>> '5'

    >>> 5

What is the result this line of code?::

    3 < '5'


Instances of both `str` and `int` objects recognise the `+` symbol. What output would you expect of the following lines of code?

::

    '1' + '2'

    1 + 2


Try the same above but this time using `*` instead of `+`. What can you
conclude of the meaning of `*`?



Koans
-----

The koans use the keyword `assert` a lot. When you assert something you are stating
that it must be true.

In python true and false are represented by the keywords True and False.

`assert` passes silently when it is followed by True but throws an Error when followed by False::

    >>> assert True
    >>> assert False
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AssertionError
    >>>

In the Koans you have to find answers that evaluate to True for the `assert` to
pass.

Using your intuition try to complete the about_asserts koans.

Visit the appendix on windows for getting started.

::

    C:\Users\greg-lo> python3 contemplate_koans.py about_asserts

.. tip::

    Try copying small lines of code into the python interpreter to experiment 
    interactively with the code. Do this whenever you are stuck.


Run these to explore `int` objects:: 

    python contemplate_koans.py about_integers


Methods that exist on string objects facilitate working with text. We will
explore these by running the koans::

    python contemplate_koans.py about_strings
