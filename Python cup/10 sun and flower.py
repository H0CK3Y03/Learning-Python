from turtle import *


def kresli(pocet, dlzka, hrubka, farba):
    pencolor(farba)
    pensize(hrubka)
    fillcolor("yellow")
    current_angle = 0

    begin_fill()
    for i in range(1,361):
        forward(1)
        right(1)
        current_angle += 1
        if current_angle == (360//pocet):
            left(90)
            forward(dlzka)
            back(dlzka)
            right(90)
            current_angle = 0
    end_fill()


screen = Screen()

screen.bgcolor("cyan")

kresli(6, 30, 50, 'red')
kresli(30, 100, 2, 'yellow')

speed(0)

screen.mainloop()
