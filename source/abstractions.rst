Abstractions with Functions
***************************

With functions our programming expressivity has just taken a leap.

Computers need step by step instructions. Humans however operate at higher
levels of abstraction.

Functions are one way to introduce abstractions. They let you name code for
future execution.

They enable us to no longer think of details.


From shapes to houses
=====================

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


Exercise
========

A house can be a lot more complicated.

Define two functions called window and door.

Tip:

    To more easily compose drawing functions it is best to return the turtle to
    the point of departure and pointing in the same direction. The above house
    function does this with the last three lines of code.

