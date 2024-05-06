from tkinter import *
import random


def click(event):

    global target, score, score_label

    xtarget = canvas.coords(target)[0]
    ytarget = canvas.coords(target)[1]

    if xtarget < event.x < xtarget + 100 and ytarget < event.y < ytarget + 100:

        score += 1

        score_label.config(text=f"Score: {score}")

        canvas.delete("target")

        x = random.randint(100, 900)
        y = random.randint(100, 900)

        target = canvas.create_rectangle(x, y, x + 100, y + 100, fill="red", tags="target")

        window.update()

    elif not (xtarget < event.x < xtarget + 100 and ytarget < event.y < ytarget + 100):

        score -= 2

        score_label.config(text=f'Score: {score}')

        window.update()


window = Tk()
canvas = Canvas(window, width=1000, height=1000)
canvas.pack()

x = random.randint(100, 900)
y = random.randint(100, 900)

target = canvas.create_rectangle(x, y, x + 100, y + 100, fill="red", tags="target")

score = 0

score_label = Label(canvas, text=f"Score: {score}")
score_label.place(x=900, y=50)

window.bind("<Button-1>", click)


canvas.mainloop()
