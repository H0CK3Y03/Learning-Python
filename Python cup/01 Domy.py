import turtle
from turtle import *


def stvorec(d):
    for i in range(4):
        fd(d)
        rt(90)


def trojuh(strana):
    for i in range(3):
        fd(strana)
        lt(120)


def dom(velkost):
    stvorec(velkost)
    trojuh(velkost)


def domy9(velkost):
    for i in range(9):
        dom(velkost)
        fd(velkost)


# dom(50)
speed(0)
domy9(30)

Screen().mainloop()