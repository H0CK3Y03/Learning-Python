from turtle import *


def square():
    for i in range(4):
        forward(300)
        left(90)


def triangle():

    for i in range(3):
        forward(50)
        left(120)


def semicircle():

    right(60)

    for i in range(120):

        forward(1)
        left(1)

def face():

    square()

    penup()

    setx(50)
    sety(200)

    pendown()

    triangle()

    penup()

    forward(150)

    pendown()

    triangle()

    penup()

    back(50)

    left(90)

    forward(50)

    right(180)

    pendown()

    forward(100)

    left(90)

    penup()

    goto(100, 100)

    pendown()

    semicircle()


screen = Screen()

face()

screen.mainloop()