from turtle import *
import random


def broom(length_of_handle, number_of_fibers, length_of_fiber):

    forward(length_of_handle)

    left(180 / number_of_fibers * number_of_fibers / 2)

    for i in range(number_of_fibers):

        forward(length_of_fiber)
        back(length_of_fiber)
        right(180 / (number_of_fibers - 1))  # -1 because when we turn left we make a fiber already so 1 is already done when we get to this point

    left(180 / number_of_fibers * number_of_fibers / 2 + 180 / (number_of_fibers - 1)) # + 180 / (number_of_fibers - 1) because at the end the turtle turns right by this amount but doesn't draw anything
    back(length_of_handle)



screen = Screen()
screen.screensize(1000, 1000)

speed(3)

right(random.randint(0, 360))

for i in range(random.randint(1, 10)):

    penup()

    setx(random.randint(-300, 300))
    sety(random.randint(-300, 300))

    pendown()

    broom(random.randint(50, 200), random.randint(3, 20), random.randint(20, 80))


screen.mainloop()
