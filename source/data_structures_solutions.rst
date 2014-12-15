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

    import turtle

    number_of_turtles = 4

    turtles = []
    for _ in range(number_of_turtles):
        turtles.append(turtle.Turtle())


    def square(turtle_, side):
        for i in range(4):
            turtle_.forward(side)
            turtle_.left(90)

    # position point of origin at bottom left of window
    turtle.setworldcoordinates(0, 0, 600, 600)

    for i, turtle_ in enumerate(turtles):
        turtle_.up()

    # Evenly space out the turtles
    for i, turtle_ in enumerate(turtles):
        ypos = 600 / number_of_turtles * i
        turtle_.setpos(0, ypos)

    for i, turtle_ in enumerate(turtles):
        turtle_.down()


    def draw_squares():
        """ for each turtle draws a series of 3 squares """
        for i, turtle_ in enumerate(turtles):
            for _ in range(3):
                square(turtle_, 100)
                turtle_.up()
                turtle_.forward(200)
                turtle_.down()
