import tkinter
from math import cos, sin, radians

canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()

# x = 0
# for i in range(3):
#     canvas.create_text(180, 120, text="ŤAHAŤ", font='Arial 50', fill='blue', angle=x)
#     x = x + 120
# uloha 27/7

# x = 500
# y = 500
# r = 80
# z = 0
# for i in range(1, 7):
#     x1 = x + r * cos(radians(i * 60))
#     y1 = y + r * sin(radians(i * 60))
#     z = z - 60
#     canvas.create_text(x1, y1, text="Python", font='Arial 30', fill='black', angle=z)
# uloha 27/8

x = 200
y = 250

for i in range(5):
    canvas.create_line(x, y, x + 50, y)
    x += 50
    canvas.create_line(x, y, x, y + 50)
    y += 50

canvas.create_line(x, y, x + 100, y)
x += 100

for i in range(5):
    canvas.create_line(x, y, x, y - 50)
    x += 50
    y -= 50
    canvas.create_line(x - 50, y, x, y)
# uloha 27/9

canvas.mainloop()
