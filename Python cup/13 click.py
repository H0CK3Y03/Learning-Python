from tkinter import *
import random


HEIGHT = 1000
WIDTH = 1000
SIZE = 50
SPEED = 1000


class Target:

    def __init__(self):

        x = random.randint(0, (WIDTH // SIZE) - 1) * SIZE
        y = random.randint(0, (HEIGHT // SIZE) - 1) * SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SIZE, y + SIZE, fill='#00FF00', tags="target")
        canvas.create_line((x + SIZE / 2), y, (x + SIZE / 2) , y + SIZE, tags="cross")
        canvas.create_line(x, (y + SIZE / 2), x + SIZE, (y + SIZE / 2), tags="cross")

        self.timer_id = window.after(1000, self.move)

    def move(self):
        canvas.delete('target', 'cross')
        window.after_cancel(self.timer_id)

        x = random.randint(0, (WIDTH // SIZE) - 1) * SIZE
        y = random.randint(0, (HEIGHT // SIZE) - 1) * SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SIZE, y + SIZE, fill='#00FF00', tags="target")
        canvas.create_line((x + SIZE / 2), y, (x + SIZE / 2) , y + SIZE, tags="cross")
        canvas.create_line(x, (y + SIZE / 2), x + SIZE, (y + SIZE / 2), tags="cross")

        self.timer_id = window.after(1000, self.move)

    def click(self, event):
        global score
        if self.coordinates[0] <= event.x <= self.coordinates[0] + SIZE and \
                self.coordinates[1] <= event.y <= self.coordinates[1] + SIZE:
            score += 1
            score_label.config(text=f'{score}')
            canvas.delete('target', 'cross')
            window.after_cancel(self.timer_id)
            self.move()
        else:
            score -= 2
            score_label.config(text=f'{score}')

    def start(self):
        self.move()
        window.bind("<Button-1>", self.click)


score = 0

window = Tk()
window.title("Reaction Time Calculation")

canvas = Canvas(window, background="#111111", width=WIDTH, height=HEIGHT)
canvas.pack()

score_label = Label(window,
                    text=f"{score}",
                    font=("Arial", 20),
                    foreground="#FFFFFF",
                    background='#111111')
score_label.place(relx=1, x=-2, y=2, anchor=NE)

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

target = Target()
target.start()

window.mainloop()
