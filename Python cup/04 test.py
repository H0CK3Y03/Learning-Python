from turtle import *
import random


COLORS = ["cyan", "black", "red", "green", "yellow"]

def polica():

    right(90)
    forward(50)

    for i in range(5):

        left(90)
        forward(max_shelf_width + 20)
        back(max_shelf_width + 20)
        right(90)
        forward(50)

    penup()

    left(90)
    forward(max_shelf_width + 20)
    left(90)

    pendown()

    forward(300)

    penup()

    right(90)




def kniha(sirka, vyska, farby):

    begin_fill()

    for u in range(2):

        fillcolor(farby[u % len(farby)])

        forward(sirka)
        left(90)
        forward(vyska)
        left(90)

    end_fill()

    forward(sirka)

    farby.append(farby.pop(0))





speed(0)

current_shelf_width = 0
max_shelf_width = 0


for z in range(5):

    penup()

    setx(0)
    sety(-50 * z)

    pendown()

    current_shelf_width = 0

    for i in range(random.randint(8, 13)):

        length = random.randint(25, 45)
        width = random.randint(10, 15)

        current_shelf_width += width

        COLOR = random.choice(COLORS)

        removed_color = COLOR

        kniha(width, length, COLORS)

        if max_shelf_width < current_shelf_width:

            max_shelf_width = current_shelf_width


penup()

goto(-10, 50)

pendown()

polica()

Screen().mainloop()
