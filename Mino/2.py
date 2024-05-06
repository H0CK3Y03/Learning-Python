import tkinter as tk
from math import *

canvas = tk.Canvas(tk.Tk(), width= 1000, height= 1000)
canvas.pack()

def square(size, i):
    canvas.create_rectangle(size, size - i * 20, size + 20 * i, size - i * 20 + 20 * i)

for i in range(20):
    square(1000 - i * 20, i)

canvas.mainloop()
