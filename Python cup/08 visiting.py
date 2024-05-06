from tkinter import *
import random


xVelocity = 10
yVelocity = 10


def move_up(event):
    canvas.move(bug2, 0, -yVelocity)

def move_left(event):
    canvas.move(bug2, -xVelocity, 0)

def move_down(event):
    canvas.move(bug2, 0, yVelocity)

def move_right(event):
    canvas.move(bug2, xVelocity, 0)

def calculate_distance():

    x1, y1 = canvas.coords(bug1)
    x2, y2 = canvas.coords(bug2)

    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    print(distance)

    return distance


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

while True:

    calculate_distance()
    canvas.delete("temp")

    if calculate_distance() < 200:
        canvas.create_text(canvas.coords(bug2)[0], canvas.coords(bug2)[1] + 70, text="Hello Ladybug!", tags="temp")

    window.update()


window.mainloop()
