import turtle
from turtle import *
import random


def rails():

    pensize(10)
    pencolor("brown")
    amount = random.randint(3, 17)

    for i in range(amount):

        pendown()

        forward(50)
        back(50)

        x = turtle.position()[0]
        y = turtle.position()[1]

        penup()

        left(90)

        forward(25)
        right(90)

    forward(10)

    pendown()

    right(90)

    pencolor("gray")

    pensize(5)

    forward(25 * amount + 25)

    penup()

    left(90)

    forward(30)

    left(90)

    pendown()

    forward(25 * amount + 25)

screen = Screen()


penup()
setx(random.randint(-200, 200))
sety(random.randint(-200, 200))
pendown()

right(random.randint(0, 360))
rails()




screen.mainloop()