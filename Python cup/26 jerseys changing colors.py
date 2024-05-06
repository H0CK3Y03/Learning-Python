from tkinter import *
import random


def change(event):

    global changeable, count

    if count % 2 == 1:

        for i in range(len(changeable)):

            canvas.create_oval(changeable[i][0], changeable[i][1], changeable[i][2], changeable[i][3], fill="cyan")

    if count % 2 == 0:

        for f in range(len(changeable)):

            canvas.create_oval(changeable[f][0], changeable[f][1], changeable[f][2], changeable[f][3], fill="red")

    count += 1


window = Tk()

bg_field = PhotoImage(file="ihrisko.png")

count = 1

WIDTH = bg_field.width()
HEIGHT = bg_field.height()
SIZE = 25

canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

canvas.create_image(0, 0, image=bg_field, anchor=NW)

list_of_bol_coordinates = []

for i in range(10):

    for z in range(14):

        bol = canvas.create_oval(WIDTH / 14 * z, HEIGHT / 10 * i, WIDTH / 14 * z + SIZE, HEIGHT / 10 * i + SIZE,
                                 fill="black")

        list_of_bol_coordinates.append(canvas.coords(bol))

print(list_of_bol_coordinates)

changeable = []

for i in range(10):

    chosen = random.choice(list_of_bol_coordinates)

    list_of_bol_coordinates.remove(chosen)

    canvas.create_oval(chosen[0], chosen[1], chosen[2], chosen[3], fill="red")

    changeable.append(chosen)

window.bind("<space>", change)


window.mainloop()