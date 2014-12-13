Loan
====
::
    In [124]: while balance > 0:
        compound_interest = 0.1 * balance
        print('balance: ' + str(balance))
        balance = balance + compound_interest - 20
       .....:
    balance: 100.0
    balance: 90.0
    balance: 79.0
    balance: 66.9
    balance: 53.59
    balance: 38.949000000000005
    balance: 22.843900000000005
    balance: 5.128290000000007

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
