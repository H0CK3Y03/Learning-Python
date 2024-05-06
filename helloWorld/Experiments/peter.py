import tkinter
from math import cos, sin, radians

canvas = tkinter.Canvas(bg='white', width=700, height=700)
canvas.pack()

# canvas.create_line(120, 20, 220, 200, 20, 200, 120, 20, fill='blue')
# canvas.create_line(240, 20, 340, 200, 140, 200, 240, 20, fill='red')
# 9/3

# y = 40
# for i in range(10):
#     canvas.create_rectangle(100, y, 200, y+20)
#     y += 40
# 26/5

# x = 10
# y = 10

# for i in range(10):
#     canvas.create_line(x, y, x + 50, y + 50, x, y + 100, x + 100, y)
#     x += 50
# for i in range(10):
#     canvas.create_line(x, y, x + 50, y + 50, x, y + 100, x + 100, y, x + 50, y + 50, x + 100, y + 100)
#     x += 50
# for i in range(10):
#     canvas.create_line(x, y, x + 50, y + 50, x, y + 100)
#     canvas.create_line(x + 100, y, x + 50, y + 50, x + 100, y + 100)
#     x += 100
# for i in range(10):
#     canvas.create_line(x, y, x + 50, y + 50, x, y + 100)
#     canvas.create_line(x + 100, y, x + 50, y + 50, x + 100, y + 100)
#     x += 150
#  28/13

# canvas.create_line(100,110,60,150, width=15)
# canvas.create_line(160,110,210,150, width=15)


# canvas.create_rectangle(100, 100, 200, 200)
# canvas.create_oval(100, 100, 200, 200)

# canvas.create_text(100, 100, text='Python', font='Arial 30', angle= 180)
# canvas.create_text(170, 30, text='Python', font='Arial 30', angle= 90)
# canvas.create_text(240, 100, text='Python', font='Arial 30', angle= 0)
# canvas.create_text(170, 170, text='Python', font='Arial 30', angle= 270)
#
# canvas.create_rectangle(40, 85, 160, 115)
# canvas.create_rectangle(180, 85, 300, 115)
# canvas.create_rectangle(400, 400, 520, 430)
# canvas.create_rectangle(400, 400, 520, 430)
#
#
# canvas.create_rectangle(400, 400, 520, 430)
# canvas.create_text(460, 415, text='Python', font='Arial 30', angle= 0) #font=30 -> height of characters, width of characters -> font*2/3 -> 30*2/3 ->20

# canvas.create_text(200, 200, text='Python', font="Arial 20", angle=180)
# canvas.create_text(200, 200, text='Python', font="Arial 20", angle=120)

x = 500
y = 500
r = 80
z = 0
for i in range(1, 7):
    x1 = x + r * cos(radians(i * 60))
    y1 = y + r * sin(radians(i * 60))
    z = z - 60
    canvas.create_text(x1, y1, text="Python", font='Arial 30', fill='black', angle=z)


canvas.mainloop()