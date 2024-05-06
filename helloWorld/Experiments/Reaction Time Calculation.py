from tkinter import *
import random
import time

HEIGHT = 1000
WIDTH = 1000
SIZE = 50
SPEED = 50


class Target:

    def __init__(self):

        x = random.randint(0, (WIDTH // SIZE) - 1) * SIZE
        y = random.randint(0, (HEIGHT // SIZE) - 1) * SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SIZE, y + SIZE, fill='#00FF00', tags="target")
        canvas.create_line((x + SIZE / 2), y, (x + SIZE / 2) , y + SIZE, tags="cross")
        canvas.create_line(x, (y + SIZE / 2), x + SIZE, (y + SIZE / 2), tags="cross")


def click(event):

    global score, miss, target, start, average, time_list

    if target.coordinates[0] <= event.x <= target.coordinates[0] + SIZE and \
            target.coordinates[1] <= event.y <= target.coordinates[1] + SIZE:

        score += 1
        score_label.config(text=f'Score: {score}')

        canvas.delete('target', 'cross')

        target = Target()

        end = time.perf_counter()

        time_list.append(end - start)

        time_label.config(text=f"time: {end - start:.2f}s")

        average = sum(time_list) / len(time_list)

        average_time.config(text=f"Your average reaction time is: {average:.2f} seconds")

        start = time.perf_counter()

        return start

    else:
        miss += 1
        miss_label.config(text=f'Misses: {miss}')

    window.update()


window = Tk()
window.title("Reaction Time Calculation")

score = 0
miss = 0
time_list = []
average = 0

score_label = Label(window,
                    text=f"Score: {score}",
                    font=("Arial", 20),
                    foreground="#000000")
score_label.pack()

miss_label = Label(window,
                    text=f"Misses: {miss}",
                    font=("Arial", 20),
                    foreground="#000000")
miss_label.pack()

time_label = Label(window,
                   text=f"time:",
                   foreground="#000000",
                   font=("Arial",20))
time_label.pack()

average_time = Label(window,
                     text=f"Your average reaction time is: {average} seconds",
                     foreground="#000000",
                     font=("Arial",20))
average_time.pack()

canvas = Canvas(window, background="#111111", width=WIDTH, height=HEIGHT)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

target = Target()
window.bind("<Button-1>", lambda event: click(event))

start = time.perf_counter()

window.mainloop()
