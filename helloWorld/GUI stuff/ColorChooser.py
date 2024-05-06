from tkinter import *
from tkinter import colorchooser  # this is a submodule

def click():
    # color = colorchooser.askcolor() # creates a tuple of RGB values, and a hexidecimal value on indexes 0 and 1
    # # print(color) # prints the RGB amount values and the hexidecimal representation of the values
    # colorHex = color[1]
    # # print(colorHex)
    # window.config(bg=colorHex) # change background color

    # color = colorchooser.askcolor()
    # window.config(bg=color[1])   # same thing in less lines of code

    window.config(bg=colorchooser.askcolor()[1]) # even less lines of code

window = Tk()
window.geometry('420x420')
button = Button(window,
                text='click me',
                command=click)
button.pack()

window.mainloop()





















