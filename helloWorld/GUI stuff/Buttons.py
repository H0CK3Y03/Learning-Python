# button = you click it, then it does stuff

from tkinter import *

count = 0

def click():
    global count         # we list the local variable (count) as a global variable, so we can use it in our definition
    count += 1
    print(count)

window = Tk()

photo = PhotoImage(file="C:\\Users\\Adam Vesely\\PycharmProjects\\pythonProject\\helloWorld\\Advanced\\Legion.png")

button = Button(window,                       # syntax -> (master[window in this case])
                text="click me!",
                command=click,                # we list a function name without it's parenthesis, this is what's known as a callback [a function without parenthesis]
                font=("Comic Sans",30),
                fg="#00FF00",                 # inactive foreground (not being pressed)
                bg="black",                   # inactive background
                activeforeground="#1721d4",   # active foreground (being pressed)
                activebackground='red',       # active background
                state=ACTIVE,                 # can disable (by putting DISABLED)the button (default is ACTIVE)
                image=photo,                  # again photo covers text
                compound="top")               # so we need to compound

button.pack()

window.mainloop()






















