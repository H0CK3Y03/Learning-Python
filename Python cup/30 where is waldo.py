from tkinter import *
import random


def check(event):

    global waldo, waldo_bbox

    x = event.x
    y = event.y

    if waldo_bbox[0] <= x <= waldo_bbox[2] and waldo_bbox[1] <= y <= waldo_bbox[3]:

        canvas.delete("imposters")

        canvas.create_text(500, 500, text="YOU FOUND WALDO!", font=("Courier", 20))


window = Tk()
canvas = Canvas(window, width=1000, height=1000)
canvas.pack()

ladybug_left = PhotoImage(file='lienkaL.png')
ladybug_right = PhotoImage(file='lienkaP.png')

for i in range(9):

    for z in range(13):

        imposter = canvas.create_image(random.randint((900 // 13 + (900 // 13) * z) - 10,
                                                          (900 // 13 + (900 // 13) * z) + 10),
                                                          random.randint((900 // 9 + (900 // 9) * i) - 10,
                                                          (900 // 9 + (900 // 9) * i) + 10),
                                                          image=ladybug_left, tags="imposters")

waldo = canvas.create_image(random.randint(900 // 13 - 10, 900 // 13 * 13 + 10),
                            random.randint(900 // 9 - 10, 900 // 9 * 9 + 10),
                            image=ladybug_right, tags="waldo")

waldo_bbox = canvas.bbox(waldo)


window.bind("<Button-1>", check)


window.mainloop()
