from tkinter import *
import random, time


def die():

    global number
    window.update()
    x = random.randint(0, canvas.winfo_width() - 200)
    y = random.randint(0, 200)

    canvas.create_rectangle(x, y, x + 100, y + 100)

    if number == 1:

        canvas.create_oval(x + 5, y + 5, x + 30, y + 30, fill="blue")

    if number == 2:

        canvas.create_oval(x + 5, y + 5, x + 30, y + 30, fill="blue")
        canvas.create_oval(x - 30 + 100, y - 30 + 100, x + 100 - 5, y + 100 - 5, fill="blue")

    if number == 3:

        canvas.create_oval(x + 5, y + 5, x + 30, y + 30, fill="blue")
        canvas.create_oval(x + 50 - 12.5, y + 50 - 12.5, x + 50 + 12.5, y + 50 + 12.5, fill="blue")
        canvas.create_oval(x - 30 + 100, y - 30 + 100, x + 100 - 5, y + 100 - 5, fill="blue")


    if number == 4:
        canvas.create_oval(x + 5, y + 5, x + 30, y + 30, fill="blue")
        canvas.create_oval(x + 5, y - 5 + 100, x + 30, y + 100 - 30, fill="blue")
        canvas.create_oval(x - 30 + 100, y - 30 + 100, x + 100 - 5, y + 100 - 5, fill="blue")
        canvas.create_oval(x - 30 + 100, y + 30, x + 100 - 5, y + 5, fill="blue")

    if number == 5:

        canvas.create_oval(x + 5, y + 5, x + 30, y + 30, fill="blue")
        canvas.create_oval(x + 5, y - 5 + 100, x + 30, y + 100 - 30, fill="blue")
        canvas.create_oval(x + 50 - 12.5, y + 50 - 12.5, x + 50 + 12.5, y + 50 + 12.5, fill="blue")
        canvas.create_oval(x - 30 + 100, y - 30 + 100, x + 100 - 5, y + 100 - 5, fill="blue")
        canvas.create_oval(x - 30 + 100, y + 30, x + 100 - 5, y + 5, fill="blue")

    if number == 6:

        canvas.create_oval(x + 5, y + 5, x + 30, y + 30, fill="blue")
        canvas.create_oval(x + 5, y + 50 - 12.5, x + 30, y + 50 + 12.5, fill="blue")
        canvas.create_oval(x + 5, y - 5 + 100, x + 30, y + 100 - 30, fill="blue")
        canvas.create_oval(x - 30 + 100, y - 30 + 100, x + 100 - 5, y + 100 - 5, fill="blue")
        canvas.create_oval(x + 100 - 5, y + 50 - 12.5, x + 100 - 30, y + 50 + 12.5, fill="blue")
        canvas.create_oval(x - 30 + 100, y + 30, x + 100 - 5, y + 5, fill="blue")



window = Tk()
canvas = Canvas(window, height=1000, width=1000)
canvas.pack()

number = random.randint(1, 6)

canvas.create_oval(450, 450, 550, 550, fill='Black')
canvas.create_text(500, 560, text="Player", font=("Arial", 15))
canvas.create_text(500, 440, text=f"You will throw a {number}", font=("Arial", 15))

window.after(1, die())


window.mainloop()
