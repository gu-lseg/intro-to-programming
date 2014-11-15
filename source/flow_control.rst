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


Comparison Operators
--------------------

Using introspection which special functions does the following syntax
resolve to:

* `3 > 2`
* `3 < 2`
* `3 <= 2`
* `3 >= 2`
* `3 != 2`


Practicals
==========

Turtles Joypad
--------------

We want to control the movements of the turtle using instructions from the
keyboard. Much like the way you'd control a sprite in a game.

Write this progam in a file. 

You may find this helpful to get started

place this in file called `echo.py`::

    while True:
        user_said = input('\nType something (q to exit): ')
        if user_said == 'q':
            break
        print(user_said)

Paper Sissors Rock
------------------

As a challenge code the paper sissors rock game.

Steps:

1. user inputs either paper, sissors or rock.
2. computer randomly chooses one too.
3. print outcome according to the rules of the game:

   * If user chose 'paper' and computer chose 'rock', then print 'rock wins'
   * if user chose 'sissors' and computer chose 'paper' then print 'sissors
     wins'
   * ... and so on ...
4. Exit

You will need to use some randomness::
    
    >>> import random
    >>> random.choice(['a', 'b', 'c'])
