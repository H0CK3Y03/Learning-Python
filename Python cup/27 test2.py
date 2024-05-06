from tkinter import *
import random


def move_up(event):

    global list_of_eggs

    if canvas.coords(girl)[1] != 65:

        canvas.move(girl, 0, -SPEED)

        # Check for egg collisions
        girl_bbox = canvas.bbox(girl)
        overlapping_items = canvas.find_overlapping(*girl_bbox)

        for item in overlapping_items:
            if "egg" in canvas.gettags(item):
                canvas.delete(item)

    window.update()


def move_left(event):

    global list_of_eggs

    if canvas.coords(girl)[0] != 65:

        canvas.move(girl, -SPEED, 0)

        # Check for egg collisions
        girl_bbox = canvas.bbox(girl)
        overlapping_items = canvas.find_overlapping(*girl_bbox)

        for item in overlapping_items:
            if "egg" in canvas.gettags(item):
                canvas.delete(item)

    window.update()


def move_down(event):

    global list_of_eggs

    if canvas.coords(girl)[1] != canvas.winfo_height() - 65:

        canvas.move(girl, 0, SPEED)

        # Check for egg collisions
        girl_bbox = canvas.bbox(girl)
        overlapping_items = canvas.find_overlapping(*girl_bbox)

        for item in overlapping_items:
            if "egg" in canvas.gettags(item):
                canvas.delete(item)

    window.update()


def move_right(event):

    global list_of_eggs

    if canvas.coords(girl)[0] != canvas.winfo_width() - 65:

        canvas.move(girl, SPEED, 0)

        # Check for egg collisions
        girl_bbox = canvas.bbox(girl)
        overlapping_items = canvas.find_overlapping(*girl_bbox)

        for item in overlapping_items:
            if "egg" in canvas.gettags(item):
                canvas.delete(item)

    window.update()



AREA = 65
SPEED = 65

window = Tk()
canvas = Canvas(window, height=390 - 4, width=520 - 4)
canvas.pack()

girl_image = PhotoImage(file='dievca.png')
egg_image = PhotoImage(file="vajicko.png")

window.update()

print(canvas.winfo_reqheight(), canvas.winfo_reqwidth())

girl = canvas.create_image(AREA, canvas.winfo_height() - AREA, image=girl_image, tags="girl")

list_of_eggs = []
count = 0

for i in range(1, 5):

    for z in range(1, 8):

        count += 1

        eggs = canvas.create_image(AREA * z, AREA * i, image=egg_image, tags=f"egg")

        window.update()

        list_of_eggs.append(canvas.coords(eggs))

        print(f"{list_of_eggs.index(canvas.coords(eggs))} - {canvas.coords(eggs)}")

print(list_of_eggs)



window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)



window.mainloop()