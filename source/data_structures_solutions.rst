Shapes file
===========

Your ``shapes.py`` file should now look like this:

::

    import turtle


    def square(side):
        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)

    def rectangle(width, length):
        for _ in range(2):
            turtle.forward(width)
            turtle.left(90)
            turtle.forward(length)
            turtle.left(90)

    def equilateral_triangle(side):
        for _ in range(3):
            turtle.forward(side)
            turtle.left(180-60)
        
    def hexagon():
      for _ in range(6):
          turtle.forward(100)
          turtle.left(60)

    def honeycomb():
        for _ in range (6):
            hexagon()
            turtle.forward(100)
            turtle.right(60)

    def house(size):
        square(size)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        equilateral_triangle(100)
        turtle.right(90)             # point of departure
        turtle.forward(100)
        turtle.left(90)

    def any_shape(sides, length):
        for _ in range(sides):
            turtle.forward(length)
            turtle.right(360 / sides)


Turtle Loops
============

`turtle_queue.py`::

    from turtle import Turtle, exitonclick, setworldcoordinates

    number_of_turtles = 4

    # Make some turtles:
    turtles = []
    for _ in range(number_of_turtles):
        turtles.append(Turtle())

    # position point of origin at bottom left of window
    setworldcoordinates(0, 0, 600, 600)

    def ready_the_turtles():

        for turtle in turtles:
            turtle.up()

        # Evenly space out the turtles
        for i, turtle in enumerate(turtles):
            ypos = 600 / number_of_turtles * i
            turtle.setpos(0, ypos)

        for i, turtle in enumerate(turtles):
            turtle.down()

    def square(turtle, side):
        for i in range(4):
            turtle.forward(side)
            turtle.left(90)

    def draw_squares():
        """ for each turtle draws a series of 3 squares """
        for turtle in turtles:
            for _ in range(3):
                square(turtle, 100)
                turtle.up()
                turtle.forward(200)
                turtle.down()

    ready_the_turtles()
    draw_squares()

    exitonclick()
