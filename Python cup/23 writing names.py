from tkinter import *


x = 20
y = 500

def write_letter(letter):

    canvas.create_text(x + x * i, y, text=letter, font=("Arial", 20))


window = Tk()
canvas = Canvas(window, height=1000, width=1000)
canvas.pack()

window.update()


for i in range(int(input("Length of name / word: "))):

    write_letter(input("Your letter: "))

    window.update()

# pos = 0
# while write_letter != "":
#
#     pos += 1
#
#     write_letter(input("Your letter: "))
#
#     window.update()


window.mainloop()
