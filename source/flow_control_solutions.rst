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
