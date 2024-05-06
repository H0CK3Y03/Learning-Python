import tkinter


canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()

def slnko(x,y):
    canvas.create_oval(x + 100, y + 100, x + 175, y + 175, fill='Yellow')
    canvas.create_line(x + 140, y + 100, x + 145, y + 50)
    canvas.create_line(x + 113, y + 110, x + 80, y + 60)
    canvas.create_line(x + 170, y + 120, x + 210, y + 80)
    canvas.create_line(x + 175, y + 145, x + 230, y + 157)
    canvas.create_line(x + 160, y + 167, x + 200, y + 210)
    canvas.create_line(x + 135, y + 175, x + 130, y + 227)
    canvas.create_line(x + 107, y + 160, x + 60, y + 200)
    canvas.create_line(x + 100, y + 135, x + 45, y + 130)

slnko(0,0)

canvas.mainloop()