Shapes file
===========

Your ``shapes.py`` file should now look like this:

.. code-block:: python

    from turtle import Turtle

    tess = Turtle()

    def square(side):
        for _ in range(4):
            tess.forward(side)
            tess.left(90)

    def rectangle(width, length):
        for _ in range(2):
            tess.forward(width)
            tess.left(90)
            tess.forward(length)
            tess.left(90)

    def equilateral_triangle(side):
        for _ in range(3):
            tess.forward(side)
            tess.left(180-60)

    def hexagon():
      for _ in range(6):
          tess.forward(100)
          tess.left(60)

    def honeycomb():
        for _ in range (6):
            hexagon()
            tess.forward(100)
            tess.right(60)

    def house(size):
        square(size)
        tess.left(90)
        tess.forward(100)
        tess.right(90)
        equilateral_triangle(100)
        tess.right(90)             # point of departure
        tess.forward(100)
        tess.left(90)

    def any_shape(sides, length):
        for _ in range(sides):
            tess.forward(length)
            tess.right(360 / sides)

`paper_sissors_rock.py`
=======================

.. code-block:: python

    import random

    choices = ['paper', 'sissors', 'rock']
    chosen = random.choice(choices)

    while True:
        msg = 'Type one of following {}: '.format(' '.join(choices))
        usr = input(msg)
        if usr in choices:
            break
        print('Please choose a correct choice')

    print('computer choses: {}'.format(chosen))

    if usr == chosen:
        print('The result is a tie!')

    if usr == 'paper':
        if chosen == 'rock':
            print('paper wins')
        else:
            print('rock wins')

    if usr == 'sissors':
        if chosen == 'paper':
            print('sissors wins')
        else:
            print('rock wins')

    if usr == 'rock':
        if chosen == 'sissors':
            print('rock wins')
        else:
            print('paper wins')


`turtle_queue.py`
=================

.. code-block:: python

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
