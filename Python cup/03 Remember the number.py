from tkinter import *
import time
import random

def prog():
    window.update()
    time.sleep(2)
    canvas.create_text(500, 500, text=number, font=("Arial", 20))
    window.update()
    time.sleep(1)
    canvas.delete("all")
    window.update()
    if int(input("What was the number? ")) == number:
        canvas.create_text(500, 500, text="Correct!", font=("Arial", 20))
        window.update()
    else:
        canvas.create_text(500, 500, text=f"It was: {number}", font=("Arial", 20))
        canvas.create_text(500, 400, text="Wrong!", font=("Arial", 20))
        window.update()


window = Tk()
canvas = Canvas(window, height=1000, width=1000)
canvas.pack()

number = random.randint(10000, 100000)

prog()

window.mainloop()
