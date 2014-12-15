Shapes file
===========

Your ``shapes.py`` file should now look like this:

::

    import turtle


    def square(side):
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)


    def rectangle(side):
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)


    def equilateral_triangle(side):
        turtle.forward(side)
        turtle.left(180-60)
        turtle.forward(side)
        turtle.left(180-60)
        turtle.forward(side)
        turtle.left(180-60)


    def house(size):
        square(size)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        equilateral_triangle(100)
        turtle.right(90)             # return to point of departure
        turtle.forward(100)
        turtle.left(90)
