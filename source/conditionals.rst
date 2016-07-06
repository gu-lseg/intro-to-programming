Conditionals
************

Conditional flow control is how the python interpreter chooses which code to
execute. Think of it as how to express choices. Conditionals are a very powerful
part of programming as it means that you can get your program to carry out different
behaviour depending on input rather than having your program do the same thing
every time it runs.

Boolean expressions are lines of code that resolve to a boolean object. There
are only two values a boolean object can take: True or False.

Conditionals always base their decisions on the result of a boolean expression.
They are always followed by a block of code.


Furthermore conditional loops enable us to harness logic relating to repetition.


Code Blocks
===========

A block of code is code that will execute together. In Python a block is defined by the
use of indentation.

All types of conditionals use code blocks which are executed depending on the
outcome of the conditional expression that guards their execution.

.. code-block:: python

    a = 4
    if a == 4:
        print('This code block will execute')
        result = 5 + a
    else:
        print('This code block will not execute')
        result = a + 6


.. tip::

    In other languages code blocks are defined by the use of braces `{}`s

Questions
-------
1. Can you change the code above to make the `else` block execute?

Equality
========

Testing the equality of two objects returns `True` or `False` depending on how
equality is defined on those two objects.

Equality on strings is defined as follows:

.. code-block:: python

    >>> '5' == '5'
    True
    >>> '5' == '6'
    False

Generally the objects have to first be of the same type and then have the same
value to be equal:

.. code-block:: python

    >>> 5 == '5'
    False

Questions
-------
1. Write some equality statements of your own

2. Instead of == you can also use `!=` `<=` `<` `>=` or `>`. Write some equality statements using these
and if you're not sure what they do see if you can work it out from whether you get a `True`
or `False` response.

The `while` loop
================

The `while <condition>:` construct is a way of instructing the interpreter to repeat
indefinitely. The condition defines when the loop will terminate.

syntax
------

::

    while <condition>:   # condition must evaluate to a boolean
        <code block>     # the indent defines the loop's code block

example
-------

.. code-block:: python

    >>> import random
    >>> warm = 20
    >>> temperature = random.randrange(5, 30)
    >>> while temperature <= warm:
    ...    print('cold')
    ...    temperature = random.randrange(5, 30)
    cold
    cold
    cold

Questions
-------
1. What do you think ``random.randrange(5, 30)`` does?

visualising execution
---------------------

|py-while|

.. |py-while| raw:: html

    <iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=import+random%0Awarm+%3D+20%0Atemperature+%3D+18%0Awhile+temperature+%3C%3D+warm%3A%0A++++print('Its+'+%2B+str(temperature)+%2B+'+degrees.+Wrap+up.')%0A++++temperature+%3D+random.randrange(5,+25)%0A++++%0Aprint('Thats+all+for+now')&origin=opt-frontend.js&cumulative=false&heapPrimitives=false&drawParentPointers=false&textReferences=false&showOnlyOutputs=false&py=3&rawInputLstJSON=%5B%5D&curInstr=0&codeDivWidth=350&codeDivHeight=400"> </iframe>

.. tip::
    A while loop is used to repeatedly execute an instruction until a condition
    is no longer true. You should make sure that the condition will eventually be
    false otherwise your program will run forever. If you do end up writing a loop like
    this use ``ctrl + c`` to terminate your program.

loop keywords
-------------

`break` is a keyword that instructs the interpreter to break out of a loop.
`continue` instructs the interpreter to skip the rest of the loop code block
and continue with the next loop.


Practicals
==========

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

Extension: Can you return an error message for the user if they enter an invalid shoe size.

Practical: Loan
---------------

A loan repayment plan consists of a balance and monthly interest and
repayments.

The loan amount in question is £100. Repayments are made at £20. Interest is
charged monthly at %10.

Write a program that prints to screen the remaining balance after every month.

The program should terminate when the loan is completely paid off.

Practical: BMI Calculator
-------------------------

The NHS has hired you to create a BMI Calculator.

Write a command line program that asks a user for:

* Weight in Kilograms
* Height in Meters

Return the bmi result, followed by the users' BMI classification.

BMI Classification

.. tip::

    You will have to do some research online for how to calculate a persons
    bmi.

    Try working the maths out on paper first before you write the code.

=============   =================
BMI             Classification
=============   =================
18.5 or less	Underweight
18.5 to 24.99	Normal Weight
25 to 29.99	Overweight
30 to 34.99	Obesity (Class 1)
35 to 39.99	Obesity (Class 2)
40 or greater	Morbid Obesity
=============   =================

Practical: Turtles Joypad
-------------------------

We want to control the movements of the turtle using instructions from the
keyboard. Much like the way you'd control a character in a game.

Place this in a file called `turtle_joypad.py`:

.. code-block:: python

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
