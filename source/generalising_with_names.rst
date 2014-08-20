Varying with Names
******************

Variablity
==========

Names are often called variables. The word `variable` captures an important
aspect of how they serve in programming.

Names give us a lot of expressivity. They enable you to generalise your code.

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

Also our programatic definition mirrors more the mathematical defintion in
that the lenguth of a square's side is irrelevant to its nature as a square.

So names help you:

- program efficiently.
- capture meaning. 

Tip:

    When you find yourself needing to replace many similar values in order
    to update your code, using names is worth considering.

Exercises
=========

Many Squares with Variables
---------------------------

We will demonstrate the use of variables by revisiting the many squares exercise.

Replace the numbers with variables. 
We should have the following variables: ``rotate_angle``, ``side``, ``right_angle``

Do copy and paste!!

What are the benefits?

- Is the code more readable?

- Easier to update?

