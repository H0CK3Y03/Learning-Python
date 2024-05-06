from tkinter import *
import random


SIZE = 100
x = random.randint(100, 900)
y = random.randint(100, 900)

window = Tk()
canvas = Canvas(window, height=1000, width=1000)
canvas.pack()


if y + (SIZE / 2) < 500:

    color = "blue"

elif y + (SIZE / 2) > 500:

    color = "green"

else:

    color = "#008080"


ball = canvas.create_oval(x, y, x + SIZE, y + SIZE, fill=color)
print(canvas.coords(ball))


window.mainloop()
