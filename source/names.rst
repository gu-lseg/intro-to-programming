Names
*****

To work effectively with objects we need a way to refer to them. This is called assignemnt.

Names are like the nouns we use in every day speach.

Variables
=========

Naming integer objects::

    >>> x = 5
    >>> four = 4

String object::

    >>> first_name = "greg"

Unlike in maths, the equals symbol means assignment not equality.
Python reads `x = 5` as assign the value (object of type `int`) 5 to the name x.

We can reassign variables to any object::

    >>> x = 5            # x refers to an Integer object
    >>> x = 'greg'       # x refers now to a String object 

A variable by itself is an expression and it evaluates to its object::

    >>> x
    5

NameError
=========

Here we introduce the NameError::

    >>> the_holy_grail
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'the_holy_grail' is not defined
    >>>

Python is telling us it doesn't know what the turtle name refers to. We haven't
defined it. We have forgotten to import it.

Names & Reusability
===================

Names are often called variables. Names give us a lot of expressivity. They enable you to generalise your code facilitating code reuse.

Consider that you write this code to draw a square::

    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)

Now you decide the sides should be of length 100.

Without names you have to go back and replace 50 with 100 four times.

Instead using names you can do this::

    side = 50
    right_angle = 90

    turtle.forward(side)
    turtle.left(right_angle)
    turtle.forward(side)
    turtle.left(right_angle)
    turtle.forward(side)
    turtle.left(right_angle)
    turtle.forward(side)
    turtle.left(right_angle)

Now, if you change your mind you need only update one value.

Note that our programatic definition mirrors the mathematical defintion in
that the lenguth of a square's side is irrelevant to its nature as a square.

Names help in: 

- making programming efficient. 
- capturing meaning. 

.. tip::

    If you find yourself needing to replace many similar values in order
    to update your code, using names is worth considering.


    
Exercises
=========

Shapes
------

Refactor your code in `shapes.py` to use variables as much as possible.

