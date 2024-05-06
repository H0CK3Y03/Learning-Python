import tkinter as tk
from math import *

canvas = tk.Canvas(tk.Tk(), width= 1000, height= 1000)
canvas.pack()

def square(size, i):
    canvas.create_polygon(size + i * 6, size + i * 6, size - i * 6, size + i * 6, size - i * 6, size - i * 6, size + i * 6, size - i * 6)

for i in range(60): # we need to rotate the square by 6 degrees each time

    square(500 - i * 20, i)

canvas.mainloop()
