from tkinter import *
import time


window = Tk()

SPEED = 20

bg_planets = PhotoImage(file="planety.png")
rocket_0 = PhotoImage(file="raketa0.png")
rocket_1 = PhotoImage(file="raketa1.png")
rocket_2 = PhotoImage(file="raketa2.png")
rocket_3 = PhotoImage(file="raketa3.png")

PLANET_1 = [bg_planets.width() / 4 + 10, bg_planets.height() - 100]
PLANET_2 = [bg_planets.width() / 4 + 10, bg_planets.height() / 4]
PLANET_3 = [bg_planets.width() / 4 * 3 - 50, bg_planets.height() / 4]
PLANET_4 = [bg_planets.width() / 4 * 3 - 50, bg_planets.height() - 100]


canvas = Canvas(window, height=bg_planets.height(),
                width=bg_planets.width())
canvas.pack()

planets = canvas.create_image(0, 0, image=bg_planets, anchor=NW)

rocket = canvas.create_image(PLANET_1[0],
                             PLANET_1[1],
                             image=rocket_0, tags='rocket')

rocket_coordinates = canvas.coords(rocket)

while rocket_coordinates[1] != PLANET_2[1]:

    canvas.move(rocket, 0, (PLANET_2[1] - PLANET_1[1]) / SPEED)

    rocket_coordinates = canvas.coords(rocket)

    window.update()

    time.sleep(0.1)

canvas.create_text(PLANET_2[0], PLANET_2[1] + 70,
                   text="Centurion", font=("Arial", 20),
                   fill="cyan", tags="planet")

window.update()

canvas.after(1000, canvas.delete("rocket", "planet"))

rocket = canvas.create_image(PLANET_2[0],
                             PLANET_2[1],
                             image=rocket_1, tags='rocket')

while rocket_coordinates[0] != PLANET_3[0]:

    canvas.move(rocket, (PLANET_3[0] - PLANET_2[0]) / SPEED, 0)

    rocket_coordinates = canvas.coords(rocket)

    window.update()

    time.sleep(0.1)

canvas.create_text(PLANET_3[0], PLANET_3[1] + 70, text="Makinosh", font=("Arial", 20), fill="cyan", tags="planet")

window.update()

window.after(1000, canvas.delete("rocket", "planet"))

rocket = canvas.create_image(PLANET_3[0], PLANET_3[1],
                             image=rocket_2, tags="rocket")

while rocket_coordinates[1] != PLANET_4[1]:

    canvas.move(rocket, 0, (PLANET_4[1] - PLANET_3[1]) / SPEED)

    rocket_coordinates = canvas.coords(rocket)

    window.update()

    time.sleep(0.1)

canvas.create_text(PLANET_4[0], PLANET_4[1] - 70,
                   text="Furmigon", font=("Arial", 20), fill="cyan", tags="planet")

window.update()

window.after(1000, canvas.delete("rocket", "planet"))

rocket = canvas.create_image(PLANET_4[0], PLANET_4[1], image=rocket_3, tags="rocket")

while rocket_coordinates[0] != PLANET_1[0]:

    canvas.move(rocket, (PLANET_1[0] - PLANET_4[0]) / SPEED, 0)

    rocket_coordinates = canvas.coords(rocket)

    window.update()

    time.sleep(0.1)

canvas.create_text(PLANET_1[0], PLANET_1[1] - 70,
                   text="Terra Nova", font=("Arial", 20),
                   fill="cyan", tags="planet")

window.update()

window.after(1000, canvas.delete("rocket", "planet"))


window.mainloop()
