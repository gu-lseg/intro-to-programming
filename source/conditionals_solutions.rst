Turtles joypad
==============

`turtle_joypad.py`::

    import turtle

    tess = turtle.Turtle()

    while True:

        move = input('Type a w d s for left right up down\nType q to exit\n')

        if move == 'a':
            tess.setheading(180)  # west
            tess.forward(10)
        elif move == 'w':
            tess.setheading(90)   # north
            tess.forward(10)
        elif move == 'd':
            tess.setheading(0)    # west
            tess.forward(10)
        elif move == 's':
            tess.setheading(270)  # south
            tess.forward(10)
        elif move == 'q':
            break


Paper Sissors Rock
==================

`paper_sissors_rock.py`::

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
