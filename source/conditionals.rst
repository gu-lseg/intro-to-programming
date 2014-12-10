Flow 1: Conditionals
********************

Conditional flow control is how the python interpreter chooses which code to
execute. Think of it as how to express choices.


Equality
========

Testing the equality of two objects returns `True` or `False` depending on how
equality is defined on those two objects.

Equality on stings is defined as follows::

    >>> '5' == '5'
    True
    >>> '5' == '6'
    False

Generally the objects have to first be of the same type and then have the same
value to be equal::

    >>> 5 == '5'
    False

bools 
-----

::
    
    >>> type(True)
    bool
    >>> type(False)
    bool

Comparison Operators
====================

These expressions evaluate to a boolean (`True` or `False`) according to the
values of x and y.

::

    x == y           # x equal to y
    x != y           # x not equal to y
    x > y            # x greater than y
    x < y            # x less than y
    x >= y           # x greater than or equal to y
    x <= y           # x less than or equal to y



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


Practical 1: Turtles Joypad
---------------------------

We want to control the movements of the turtle using instructions from the
keyboard. Much like the way you'd control a sprite in a game.


place this in file called `turtle_joypad.py`::

    import turtle

    tess = turtle.Turtle()

    while True:
        move = input('\nType a w d s for left up right down (q to exit): ')
        if move == 'a':
            tess.setheading(180)  # west
            tess.forward(10)

        [ ... put your code here ... ]
            
        if move == 'q':
            break

Practical 2: Paper Sissors Rock
-------------------------------

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
