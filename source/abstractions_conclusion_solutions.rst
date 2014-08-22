
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

    def house(size):
        square(size)
        turtle.left(90)
        turtle.forward(100)
        turtle.right(90)
        equilateral_triangle(100)
        turtle.right(90)             # point of departure
        turtle.forward(100)
        turtle.left(90)
