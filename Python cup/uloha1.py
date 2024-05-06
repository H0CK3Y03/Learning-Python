from turtle import *
import random


def obdlznik(a, b):

    for i in range(2):

        left(90)

        forward(b)

        left(90)

        forward(a)



def slnko(n, strana, luc):

    global x, y

    for i in range(n):

        forward(strana)

        obdlznik(strana, luc)

        right(360 / n)


screen = Screen()

x = random.randint(-350, 300)
y = random.randint(100, 220)
n = random.randint(5, 15)
strana = random.randint(10, 20)
luc = random.randint(30, 80)

penup()

goto(x, y)

pendown()

slnko(n, strana, luc)


screen.mainloop()
