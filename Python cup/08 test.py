from tkinter import *
import random


xVelocity = 5
yVelocity = 5


def move_up(event):
    canvas.move(bug2, 0, -yVelocity)

def move_left(event):
    canvas.move(bug2, -xVelocity, 0)

def move_down(event):
    canvas.move(bug2, 0, yVelocity)

def move_right(event):
    canvas.move(bug2, xVelocity, 0)


window = Tk()


window.bind("<Up>", move_up)
window.bind("<Left>", move_left)
window.bind("<Down>", move_down)
window.bind("<Right>", move_right)

canvas = Canvas(window, height=1000, width=1000)
canvas.pack()

ladybug = PhotoImage(file="lienka.png")
bug = PhotoImage(file="chrobacik.png")

bug1 = canvas.create_image(random.randint(100, 950), random.randint(50, 900), image=ladybug)
bug2 = canvas.create_image(0 + bug.width(), 1000 - bug.height(), image=bug)

window.mainloop()
