from tkinter import *
import random, time


def check_for_collision():

    balloon_hitbox = [balloon_coordinates[0] - balloon_start.width() / 2,
                      balloon_coordinates[1] - balloon_start.height() / 2,
                      balloon_coordinates[0] + balloon_start.width() / 2,
                      balloon_coordinates[1] + balloon_start.height() / 2
                      ]
    cactus_hitbox = [cactus_coordinates[0] - cactus_image.width() / 2,
                     cactus_coordinates[1] - cactus_image.height() / 2,
                     cactus_coordinates[0] + cactus_image.width() / 2,
                     cactus_coordinates[1] + cactus_image.height() / 2
                     ]

    if balloon_hitbox[2] >= cactus_hitbox[0] and balloon_hitbox[3] >= cactus_hitbox[1]:
        canvas.create_text(500, 500, text="pop")
        window.update()
        return True


def creation(balloon_coordinates, image):

    canvas.delete("balloon")
    canvas.create_image(balloon_coordinates, image=image, tags="balloon")
    window.update()


window = Tk()
canvas = Canvas(window, height=1000, width=1000)
canvas.pack()

balloon_start = PhotoImage(file="balon1.png")
balloon_mid = PhotoImage(file="balon2.png")
balloon_end = PhotoImage(file="balon3.png")
cactus_image = PhotoImage(file="kaktus.png")

cactus = canvas.create_image(random.randint(500, 950),
                             random.randint(500, 950),
                             image=cactus_image, tags="cactus")
balloon = canvas.create_image(random.randint(50, 500),
                              random.randint(50, 500),
                              image=balloon_start, tags="balloon")

cactus_coordinates = canvas.coords(cactus)
balloon_coordinates = canvas.coords(balloon)



for i in range(1, 11):

    dx = cactus_coordinates[0] - balloon_coordinates[0]
    dy = cactus_coordinates[1] - balloon_coordinates[1]
    distance = (dx ** 2 + dy ** 2) ** 0.5
    speed = random.randint(30, 101)

    canvas.move(balloon,
                dx / distance * speed,
                dy / distance * speed)

    balloon_coordinates = canvas.coords(balloon)

    window.update()
    check_for_collision()

    if check_for_collision():
        time.sleep(0.3)
        # canvas.delete("balloon")
        # canvas.create_image(balloon_coordinates, image=balloon_mid, tags="balloon")
        window.after(500, creation(balloon_coordinates, balloon_mid))
        window.after(500, creation(balloon_coordinates, balloon_end))
        time.sleep(0.5)
        canvas.delete("balloon")
        break

    time.sleep(0.2)

window.mainloop()
