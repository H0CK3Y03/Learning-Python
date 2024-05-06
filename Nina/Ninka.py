import tkinter


subjektivne = input("Zadaj co chces: ")

def nieco(event):
    canvas.create_text(event.x, event.y, text=subjektivne)


canvas = tkinter.Canvas(height=1000, width=1000)
canvas.pack()

canvas.bind("<Button-1>", nieco)

canvas.mainloop()
