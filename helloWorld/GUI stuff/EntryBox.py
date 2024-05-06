# entry widget = textbox that accepts a single line of user input

from tkinter import *

def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)

def clear():
    entry.delete(0,END)           # two positional arguments, (0,END) deletes all characters in the entry box

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,                # syntax -> within the constructor [the parenthesis ()] we type in a master [this case variable window] then args
              font=('Arial',50),
              fg="#00FF00",
              bg="black",
              show="*")              # hides actual text, replaces it with what we want [this case an asterisk (*)]

# entry.insert(0,'Spongebob')        # can insert text into the chosen position (position, text)

entry.pack(side='left')              # side= -> changes the placement, we can also type LEFT without the quotations ('')

submit_button = Button(window,
                       text='submit',
                       command=submit)    # command = function name without parenthesis

submit_button.pack(side='right')     # same here -> RIGHT is eligible

clear_button = Button(window,
                       text='clear',
                       command=clear)

clear_button.pack(side='right')

backspace_button = Button(window,
                       text='backspace',
                       command=backspace)

backspace_button.pack(side='right')

window.mainloop()


























