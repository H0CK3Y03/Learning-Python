from tkinter import *
import random


window = Tk()
canvas = Canvas(window, height=1000, width=1000)
canvas.pack()

my_image_1 = PhotoImage(file="mesec.png")
my_image_2 = PhotoImage(file="minca.png")

canvas.create_image(500 - my_image_1.width()/2, 500 - my_image_1.height()/2,
                    image=my_image_1, anchor=NW)

window.update()

for i in range(int(input("How many coins? "))):
    canvas.create_image(random.randint(0, canvas.winfo_width()),
                        random.randint(0, 500 - my_image_1.height()/2),
                        image=my_image_2, anchor=NW)

window.mainloop()