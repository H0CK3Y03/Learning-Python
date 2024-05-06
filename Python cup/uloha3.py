from tkinter import *
import random, time


def click(event):

    global duch_suradnice

    if duch_suradnice[0] <= event.x <= duch_suradnice[0] + 50 and\
        duch_suradnice[1] <= event.y <= duch_suradnice[1] + 50:

        canvas.create_image(duch_suradnice[0], duch_suradnice[1], image=duch_photoimage, anchor=NW)

        canvas.create_text(duch_suradnice[0] + 50, duch_suradnice[1], text="SUPER", anchor=NW)

    else:

        canvas.create_image(duch_suradnice[0], duch_suradnice[1], image=duch_photoimage, anchor=NW)

        canvas.create_text(duch_suradnice[0] + 50, duch_suradnice[1], text="TU SOM", anchor=NW)


window = Tk()

duch_photoimage = PhotoImage(file="images\\duch.png")

M = random.randint(3, 5)
N = random.randint(3, 7)

canvas = Canvas(window, width=N * 50, height=M * 50)
canvas.pack()

for riadok in range(M):

    canvas.create_line(0, 50 + (50 * riadok), N * 50, 50 + (50 * riadok))

    for stlpec in range(N):

        canvas.create_line(50 + (50 * stlpec), 0, 50 + (50 * stlpec), M * 50)

for i in range(M):

    for z in range(N):

        ano = random.randint(0, 1)

        if ano:

            canvas.create_rectangle(i * 50, z * 50, i * 50 + 50, z * 50 + 50, fill="gray")

for i in range(random.randint(3, 5)):

            duch = canvas.create_image(50 * random.randint(0, (N - 1)),
                                       50 * random.randint(0, (M - 1)),
                                       image=duch_photoimage, tags=f"duch", anchor=NW)

            window.update()

            duch_suradnice = canvas.coords(duch)

            time.sleep(0.5)

            canvas.delete("duch")


window.bind("<Button-1>", click)

window.mainloop()
