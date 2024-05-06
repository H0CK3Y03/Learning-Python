import tkinter

canvas = tkinter.Canvas(width=1000, height=1000)
canvas.pack()

z = 50
x = 100
y = 100
txt = 'Python'
canvas.create_text(x, y, text=txt, font=f'Arial {z}', angle= 180)
canvas.create_text(x + (z*2/3) * len(txt)/2, y - (z*2/3) * len(txt)/2, text=txt, font=f'Arial {z}', angle= 90)
# canvas.create_text(240, 100, text=txt, font=f'Arial {z}', angle= 0)
# canvas.create_text(170, 170, text=txt, font=f'Arial {z}', angle= 270)

canvas.create_rectangle(0, 75, 200, 125)
canvas.create_rectangle(180, 85, 300, 115)
canvas.create_rectangle(400, 400, 520, 430)
canvas.create_rectangle(400, 400, 520, 430)




canvas.mainloop()