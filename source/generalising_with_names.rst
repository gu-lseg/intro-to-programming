Reusability & Abstractions
**************************

Names and functions are great ways to increase the expressivity of
a programmer.


Names & Reusability
===================

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


Functions & Abstractions
========================

With functions our programming expressivity has just taken a leap.

Computers need step by step instructions. Humans however operate at higher
levels of abstraction.

Functions are one way to introduce abstractions. They let you name code for
future execution.

They enable us to no longer think of details.


From shapes to houses
---------------------

You can use the already defined shapes as building blocks for even higher abstractions.

Consider the following.

::

    def house():
        square(100)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        equilateral_triangle(100)
        turtle.right(90)             # return turtle to point of departure
        turtle.forward(100)
        turtle.left(90)



By reusing the code which defined our concepts of a square and triangle we have
defined the concept of a house.

Try your own. Enjoy thinking at a higher level!


Exercises
=========

A house can be a lot more complicated.

Define two functions called window and door.

Tip:

    To more easily compose drawing functions it is best to return the turtle to
    the point of departure and pointing in the same direction. The above house
    function does this with the last three lines of code.

Many Squares with Variables
---------------------------

We will demonstrate the use of variables by revisiting the many squares exercise.

Replace the numbers with variables. 
We should have the following variables: ``rotate_angle``, ``side``, ``right_angle``

Do copy and paste!!

What are the benefits?

- Is the code more readable?

- Easier to update?
