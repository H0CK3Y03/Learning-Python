from tkinter import *
import time

WIDTH = 550         # this is a constant (a variable  that we don't plan to change), we usually capitalize the whole word, it is a common naming convention
HEIGHT = 550
xVelocity = 3
yVelocity = 2

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

back_LEG = PhotoImage(file='C:\\Users\\Adam Vesely\\PycharmProjects\\pythonProject\\helloWorld\\Advanced\\Legion.png')
background = canvas.create_image(0, 0, image=back_LEG, anchor=NW)

helmet = PhotoImage(file='C:\\Users\\Adam Vesely\\PycharmProjects\\pythonProject\\helloWorld\\Advanced\\Brotherhood_helmet.png')
my_image = canvas.create_image(0,0,image=helmet,anchor=NW)

helmet_width = helmet.width()
helmet_height = helmet.height()

while True:
    coordinates = canvas.coords(my_image)  # provides us with a list of the x and y axis values of our image (they are floats)
    print(coordinates)
    if coordinates[0] >= WIDTH - helmet_width or coordinates[0]<0:  # coordinates[0 -> x, 1 -> y]
       xVelocity *= -1
       #  xVelocity = xVelocity * -1
       #  xVelocity = -xVelocity

    if coordinates[1] >= HEIGHT - helmet_height or coordinates[1]<0:
       yVelocity *= -1

    canvas.move(my_image,xVelocity,yVelocity)
    window.update()
    time.sleep(0.01)

window.mainloop()



























