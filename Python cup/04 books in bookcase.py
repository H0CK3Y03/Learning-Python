from turtle import *
import random


COLORS = ("red", "blue", "green", "yellow", "purple", "pink", "orange", "cyan", "black")

def polica():

    right(90)
    forward(200)
    back(150)

    for i in range(5):
        left(90)
        forward(200)
        back(200)
        right(90)
        forward(50)

    penup()

    left(90)
    forward(200)
    left(90)

    pendown()

    forward(300)

    penup()

    right(90)




def kniha(sirka, vyska, farba):

    global COLOR, COLORS

    fillcolor(farba)

    for i in range(2):

        begin_fill()
        forward(sirka)
        left(90)
        forward(vyska)
        left(90)
        end_fill()

    forward(sirka)

    COLORS.remove(farba)
    COLOR = random.choice(COLORS)


speed(0)

current_shelf_length = 0
max_shelf_length = 0

for z in range(5):

    penup()

    setx(0)
    sety(-50 * z)

    pendown()

    for i in range(random.randint(8, 13)):

        # current_shelf_length =
        length = random.randint(25, 45)
        width = random.randint(10, 15)

        COLORS = ["red", "blue", "green", "yellow", "purple", "pink", "orange", "cyan", "black"]

        COLOR = random.choice(COLORS)

        kniha(width, length, COLOR)

        # max_length


penup()

goto(0, 50)

pendown()

polica()





Screen().mainloop()
