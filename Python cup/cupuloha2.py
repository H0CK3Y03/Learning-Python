from tkinter import *
import random, time


SPEED = 20


window = Tk()
canvas = Canvas(window, height=1000, width=1000)
canvas.pack()

hive = canvas.create_oval(10, 940, 60, 990, fill="yellow", tags="hive")
bee = canvas.create_rectangle(20, 960, 30, 970, fill="black", tags="bee")

list_of_flower_coords = []

for i in range(3):

    x = random.randint(10, 940)
    y = random.randint(10, 850)

    flower = canvas.create_oval(x, y, x + 50, y + 50, tags="flower")

    list_of_flower_coords.append(canvas.coords(flower))

random.shuffle(list_of_flower_coords)

bee_coordinates = canvas.coords(bee)

for z in range(3):

    startx = bee_coordinates[0]
    starty = bee_coordinates[1]

    while True:

        canvas.move(bee, (list_of_flower_coords[0 + z][0] + 25 - startx) / SPEED,
                    (list_of_flower_coords[0 + z][1] + 25 - starty) / SPEED)

        window.update()

        time.sleep(0.1)

        bee_coordinates = canvas.coords(bee)

        if list_of_flower_coords[0 + z][0] < bee_coordinates[0] + 5 < list_of_flower_coords[0 + z][0] + 50 and\
            list_of_flower_coords[0 + z][1] < bee_coordinates[1] + 5 < list_of_flower_coords[0 + z][1] + 50:

            break

while True:

    startx = bee_coordinates[0]
    starty = bee_coordinates[1]

    canvas.move(bee, (canvas.coords(hive)[0] + 25 - startx) / SPEED,
                    (canvas.coords(hive)[1] + 25 - starty) / SPEED)

    window.update()

    time.sleep(0.1)

    if canvas.coords(hive)[0] + 50 < bee_coordinates[0] + 5 < canvas.coords(hive)[0] + 50 and\
        canvas.coords(hive)[1] < bee_coordinates[1] + 5 < canvas.coords(hive)[1] + 50:

        break


window.mainloop()
