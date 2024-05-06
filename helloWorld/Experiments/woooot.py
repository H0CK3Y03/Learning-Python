import math
import tkinter as tk


def rotate(angle1=0, angle2=0):
    dx = math.cos(angle1) * 200 + 250
    dy = math.sin(angle1) * 200 + 250
    canvas.coords(txt, dx, dy)
    canvas.itemconfig(txt, angle=angle2)
    canvas.after(100, rotate, angle1+0.1, angle2-5.8)

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)

txt = canvas.create_text(250, 50, text='around and around')
rotate()
canvas.pack()
root.mainloop()