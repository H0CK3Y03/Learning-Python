from tkinter import *
import random, time


def tulip_growth():

    global amount, list_of_tulip_coordinates

    amount = random.randint(50, 100)

    list_of_tulip_coordinates = []

    for i in range(amount):

        x_tulip = random.randint(default_1.width() + 10,
                                 1000 - default_1.width() - 10)
        y_tulip = random.randint(default_1.height() + 10,
                                 1000 - default_1.height() - 10)

        tulip = canvas.create_image(x_tulip, y_tulip, image=default_1, tags="tulip")

        list_of_tulip_coordinates.append(canvas.coords(tulip))

        window.update()

    window.after(2000, canvas.delete("tulip"))

    for i in range(amount):

        tulip = canvas.create_image(list_of_tulip_coordinates[i][0],
                                    list_of_tulip_coordinates[i][1],
                                    image=default_2, tags="tulip")

        window.update()

    window.after(2000, canvas.delete("tulip"))

    for i in range(amount):

        tulip = canvas.create_image(list_of_tulip_coordinates[i][0],
                            list_of_tulip_coordinates[i][1],
                            image=default_3, tags="tulip")

        window.update()

    window.after(2000, canvas.delete("tulip"))

    tulip_end()


def tulip_end():

    global amount, list_of_tulip_coordinates

    for i in range(amount):

        end_tulip = random.choice(list_of_end_tulips)

        tulip = canvas.create_image(list_of_tulip_coordinates[i][0],
                            list_of_tulip_coordinates[i][1],
                            image=end_tulip, tags="tulip")

        window.update()


window = Tk()
canvas = Canvas(window, height=1000, width=1000)
canvas.pack()

default_1 = PhotoImage(file="tulipan0.png")
default_2 = PhotoImage(file="tulipan1.png")
default_3 = PhotoImage(file="tulipan2.png")
end_1 = PhotoImage(file="tulipan3.png")
end_2 = PhotoImage(file="tulipan4.png")
end_3 = PhotoImage(file="tulipan5.png")

list_of_end_tulips = [end_1, end_2, end_3]


tulip_growth()


window.mainloop()
