from turtle import *
import random


def square():

    fillcolor("blue")

    begin_fill()

    for i in range(4):
        forward(100)
        left(90)

    end_fill()

def triangle():

    fillcolor("red")

    begin_fill()

    for i in range(3):
        forward(100)
        left(120)

    end_fill()


def house():

    square()

    left(90)
    forward(100)
    right(90)

    triangle()


def stairs():

    x = distance(start_x, -400) / 10
    y = distance(-400, start_y) / 10

    for i in range(10):

        left(90)
        forward(y)
        right(90)
        forward(x)




screen = Screen()
screensize(500, 500)

start_x = random.randint(500 // 2, (1000 - 200) // 2)
start_y = random.randint(300 // 2, 500 // 2)

penup()

goto(start_x, start_y)

pendown()

house()

penup()

goto(-400, -400)

pendown()

stairs()


screen.mainloop()
