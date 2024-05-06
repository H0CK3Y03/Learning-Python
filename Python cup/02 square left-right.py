from tkinter import *
import time

WIDTH = 1000
HEIGHT = 1000
VELOCITY = 10


window = Tk()
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

square = canvas.create_rectangle(0, 100, 50, 150, fill="blue")

while True:
    coordinates = canvas.coords(square)
    if coordinates[0] + 50 >= canvas.winfo_width() or coordinates[0] < 0:
        VELOCITY = -VELOCITY

    canvas.move(square, VELOCITY, 0)
    window.update()
    time.sleep(0.001)



window.mainloop()