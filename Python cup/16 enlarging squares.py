from turtle import *


def square(dlzka):

    for i in range(4):
        forward(dlzka)
        left(90)

    forward(dlzka)


screen = Screen()

for i in range(7):

    square(30 + 10 * i)


screen.mainloop()
