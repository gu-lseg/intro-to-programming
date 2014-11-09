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
            

Paper Sissors Rock
==================

::

    import random

    choices = ['paper', 'sissors', 'rock']

    while True:
        msg = 'Type one of following {}: '.format(' '.join(choices))
        usr = raw_input(msg)
        if usr in choices:
            break
        print 'Please choose a correct choice'

    index = random.randint(0, 2)
    computer = choices[index]

    print 'computer choses: {}'.format(computer)

    if usr == computer:
        print 'The result is a tie!'

    if usr == 'paper':
        if computer == 'rock':
            print 'paper wins'
        else:
            print 'rock wins'

    if usr == 'sissors':
        if computer == 'paper':
            print 'sissors wins'
        else:
            print 'rock wins'

    if usr == 'rock':
        if computer == 'sissors':
            print 'rock wins'
        else:
            print 'paper wins'
