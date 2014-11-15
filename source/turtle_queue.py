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
