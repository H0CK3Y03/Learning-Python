from tkinter import *
from math import *


def hviezda(x, y):

    canvas.create_polygon(x, y, x + 20, y, x + 20 - 10, y - 20, fill="yellow")
    canvas.create_polygon(x, y - 12, x + 20, y - 12, x + 20 - 10, y - 12 + 20, fill="yellow")


window = Tk()
canvas = Canvas(window, height=1000, width=1000)
canvas.pack()

canvas.create_rectangle(50, 50, 50 * 12, 50 * 8, fill="blue")

for i in range(12):

    hviezda((50 * 12 // 2) + 80 * cos(radians(i * 30)), (50 * 8 // 6 * 3 + 20) + 80 * sin(radians(i * 30)))

window.mainloop()
