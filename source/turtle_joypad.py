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

