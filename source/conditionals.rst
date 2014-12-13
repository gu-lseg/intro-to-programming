Conditionals
************

Conditional flow control is how the python interpreter chooses which code to
execute. Think of it as how to express choices.

Boolean expressions are lines of code that resolve to a boolean object. There
are only two values a boolean object can take: True or False.

Conditionals always base their decisions on the result of a boolean expression.

First we look at some boolean expressions, then at two conditonal
statements: `if` and `while`.

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

For `int` objects the meaning of these operators maps to our expectations from math.

if
==

The `if <boolean expression>:` followed by an indented block of code is syntax
that means the interpreter will only execute the block of code if the
expression evaluates to the object True.

::

    >>> person = 'Natalia'
    >>> if person == 'Natalia':
    ...    print('female')
    'female'


We can add multiple conditional branches by using `elif <boolean expression>:`

:: 

    >>> x = input("Enter your age: ")    # input returns a str 
    Enter your age: 24
    >>> x = int(x)                       # convert to an int
    >>> if x < 18:
    ...     print('You are a child')
    ... elif x == 18:
    ...     print('You have just turned into an adult')
    ... else:
    ...     print('You are an adult')

while
=====

The `while <condition>:` construct is a way of instructing the interpreter to repeat
indefinitely. Intuitively `break` is a keyword that instructs the
interpreter to break out of a loop. We will examine this in more detail
later.

A while statement is the `while` keyword followed by a condition. The condition defines when
the loop will terminate.

::
    
    >>> import random
    >>> warm = 20
    >>> temperature = random.randrange(5, 30)
    >>> while temperature <= warm:
    ...    print('cold')
    ...    temperature = random.randrange(5, 30)
    cold
    cold
    cold

.. tip::
    Use while if you don't when you only know a loop will terminate in a given
    condition.


Exercises
=========

Comparison Operators
--------------------

What is the result this line of code?::

    3 < '5'

Practical: Loan 
---------------

A loan repayment plan consists of a balance and monthly interest and
repayments.

The loan amount in question is £100. Repayments are made at £20. Interest is
charged monthly at %10.

Write a program that prints to screen the remaining balance after every month.

Koans - Control Statements
--------------------------

::

    > python3 contemplate_koans.py about_true_and_false

    > python3 contemplate_koans.py about_control_statements


Practical: Turtles Joypad
---------------------------

We want to control the movements of the turtle using instructions from the
keyboard. Much like the way you'd control a character in a game.


Place this in a file called `turtle_joypad.py`::

    import turtle

    tess = turtle.Turtle()

    while True:
        move = input('\nType a w d s for left up right down (q to exit): ')
        if move == 'a':
            tess.setheading(180)  # west
            tess.forward(10)

        # [ ... put your code here ... ]
            
        if move == 'q':
            break


Practical: Paper Sissors Rock
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
