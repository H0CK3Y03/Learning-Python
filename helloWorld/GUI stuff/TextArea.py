# text widget = functions like a text area, you can enter multiple lines of text

from tkinter import *

def submit():
    input = text.get('1.0',END)  # gets input from 1st line to the END
    print(input)

window = Tk()

text = Text(window,
            bg='light yellow',
            font=('Ink Free',25),      # the text area size corresponds directly to the font size
            height=8,                  # amount of characters this is high
            width=20,                  # amount of characters this is wide
            padx=20,
            pady=20,
            fg="purple")

text.pack()

button = Button(window, command=submit, text='submit')
button.pack()

window.mainloop()





















