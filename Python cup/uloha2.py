from tkinter import *
import random, time


def click(event):

    if zviera_suradnice_z[0] <= event.x <= zviera_suradnice_z[0] + 100 and \
            zviera_suradnice_z[1] <= event.y <= zviera_suradnice_z[1] + 100:

        vybrane = canvas.create_image(100, 900, image=zviera, tags="vybrane")

        window.update()

        pocet = 0

        zviera_suradnice = canvas.coords(vybrane)

        while zviera_suradnice[0] < 900:

            pocet += 1

            canvas.move(vybrane, 50, 0)

            canvas.create_image(100 + 50 * pocet, 950, image=stopa)

            zviera_suradnice = canvas.coords(vybrane)

            time.sleep(0.4)

            window.update()


window = Tk()
canvas = Canvas(window, width=1000, height=1000)
canvas.pack()

zviera0 = PhotoImage(file="images\\zviera0.png")
zviera1 = PhotoImage(file="images\\zviera1.png")
zviera2 = PhotoImage(file="images\\zviera2.png")
zviera3 = PhotoImage(file="images\\zviera3.png")
zviera4 = PhotoImage(file="images\\zviera4.png")

stopy0 = PhotoImage(file="images\\stopy0.png")
stopy1 = PhotoImage(file="images\\stopy1.png")
stopy2 = PhotoImage(file="images\\stopy2.png")
stopy3 = PhotoImage(file="images\\stopy3.png")
stopy4 = PhotoImage(file="images\\stopy4.png")

macka = canvas.create_image(100, 50, image=zviera0, tags="macka" , anchor=NW)
hus = canvas.create_image(250, 100, image=zviera1, tags="hus" , anchor=NW)
kohut = canvas.create_image(400, 50, image=zviera2, tags="kohut" , anchor=NW)
krava = canvas.create_image(550, 100, image=zviera3, tags="krava" , anchor=NW)
prasa = canvas.create_image(700, 100, image=zviera4, tags="prasa" , anchor=NW)

list_of_zvierata = [zviera0, zviera1, zviera2, zviera3, zviera4]
list_of_stopy = [stopy0, stopy1, stopy2, stopy3, stopy4]

index = random.randint(0, 4)


list_of_images = [macka, hus, kohut, krava, prasa]
zviera = list_of_zvierata[index]
stopa = list_of_stopy[index]

zviera_suradnice_z = canvas.coords(list_of_images[index])

window.update()

vybrana_stopa = canvas.create_image(100, 950, image=stopa, tags="vybranastopa", anchor=CENTER)

window.update()

window.bind("<Button-1>", click)

canvas.mainloop()
