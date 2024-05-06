from tkinter import *
import random, time


window = Tk()
canvas = Canvas(window, height=1000, width=1000)
canvas.pack()

default = PhotoImage(file="p0.png")
left_hand = PhotoImage(file="p1.png")
both_hands = PhotoImage(file="p2.png")
left_leg = PhotoImage(file="p3.png")
right_leg = PhotoImage(file="p4.png")

simon = canvas.create_image(300, 500, image=default, tags="simon")
matus = canvas.create_image(700, 500, image=default, tags="matus")

window.update()

time.sleep(1)

positions = [default, left_leg, both_hands, left_leg, right_leg]

while True:

    if random.choice(positions) == default:

        time.sleep(1)
        canvas.delete("simon")
        simon = canvas.create_image(300, 500, image=default, tags="simon")
        window.update()
        time.sleep(1)
        canvas.delete("matus")
        matus = canvas.create_image(700, 500, image=default, tags="matus")
        window.update()

    elif random.choice(positions) == left_hand:

        time.sleep(1)
        canvas.delete("simon")
        simon = canvas.create_image(300, 500, image=left_hand, tags="simon")
        window.update()
        time.sleep(1)
        canvas.delete("matus")
        matus = canvas.create_image(700, 500, image=left_hand, tags="matus")
        window.update()

    elif random.choice(positions) == both_hands:

        time.sleep(1)
        canvas.delete("simon")
        simon = canvas.create_image(300, 500, image=both_hands, tags="simon")
        window.update()
        time.sleep(1)
        canvas.delete("matus")
        matus = canvas.create_image(700, 500, image=both_hands, tags="matus")
        window.update()

    elif random.choice(positions) == left_leg:

        time.sleep(1)
        canvas.delete("simon")
        simon = canvas.create_image(300, 500, image=left_leg, tags="simon")
        window.update()
        time.sleep(1)
        canvas.delete("matus")
        matus = canvas.create_image(700, 500, image=left_leg, tags="matus")
        window.update()

    elif random.choice(positions) == right_leg:

        time.sleep(1)
        canvas.delete("simon")
        simon = canvas.create_image(300, 500, image=right_leg, tags="simon")
        window.update()
        time.sleep(1)
        canvas.delete("matus")
        matus = canvas.create_image(700, 500, image=right_leg, tags="matus")
        window.update()


window.mainloop()
