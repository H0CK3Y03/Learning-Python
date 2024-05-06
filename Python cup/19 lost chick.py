from tkinter import *
import random, time


window = Tk()
canvas = Canvas(window, height=1000, width=1000, background="cyan")
canvas.pack()


x = random.randint(100, (1000 // 100 - 1) * 100)
y = random.randint(100, (1000 // 100 - 1) * 100)


duckling_photoimage = PhotoImage(file="duckling.png")
duckling = canvas.create_image(x, y, image=duckling_photoimage)

duckling_coordinates = canvas.coords(duckling)

window.update()

time.sleep(1)

x_coordinate = canvas.create_text(x, y + 100, text=f'x : {int(duckling_coordinates[0])}', tags="x")

window.update()

time.sleep(1)

canvas.delete("x")

y_coordinate = canvas.create_text(x, y + 100, text=f'y : {int(duckling_coordinates[1])}', tags="y")

window.update()

time.sleep(1)

canvas.delete("y")

window.update()

answer = int(input("x coordinate of duckling: "))

if answer != int(duckling_coordinates[0]):

    canvas.create_text(x, y + 100, text=f'x was: {int(duckling_coordinates[0])}', tags="x")

else:

    answer = int(input("y coordinate of duckling: "))

    if answer != int(duckling_coordinates[1]):

        canvas.create_text(x, y + 100, text=f'y was: {int(duckling_coordinates[0])}', tags="x")

    else:

        canvas.create_text(x, y + 100, text=f'You found the duck!!!!!')

window.mainloop()
