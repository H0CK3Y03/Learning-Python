from tkinter import *

def doSomething(event):   # this needs an event if it is called by one
    # print("You pressed: " + event.keysym)  event.keysym (key symbol), is the key that you press
    label.config(text=event.keysym)

window = Tk()

window.bind('<Key>', doSomething)         # takes an event and a function name as args, '<arbitrary key>' -> enter is Return, <Key> -> all/almost all keys

label = Label(window, font=('Helvetica',100))
label.pack()

window.mainloop()



































