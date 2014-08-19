
Solution
--------

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
