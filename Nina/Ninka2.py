import tkinter


def znacka(event):
    canvas.create_line(event.x, event.y, event.x, event.y - 200, width=5, fill="gray")
    canvas.create_rectangle(event.x - 75,event.y - 250, event.x + 75, event.y - 200)
    canvas.create_text(event.x, event.y - 225, text=entry.get())

    if entry2.get() == "k":
        canvas.create_line(event.x - 75, event.y - 200, event.x + 75, event.y - 250, width=4, fill="dark gray")


canvas = tkinter.Canvas(height=1000, width=1000)
canvas.pack()

canvas.bind("<Button-1>", znacka)

button = tkinter.Button(
    canvas,
    text="zmazat",
    command=lambda: canvas.delete("all"))
button.place(x=485, y=900)

entry = tkinter.Entry()
entry.place(x=450, y=930)

entry2 = tkinter.Entry()
entry2.place(x=450, y=950)

canvas.mainloop()
