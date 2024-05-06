from tkinter import *
import random


def move_up(event):

    global list_of_eggs, count, eggs_left

    if canvas.coords(girl)[1] != 65:

        canvas.move(girl, 0, -SPEED)

        # Check for egg collisions
        girl_bbox = canvas.bbox(girl)
        overlapping_eggs = canvas.find_overlapping(*girl_bbox)

        for egg in overlapping_eggs:

            if "egg" in canvas.gettags(egg):

                canvas.delete(egg)

                count += 1

                score.config(text=f"Eggs: {count}")

                eggs_left -= 1

                if eggs_left == 0:

                    canvas.create_text(canvas.winfo_width() / 2,
                                       canvas.winfo_height() / 2,
                                       text="YOU WIN!!!!",
                                       font=("Courier", 30),
                                       fill="red")

    window.update()


def move_left(event):

    global list_of_eggs, count, eggs_left

    if canvas.coords(girl)[0] != 65:

        canvas.move(girl, -SPEED, 0)

        # Check for egg collisions
        girl_bbox = canvas.bbox(girl)
        overlapping_eggs = canvas.find_overlapping(*girl_bbox)

        for egg in overlapping_eggs:

            if "egg" in canvas.gettags(egg):

                canvas.delete(egg)

                count += 1

                score.config(text=f"Eggs: {count}")

                eggs_left -= 1

                if eggs_left == 0:

                    canvas.create_text(canvas.winfo_width() / 2,
                                       canvas.winfo_height() / 2,
                                       text="YOU WIN!!!!",
                                       font=("Courier", 30),
                                       fill="red")

    window.update()


def move_down(event):

    global list_of_eggs, count, eggs_left

    if canvas.coords(girl)[1] != canvas.winfo_height() - 65:

        canvas.move(girl, 0, SPEED)

        # Check for egg collisions
        girl_bbox = canvas.bbox(girl)
        overlapping_eggs = canvas.find_overlapping(*girl_bbox)

        for egg in overlapping_eggs:

            if "egg" in canvas.gettags(egg):

                canvas.delete(egg)

                count += 1

                score.config(text=f"Eggs: {count}")

                eggs_left -= 1

                if eggs_left == 0:

                    canvas.create_text(canvas.winfo_width() / 2,
                                       canvas.winfo_height() / 2,
                                       text="YOU WIN!!!!",
                                       font=("Courier", 30),
                                       fill="red")

    window.update()


def move_right(event):

    global list_of_eggs, count, eggs_left

    if canvas.coords(girl)[0] != canvas.winfo_width() - 65:

        canvas.move(girl, SPEED, 0)

        # Check for egg collisions
        girl_bbox = canvas.bbox(girl)
        overlapping_eggs = canvas.find_overlapping(*girl_bbox)

        for egg in overlapping_eggs:

            if "egg" in canvas.gettags(egg):

                canvas.delete(egg)

                count += 1

                score.config(text=f"Eggs: {count}")

                eggs_left -= 1

                if eggs_left == 0:

                    canvas.create_text(canvas.winfo_width() / 2,
                                       canvas.winfo_height() / 2,
                                       text="YOU WIN!!!!",
                                       font=("Courier", 30),
                                       fill="red")

    window.update()


AREA = 65
SPEED = 65

window = Tk()
canvas = Canvas(window, height=390 - 4, width=520 - 4)
canvas.pack()

girl_image = PhotoImage(file='dievca.png')
egg_image = PhotoImage(file="vajicko.png")

window.update()

girl = canvas.create_image(AREA, canvas.winfo_height() - AREA, image=girl_image, tags="girl")

count = 0

eggs_left = 0

list_of_eggs = []

for i in range(1, 5):

    for z in range(1, 8):

        chance = random.randint(0, 1)  # 1 means True

        if chance:

            eggs = canvas.create_image(AREA * z, AREA * i, image=egg_image, tags=f"egg")

            window.update()

            list_of_eggs.append(canvas.coords(eggs))

            eggs_left += 1

score = Label(canvas,
             text=f"Eggs: {count}",
             font=("Arial", 15)
             )
score.place(relx=1, x=-2, y=2, anchor=NE)

window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)

window.mainloop()