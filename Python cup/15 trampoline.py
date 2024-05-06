from tkinter import *
import random, time


SPEED = 0.05


def jump_around():


    global simon

    y_velocity = 10

    while True:

        position = canvas.coords(simon)

        window.update()

        jump_height = random.randint(30, 200)

        y_velocity *= -1

        for i in range(jump_height // -y_velocity):

            canvas.move(simon, 0, y_velocity)

            window.update()

            position = canvas.coords(simon)

            time.sleep(SPEED)

        y_velocity = -y_velocity

        canvas.delete("simon")

        simon = canvas.create_image(position[0],
                           position[1],
                           image=p2, anchor=S, tags="simon")

        for i in range(jump_height // y_velocity):

            canvas.move(simon, 0, y_velocity)

            window.update()

            position = canvas.coords(simon)

            time.sleep(SPEED)

        canvas.delete("simon")

        simon = canvas.create_image(position[0],
                                    position[1],
                                    image=p0, anchor=S, tags="simon")


window = Tk()

back_trampoline = PhotoImage(file="trampolina.png")

canvas = Canvas(window, height=back_trampoline.height() * 20, width=back_trampoline.width() * 4)
canvas.pack()

window.update()

canvas.create_image(window.winfo_width() / 2,
                    window.winfo_height() / 2,
                    image=back_trampoline)

p0 = PhotoImage(file="p0.png")
p2 = PhotoImage(file="p2.png")

simon = canvas.create_image(window.winfo_width() / 2,
                           window.winfo_height() / 2 - 10,
                           image=p0, anchor=S, tags="simon")


jump_around()


window.mainloop()
