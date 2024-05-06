from tkinter import *
import random


window = Tk()
canvas = Canvas(window, height=1000, width=1000)
canvas.pack()


s0 = PhotoImage(file="strom0.png")
s1 = PhotoImage(file="strom1.png")
s2 = PhotoImage(file="strom2.png")
s3 = PhotoImage(file="strom3.png")

list_of_trees = [s0, s1, s2, s3]


for i in range(7):

    canvas.create_image(50 + 110 * i, 500, image=random.choice(list_of_trees))

print(list_of_trees)

window.mainloop()
