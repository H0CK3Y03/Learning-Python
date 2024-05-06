from tkinter import *
import time

WIDTH = 1000 # tymto menis sirku okna
HEIGHT = 1000  # tymto menis vysku okna
VELOCITY = 5  # tymto menis rychlost pohybujuceho sa stvorca
SIZE = 200  # tymto menis velkost stvorca
xSquare = 0  # tymto menis zacinajucu polohu stvorca vzhladom na jeho lavy horny vrchol a os x
ySquare = 500  # tymto menis zacinajucu polohu stvorca vzhladom na jeho lavy horny vrchol a os y


def click():

    global VELOCITY

    text = entry.get()

    square = canvas.create_rectangle(xSquare, ySquare, xSquare + SIZE, ySquare + SIZE,
                                     fill="turquoise")

    coordinates = canvas.coords(square)

    inside_text = canvas.create_text(coordinates[0] + SIZE / 2,
                                     coordinates[1] + SIZE / 2,
                                     text=text, fill="#111111", font=("Courier", 10))

    while True:

        text = entry.get()

        canvas.itemconfig(inside_text, text=text)

        coordinates = canvas.coords(square)

        if coordinates[0] + SIZE >= canvas.winfo_width() or coordinates[0] < 0:

            VELOCITY = -VELOCITY

        canvas.move(square, VELOCITY, 0)
        canvas.move(inside_text, VELOCITY, 0)

        window.update()
        time.sleep(0.001)


window = Tk()
canvas = Canvas(window, height=HEIGHT, width=WIDTH, background="#111111")
canvas.pack()

button = Button(canvas, text="start",
                command=click,
                font=("Arial", 10),
                foreground="cyan",
                background="#222222",
                activeforeground="yellow",
                activebackground="#444444",
                anchor=CENTER,
                padx=100)
button.place(x=500 - 100, y=950)

entry = Entry(window,
              font=('Arial', 40),
              fg="#00FF00",
              bg="#222222",
              )
entry.place(x=500, y=900, anchor=CENTER)


window.mainloop()
