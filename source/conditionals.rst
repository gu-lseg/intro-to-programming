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


if and elif
===========

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

while loops
===========

The `while <condition>:` construct is a way of instructing the interpreter to repeat
indefinitely. The condition defines when the loop will terminate.

`break` is a keyword that instructs the interpreter to break out of a loop. 

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

|py-while|

.. |py-while| raw:: html

    <iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=import+random%0Awarm+%3D+20%0Atemperature+%3D+18%0Awhile+temperature+%3C%3D+warm%3A%0A++++print('Its+'+%2B+str(temperature)+%2B+'+degrees.+Wrap+up.')%0A++++temperature+%3D+random.randrange(5,+25)%0A++++%0Aprint('Thats+all+for+now')&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0&codeDivWidth=350&codeDivHeight=400"> </iframe>

.. tip::
    Use while if you don't when you only know a loop will terminate in a given
    condition.

Floats
======

`int` objects have enabled us to represent programs that solve arithemtic for
whole numbers. This is sufficient for problems which deal exclusively with
whole numbers such as age, and days. It is insufficient for numbers that have
a value beyond the decimal point.

`float` objects represent rational numbers, numbers that have a decimal value.

::

    >>> type(3.0)        # literal
    <class 'float'>
    >>> float('3.4')     # constructor can convert from str

All operators we saw defined on `int` work on `float` so it fits quite
naturally with our intuitions.


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

    > python contemplate_koans.py about_true_and_false

    > python contemplate_koans.py about_control_statements

Practical: Shoe Conversion
--------------------------

A UK company wants to export shoes to continental Europe.

It hires you to write a program that prompts the user for a UK size and return
the equivalent size it would be in Europe.

Here is a conversion table:

======  =====
Europe  UK
======  =====
38      5
39      6
40      7
42      8
======  =====

Practical: Turtles Joypad
-------------------------

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
-----------------------------

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
