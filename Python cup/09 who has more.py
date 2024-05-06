from tkinter import *
import random


def final():

    if player1_number > player2_number:
        canvas.delete("ref")
        canvas.create_image(500, 500, image=referee_left)
        canvas.create_text(500, 800, font=("Arial", 30), text="Player 1 wins!!!")
    elif player1_number < player2_number:
        canvas.delete("ref")
        canvas.create_image(500, 500, image=referee_right)
        canvas.create_text(500, 800, font=("Arial", 30), text="Player 2 wins!!!")
    else:
        canvas.delete("ref")
        canvas.create_image(500, 500, image=referee_both)
        canvas.create_text(500, 800, font=("Arial", 30), text="It's a draw!!!")


window = Tk()
canvas = Canvas(window, height=1000, width=1000)
canvas.pack()

# -----------------------------------------------------------
# These are the images created in krita
player_left = PhotoImage(file="red.png")
player_right = PhotoImage(file="blu.png")
referee = PhotoImage(file="ref.png")
referee_left = PhotoImage(file="ref_left.png")
referee_right = PhotoImage(file="ref_right.png")
referee_both = PhotoImage(file="ref_both.png")
# ------------------------------------------------------------
left = canvas.create_image(250, 500, image=player_left)
right = canvas.create_image(750, 500, image=player_right)
center = canvas.create_image(500, 500, image=referee, tags="ref")
# ------------------------------------------------------------

player1_number = random.randint(1, 100)
player2_number = random.randint(1, 100)

player1_number_text = canvas.create_text(250, 700, text=player1_number, font=("Arial", 20))
player2_number_text = canvas.create_text(750, 700, text=player2_number, font=("Arial", 20))


window.after(1500, final)


window.mainloop()
