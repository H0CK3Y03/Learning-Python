import random
from tkinter import *


def match(event):

    global objective, xVelocity, yVelocity, coordinates
    xVelocity = random.randint(1, 15)
    yVelocity = random.randint(1, 15)
    objective = canvas.create_image(field.width() / 5 + 10, field.height() / 2, image=ball)
    coordinates = canvas.coords(objective)
    moveBall()


def moveBall():
    global xVelocity, yVelocity, objective, coordinates
    canvas.move(objective, xVelocity, yVelocity)
    coordinates = canvas.coords(objective)
    if coordinates[0] <= 0 or coordinates[0] >= field.width():
        xVelocity *= -1
    if coordinates[1] <= 0 or coordinates[1] >= field.height():
        yVelocity *= -1
    if coordinates[0] >= field.width() - 10 and field.height()/2-40 <= coordinates[1] <= field.height()/2+40:
        canvas.create_text(field.width() / 2, field.height() / 2, text="GOAL!!!", font=("Arial", 48))
        return
    window.after(10, moveBall)


window = Tk()
canvas = Canvas(window)
canvas.pack()

field = PhotoImage(file="ihrisko.png")
ball = PhotoImage(file="lopta.png")

canvas.config(width=field.width(), height=field.height())
print(field.width(), field.height())

canvas.create_image(0, 0, image=field, anchor=NW)

window.bind("<space>", match)




window.mainloop()
